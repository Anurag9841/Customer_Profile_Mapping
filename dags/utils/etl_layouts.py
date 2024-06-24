# from pyspark.sql import SparkSession
# from pyspark.sql.functions import *
# from pyspark.sql.types import *
# from pyspark.sql.window import *
# import pymysql

# def etl_layout():
#     connection = pymysql.connect(
#             host='172.25.0.1',
#             user="wsl_root",
#             password="anurag123",
#             database='main_database'
#         )

#     spark = SparkSession.builder.appName("hadoop_add_file").getOrCreate()
#     url = "jdbc:mysql://172.25.0.1:3306/main_database"
#     properties = {
#         "user": "wsl_root",
#         "password": "anurag123",
#         "driver": "com.mysql.cj.jdbc.Driver"
#     }
#     def etl(url,table_names,properties):
#         df = spark.read.jdbc(url=url, table=table_names, properties=properties)
#         is_inc = df.select('is_incremental').collect()[0]['is_incremental']
#         for index in range(df.count()):
#             if is_inc:
#                 start_date = df.select('start_date_time').collect()[index]['start_date_time']
#                 end_date = df.select('end_date_time').collect()[index]['end_date_time']
#                 location = df.select('location').collect()[index]['location']
#                 hdfs_file_name = df.select('hdfs_file_name').collect()[index]['hdfs_file_name']
#                 inc_field = df.select('inc_field').collect()[index]['inc_field']
#                 database_name = df.select('Schema_names').collect()[index]['Schema_names']
#                 table_name = df.select('Table_names').collect()[index]['Table_names']
#                 hdfs_path = f'{location}{hdfs_file_name}'
#                 jdbc_url = f"jdbc:mysql://172.25.0.1:3306/{database_name}"
#                 query =  f"(SELECT * FROM {database_name}.{table_name} WHERE {inc_field} BETWEEN '{start_date}' AND '{end_date}') as selected_data"
#                 dataframe = spark.read.jdbc(url=jdbc_url, table=query, properties=properties)
#                 dataframe.write.mode('append').parquet(hdfs_path)
#                 with connection.cursor() as cursor:
#                     exec_date = f'update `main_database`.cf_etl_table_af set execution_date = (current_timestamp) where id = {index +1}' 
#                     cursor.execute(exec_date)
#                     start_date = f'update `main_database`.cf_etl_table_af set start_date_time = date_add(start_date_time, interval 1 day)'
#                     cursor.execute(start_date)
#                     end_date = f'update `main_database`.cf_etl_table_af set end_date_time = date_add(end_date_time, interval 1 day)'
#                     cursor.execute(end_date)
#                     connection.commit()
#     connection.close()
#     return etl(url,'cf_etl_table_af',properties)
