'''
Author: Anurag Karki
Date: 2024/07/22
'''

import pandas as pd
from sqlalchemy import create_engine,inspect
import os
from dotenv import load_dotenv

load_dotenv()

SQL_USERNAME = os.getenv('SQL_USERNAME')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')
SQL_HOST = os.getenv('SQL_HOST')
SQL_PORT = os.getenv('SQL_PORT')
ROOT_PATH = os.getenv('ROOT_PATH')
DATABASE_NAME = os.getenv('DATABASE_NAME')

def load_df_from_sql():
    def load_df_from_dir(dir_path=f'{ROOT_PATH}/input_file/input_files_entity_matching'):
        engine = create_engine(f'mysql+pymysql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{DATABASE_NAME}')
        csv_files = [f for f in os.listdir(dir_path) if f.endswith(".csv")]
        for csv_file in csv_files:
            name = csv_file.split('.')[0]
            file_path = os.path.join(dir_path, csv_file)
            df = pd.read_csv(file_path)
            df.to_sql(name=name, con=engine, if_exists='replace',index = False)
        return "sucess to load data..."

    return load_df_from_dir()