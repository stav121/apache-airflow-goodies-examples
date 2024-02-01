import pandas as pd
import logging

"""
@author: Stavros Grigoriou <unix121@protonmail.com>
"""


def keep_athens(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function that loads the pandas DataFrame and removes the lines that are not
    related to Athens.
    """
    logger: logging.Logger = logging.Logger('airflow.task')
    logger.info('Running custom transform method: keep_athens')

    # Remove each line not related to 'Athens'
    data.drop(data[data['city'] != 'Athens'].index, inplace=True)

    logger.info(f'New data:\n{data}')
    return data  # Return the DataFrame to write it in MongoDB
