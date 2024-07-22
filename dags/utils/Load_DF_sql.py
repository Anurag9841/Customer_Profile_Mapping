import pandas as pd
import numpy as np
import os
import pandas as pd
from sqlalchemy import create_engine,inspect

def sanitize(df):
    return df.applymap(
        lambda x: x.replace(',', '').replace(' ', '').strip() if isinstance(x, str) else '' if pd.isna(x) else x)


def load_df_from_dir():
    DATABASE_URL = "mysql+pymysql://wsl_root:anurag123@172.25.0.1:3306/entity_matching"
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    layouts = []

    for table in tables:
        query = f"SELECT * FROM {table}"
        # Pass the engine directly to read_sql_query
        df = pd.read_sql_query(query, engine)
        df['source'] = table
        layouts.append(df)
    
    return layouts

def char_to_digit(char):
    if char.isdigit():
        return int(char)
    elif char.isalpha():
        return (ord(char.lower()) - ord('a') + 1) % 10
    else:
        return 0


def string_to_digits(s):
    digits = [char_to_digit(char) for char in s]
    numeric_string = ''.join(map(str, digits))

    if len(numeric_string) > 13:
        return numeric_string[:13]
    else:
        return numeric_string.ljust(13, '0')

print("Sucess ...")
print(load_df_from_dir())