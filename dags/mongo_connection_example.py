from airflow import DAG
from airflow.utils.dates import days_ago
from common.task_builder import build_task
from mongo.tasks import task1

"""
Example DAG that demonstrates the usage of airgoodies.mongo.MongoConnection

@author: Stavros Grigoriou <unix121@protonmail.com>
"""

with DAG(
        dag_id='mongo_connection_example',
        schedule_interval=None,
        start_date=days_ago(2),
        default_args={
            'owner': 'airflow'
        },
        catchup=False,
        tags=['mongo_connection', 'airgoodies:v0.0.2'],
) as dag:
    import logging

    logger: logging.getLogger = logging.getLogger('airflow.task')

    t1 = build_task(dag=dag, callable=task1, name='mongo_t1')

    t1
