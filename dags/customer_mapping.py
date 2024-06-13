from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
import json
import pandas as pd
def mapping():
    spark = SparkSession.builder.appName("spark_dataframe_py").getOrCreate()
    url = "jdbc:mysql://172.25.0.1:3306/extenso_config"
    properties = {
            "user": "wsl_root",
            "password": "password",
            "driver": "com.mysql.cj.jdbc.Driver"
        }
    def config(table):
        last_transaction_date = table.select(max("last_modified_date")).collect()[0][0]
        config_data = {
        # "last_transaction_date" : last_date,
        "start_transaction_date" : last_transaction_date.strftime('%Y-%m-%d')
        }
        with open("config.json", "w") as json_file:
            json.dump(config_data, json_file)

    def get_start_last_transaction_date(config_path = "./input_file/config.json"):
        with open(config_path, 'r') as file:
            config_data = json.load(file)
            last_transaction_date = config_data.get('last_transaction_date')
            start_transaction_date = config_data.get('start_transaction_date')
            return start_transaction_date,last_transaction_date
        
    def table(table_name, start_date, end_date):
        df = spark.read.jdbc(url=url, table=table_name, properties=properties)
        if table_name == "rw_transaction_data":
            df = df.filter((df.last_modified_date >= to_date(lit(start_date))))
        return df

    def most_used_product(joined):
        most_used_product = joined.groupBy("product_name").count().fillna(0)
        most_used_product = most_used_product.orderBy("count",ascending=[0])
        top_10 =most_used_product.select("product_name").take(10)
        top_product = [row['product_name'] for row in top_10]
        return top_product

    def map(product_category_map, rw_transaction_data):
        joined = rw_transaction_data.join(product_category_map, ['product_id', 'product_type_id', 'module_id'])
        joined = joined.withColumn("first_day_of_month", trunc(col("last_modified_date"), "month"))
        top_product = most_used_product(joined)
        filtered_df = joined.filter(col("product_name").isin(top_product))
        product_used_count = filtered_df.groupBy("payer_account_id", "product_name").pivot("first_day_of_month").count().fillna(0)
        columns = product_used_count.columns
        start_date = datetime.strptime(columns[2], '%Y-%m-%d').date()
        end_date = datetime.strptime(columns[-1], '%Y-%m-%d').date()
        current_date = start_date
        date_list_comp = []
        while current_date <= end_date:
            date_list_comp.append(current_date.strftime('%Y-%m-%d'))
            current_date = current_date + timedelta(days=32 - current_date.day)
        modified_dates = [date_str[:8] + '01' for date_str in date_list_comp]
        additional_Date = []
        for date in modified_dates:
            if date not in columns:
                additional_Date.append(date)
        if len(additional_Date)!=0: 
            data = {cols: [0] * product_used_count.count() for cols in additional_Date}
            df = pd.DataFrame(data)
            additional_df = spark.createDataFrame(df)
            window = Window.orderBy(monotonically_increasing_id())
            additional_df = additional_df.withColumn("id", row_number().over(window) - 1)
            product_used_count = product_used_count.withColumn("id", row_number().over(window) - 1)
            combined_df = product_used_count.join(additional_df, on="id", how="inner").drop("id")
            excluded_columns = ['payer_account_id', 'product_name']
            coln_combined = excluded_columns + modified_dates + [str(end_date)]
            combined_df = combined_df.select(coln_combined)
        else:
            combined_df = product_used_count
        columns = combined_df.columns
        monthly_columns = columns[2:]
        for column in monthly_columns:
            combined_df= combined_df.withColumn(column, when(col(column) > 0, 1).otherwise(col(column)))
        concat_expr = col(monthly_columns[0])
        for col_name in monthly_columns[1:]:
            concat_expr = concat(concat_expr, col(col_name))
        combined_df = combined_df.withColumn("used_map",concat_expr)
        return combined_df.write.csv('./output_file/final_table_customer_mapping', header=True,mode='overwrite')

    start_date,last_date = get_start_last_transaction_date()
    product_category_map = table("product_category_map",start_date,last_date)
    rw_transaction_data = table("rw_transaction_data",start_date,last_date)
    map(product_category_map,rw_transaction_data)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    'email_on_failure': False,
    'email_on_retry': False,
}
mydag = DAG(
    'customer_mapping',
    default_args=default_args,
    description='A dag for customer_mapping',
    schedule_interval='@once',
    catchup=False,
)
customer_mapping = PythonOperator(
    task_id = "customer_mapping",
    python_callable = mapping,
    dag = mydag,
)
customer_mapping