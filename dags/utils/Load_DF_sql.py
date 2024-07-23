'''
Author: Anurag Karki
Date: 2024/07/21
'''
import pandas as pd
import numpy as np
import os
import pandas as pd
from sqlalchemy import create_engine,inspect
from dotenv import load_dotenv

load_dotenv()

SQL_USERNAME = os.getenv('SQL_USERNAME')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')
SQL_HOST = os.getenv('SQL_HOST')
SQL_PORT = os.getenv('SQL_PORT')
ROOT_PATH = os.getenv('ROOT_PATH')
DATABASE_NAME = os.getenv('DATABASE_NAME')

def sanitize(df):
    '''
    Sanitize the data loaded from the SQL database.
    
    This function removes commas and spaces from string values and strips any leading or trailing whitespace.
    For non-string values, it replaces NaNs with empty strings.
    
    :param df: The dataframe to sanitize
    :return: The sanitized dataframe
    '''
    return df.applymap(
        lambda x: x.replace(',', '').replace(' ', '').strip() if isinstance(x, str) else '' if pd.isna(x) else x
    )

def load_df_from_dir():
    '''
    Load data from an SQL database into a list of dataframes.
    
    This function connects to the MySQL database using SQLAlchemy, retrieves all tables, 
    executes a SELECT query on each table, and loads the data into pandas dataframes. 
    Each dataframe is tagged with its source table name.
    
    :return: A list of dataframes, each representing a table from the database
    '''
    DATABASE_URL = f'mysql+pymysql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{DATABASE_NAME}'
    engine = create_engine(DATABASE_URL)  # Create a SQLAlchemy engine
    inspector = inspect(engine)  # Inspect the database schema
    tables = inspector.get_table_names()  # Get a list of table names
    layouts = []

    for table in tables:
        query = f"SELECT * FROM {table}"  # Construct a SQL query to select all data from the table
        # Pass the engine directly to read_sql_query to fetch data into a dataframe
        df = pd.read_sql_query(query, engine)
        df['source'] = table  # Add a column to identify the source table
        layouts.append(df)  # Append the dataframe to the list
    
    return layouts

def char_to_digit(char):
    '''
    Convert a character to a digit for creating unique IDs.
    
    This function converts alphabetical characters to digits (1-9) and keeps digits unchanged. 
    Characters not in these ranges are converted to 0.
    
    :param char: The character to convert
    :return: The corresponding digit
    '''
    if char.isdigit():
        return int(char)  # Return the digit as is
    elif char.isalpha():
        # Convert alphabetical characters to digits (1-9)
        return (ord(char.lower()) - ord('a') + 1) % 10
    else:
        return 0  # Convert any other character to 0

def string_to_digits(s):
    '''
    Convert a string to a numeric string representation.
    
    This function maps each character in the string to a digit, concatenates them, and ensures 
    the result is 13 characters long by truncating or padding with zeros.
    
    :param s: The string to convert
    :return: A numeric string of length 13
    '''
    digits = [char_to_digit(char) for char in s]  # Convert each character to a digit
    numeric_string = ''.join(map(str, digits))  # Join digits into a single string

    if len(numeric_string) > 13:
        return numeric_string[:13]  # Truncate to 13 characters if too long
    else:
        return numeric_string.ljust(13, '0')  # Pad with zeros to ensure 13 characters

# Test print statements to check if the functions are working correctly
print("Success ...")
print(load_df_from_dir())
