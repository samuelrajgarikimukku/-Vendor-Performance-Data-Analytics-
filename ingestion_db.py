import pandas as pd 
import os
from sqlalchemy import create_engine

import logging
import time 

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
# Connect to your inventory_management database
engine = create_engine("postgresql://postgres:0101@localhost:5432/inventory_management")

def ingest_db(df, table_name, engine, chunksize=50000):
    '''ingests a dataframe into a specified table in the database in chunks'''
    df.to_sql(
        table_name,
        con=engine,
        if_exists='replace',
        index=False,
        chunksize=chunksize,
        method="multi"
    )


def load_raw_data():
    start = time.time()
    for file in os.listdir(r""):
        if file.endswith(".csv"):
            try:
                df = pd.read_csv(rf"data\{file}")
                logging.info(f'Ingesting {file} into db')
                ingest_db(df, file[:-4], engine=engine)
                logging.info(f'Successfully ingested {file}')
            except Exception as e:
                logging.error(f'❌ Failed to ingest {file}: {e}')
    end = time.time()
    total_time = (end - start)/60
    logging.info('----------Ingestion completed----------')
    logging.info(f'Total time for ingestion: {total_time:.2f} minutes')


if __name__ == "__main__":
    load_raw_data()
