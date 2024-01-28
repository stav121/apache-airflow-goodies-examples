from airflow import DAG
from airflow.utils.dates import days_ago
from common.task_builder import build_task
from aws.s3.tasks import task1, task2, task3, task4

"""
DAG that contains an example of usage for airgoodies.aws.s3 goodies.

@author: Stavros Grigoriou <unix121@protonmail.com>
@since 0.0.3
"""

with DAG(
        dag_id='aws_s3_wrapper_example',
        schedule_interval=None,
        start_date=days_ago(2),
        default_args={
            'owner': 'airflow'
        },
        catchup=False,
        tags=['aws_s3_wrapper', 'airgoodies:v0.0.3'],
) as dag:
    import logging

    logger: logging.getLogger = logging.getLogger('airflow.task')

    t1 = build_task(dag=dag, callable=task1, name='aws_s3_t1')
    t2 = build_task(dag=dag, callable=task2, name='aws_s3_t2')
    t3 = build_task(dag=dag, callable=task3, name='aws_s3_t3')
    t4 = build_task(dag=dag, callable=task4, name='aws_s3_t4')

    t1 >> t2 >> t3 >> t4
