from airflow import DAG
from airflow.utils.dates import days_ago
from common.task_builder import build_task
from xcom.tasks import task1, task2, task3, task4

"""
Example DAG that demonstrates the usage of airgoodies.xcom.XComManager

@author: Stavros Grigoriou <unix121@protonmail.com>
"""

with DAG(
        dag_id='xcom_manager_example',
        schedule_interval=None,
        start_date=days_ago(2),
        default_args={
            'owner': 'airflow'
        },
        catchup=False,
        tags=['xcom_manager', 'airgoodies:v0.0.2'],
) as dag:
    import logging

    logger: logging.getLogger = logging.getLogger('airflow.task')

    t1 = build_task(dag=dag, callable=task1, name='xcom_t1')
    t2 = build_task(dag=dag, callable=task2, name='xcom_t2')
    t3 = build_task(dag=dag, callable=task3, name='xcom_t3')
    t4 = build_task(dag=dag, callable=task4, name='xcom_t4')
    t1 >> t2 >> t3 >> t4
