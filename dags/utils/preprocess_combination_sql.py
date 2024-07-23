'''
Author: Anurag Karki
Date: 2024/07/22
'''
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,inspect
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
from utils.Load_DF_sql import load_df_from_dir,sanitize,string_to_digits,char_to_digit
from Levenshtein import distance
from dotenv import load_dotenv

load_dotenv()

SQL_USERNAME = os.getenv('SQL_USERNAME')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')
SQL_HOST = os.getenv('SQL_HOST')
SQL_PORT = os.getenv('SQL_PORT')
ROOT_PATH = os.getenv('ROOT_PATH')
DATABASE_NAME = os.getenv('DATABASE_NAME')

def final_entity_matching():

    layouts = load_df_from_dir()
    engine = create_engine(f'mysql+pymysql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{DATABASE_NAME}')
    for layout in layouts:
        layout['last_modified_date'] = datetime.now()

    def create_soup(df, df_, soup, soup_name):
        """
        Concatenate specified columns into a single 'soup' column with lowercase text.
        
        :param df: Original dataframe to update
        :param df_: Dataframe with raw data
        :param soup: List of columns to concatenate
        :param soup_name: Name of the new 'soup' column
        """
        df[soup_name] = df_[soup].apply(lambda x: ' '.join(x.values.astype(str)).lower(), axis=1)

    layout_copies = [layout.copy() for layout in layouts]
    soup = ['Name', 'Date of Birth', 'Father_Name']

    for layout, layout_copy, in zip(layouts, layout_copies):
        layout_copy = sanitize(layout_copy)
        create_soup(layout, layout_copy, soup, "soup")

    def combine_layouts(A, B, metric='cosine', threshold=0.8):
        """
        Combine two dataframes based on similarity metrics.
        
        :param A: First dataframe
        :param B: Second dataframe
        :param metric: Similarity metric ('cosine' or others)
        :param threshold: Similarity threshold for merging
        :return: Combined dataframe
        """
        def calculate_similarity(A, B, metric):
            if metric == 'cosine':
                tfidf = TfidfVectorizer(stop_words='english')
                combined_soup = pd.concat([A['soup'], B['soup']], ignore_index=True)
                tfidf.fit(combined_soup)
                tfidf_matrix_A = tfidf.transform(A['soup'])
                tfidf_matrix_B = tfidf.transform(B['soup'])
                similarity = cosine_similarity(tfidf_matrix_A, tfidf_matrix_B)
                similarity_df = pd.DataFrame(similarity, index=A.index, columns=B.index)
                idx_row = similarity_df.idxmax(axis=1)
                similarity_mask = similarity_df.max(axis=1) > threshold
            else:
                distance_matrix = pd.DataFrame([[distance(a, b) for b in B['soup']] for a in A['soup']], index=A.index,
                                               columns=B.index)
                idx_row = distance_matrix.idxmin(axis=1)
                similarity_mask = distance_matrix.min(axis=1) <= threshold
            return idx_row, similarity_mask

        def merge_data(A, B, idx_row, similarity_mask):
            combined_columns = list(set(A.columns) | set(B.columns))
            combined_data = pd.DataFrame(columns=combined_columns)
            for idx_A in A.index:
                if similarity_mask[idx_A]:
                    idx_B = idx_row[idx_A]
                    combined_row = A.loc[idx_A].combine_first(B.loc[idx_B])
                    combined_row['source'] = f"{A.loc[idx_A]['source']}, {B.loc[idx_B]['source']}"
                    combined_row['last_modified_date'] = datetime.now()
                else:
                    combined_row = A.loc[idx_A]
                combined_data = pd.concat([combined_data, combined_row.to_frame().T], ignore_index=True)
            new_records = B.loc[~B.index.isin(idx_row[similarity_mask].values)]
            return pd.concat([combined_data, new_records], ignore_index=True)

        idx_row, similarity_mask = calculate_similarity(A, B, metric)
        return merge_data(A, B, idx_row, similarity_mask)

    def save_layouts():
        """
        Combine all layouts and save the final result to a database.
        
        :return: SQL result of saving the final dataframe
        """
        final_df = layouts[0]

        for df in layouts[1:]:
            final_df = combine_layouts(final_df, df)

        final_df['uuid'] = final_df['soup'].apply(string_to_digits)
        
        return final_df.to_sql(name="entity_matching_output", con=engine, if_exists='replace',index = False)
    return save_layouts()
