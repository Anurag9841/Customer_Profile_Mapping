
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json
import os
def main():
    # Initialize the spark session.
    spark = SparkSession.builder.appName("spark_dataframe_py").getOrCreate()
    # JDBC url and connection properties for mysql
    url = "jdbc:mysql://172.25.0.1:3306/extenso_config"
    # 
    properties = {
        "user": "wsl_root",
        "password": "anurag123",
        "driver": "com.mysql.cj.jdbc.Driver"
    }
    emptyRDD = spark.sparkContext.emptyRDD()
    # defining structure for empty schema 
    schema = StructType([
    StructField('payer_account_id', IntegerType(), True),
    StructField('first_day_of_month', DateType(), True),
    StructField('txn_flow', StringType(), True),
    StructField('sum(amount)', DoubleType(), True),
    StructField('count(amount)', LongType(), True),
    StructField('last_modified_date', DateType(), True),
    StructField('min(last_modified_date)', DateType(), True),
    ])
    Schema = spark.createDataFrame(emptyRDD,schema)

    # function to manipulate config file
    def config(table,start_date,last_date):
        if isinstance(start_date, str) and isinstance(last_date, str):
            start_dates = datetime.strptime(start_date, '%Y-%m-%d')
            last_dates = datetime.strptime(last_date, '%Y-%m-%d')
        config_data = {
            "start_transaction_date": (start_dates + relativedelta(months=2)).strftime('%Y-%m-%d'),
            "last_transaction_date" : (last_dates + relativedelta(months=2)).strftime('%Y-%m-%d')
        }
        with open("./input_file/config.json", "w") as json_file:
            json.dump(config_data, json_file)

    # function to read the data from config file
    def get_start_last_transaction_date(config_path = "./input_file/config.json"):
        with open(config_path, 'r') as file:
            config_data = json.load(file)
            last_transaction_date = config_data.get('last_transaction_date')
            start_transaction_date = config_data.get('start_transaction_date')
            return start_transaction_date,last_transaction_date
        
    # function to get required data from sql
    def table(table_name, start_date, end_date):
        df = spark.read.jdbc(url=url, table=table_name, properties=properties)
        if table_name == "rw_transaction_data":
            df = df.filter((df.last_modified_date >= to_date(lit(start_date))) & (df.last_modified_date <= to_date(lit(end_date))))
        return df

    def new_data(final_table , rw_transaction_data , product_category_map):
            
        '''
            function facilitates the seamless integration of new transactional data into an ongoing aggregation process,
            ensuring data consistency and integrity through careful merging and aggregation techniques before exporting 
            the final dataset for further analysis or storage
        '''
        rw_transaction_data = rw_transaction_data.withColumn("first_day_of_month", trunc(col("last_modified_date"), "month"))
        joined = rw_transaction_data.join(product_category_map, ['product_id', 'product_type_id', 'module_id'])
        table_to_join = joined.groupBy(["payer_account_id","first_day_of_month","txn_flow"]).agg(sum("amount"),count("amount"),max("last_modified_date").alias("last_modified_date"),min("last_modified_date"))
        table_to_join = table_to_join.withColumn("last_modified_date", date_format(table_to_join["last_modified_date"], "yyyy-MM-dd"))
        table_to_join = table_to_join.withColumn("first_day_of_month", date_format(table_to_join["first_day_of_month"], "yyyy-MM-dd"))
        def merge_table(row):
            existing_row = table_to_join.filter((table_to_join.payer_account_id == row.payer_account_id) & (table_to_join.first_day_of_month == row.first_day_of_month) & (table_to_join.txn_flow == row.txn_flow)).collect()
            if existing_row:
                return existing_row[0]
            else:
                return row
        final_table = final_table.unionAll(table_to_join)
        if final_table.count() == 0:
            merged_rows = table_to_join.collect()
        else:
            merged_rows = final_table.collect()
        merged_rows = [merge_table(row) for row in merged_rows]
        merged_table = spark.createDataFrame(merged_rows, final_table.schema)
        merged_table = merged_table.distinct()
        merged_table.write.csv('./input_file/final_table', header=True,mode='overwrite')
        return merged_table
    
    
    def agg_table(final_table):
        '''
        function that aggregates financial transaction data by
        account and transaction flow, computes total and average amounts and counts.
        '''
        total_amount = final_table.groupby('payer_account_id').pivot("txn_flow").agg(sum("sum(amount)").alias("Total_sum"),avg("sum(amount)").alias("Avg_sum"))
        total_count = final_table.groupby('payer_account_id').pivot("txn_flow").agg(sum("count(amount)").alias("Total_count"),avg("count(amount)").alias("Avg_count"))
        final_table = total_amount.join(total_count,['payer_account_id'])
        return final_table.write.csv('./output_file/final_table', header=True,mode='overwrite')

    start_date,last_date = get_start_last_transaction_date()
    product_category_map = table("product_category_map",start_date,last_date)
    rw_transaction_data = table("rw_transaction_data",start_date,last_date)
    file_path = "./input_file/final_table"
    if os.path.exists(file_path):
        df = spark.read.csv('./input_file/final_table', header=True, schema=schema)
        final_table = new_data(df,rw_transaction_data,product_category_map)
    else:
        final_table = new_data(Schema,rw_transaction_data,product_category_map)
    config(final_table,start_date,last_date)
    agg_table(final_table)