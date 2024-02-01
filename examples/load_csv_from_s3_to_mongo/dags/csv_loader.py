from airflow import DAG
from airflow.utils.dates import days_ago
from airgoodies.command.parser import CommandParser
from airflow.operators.python import PythonOperator

"""
DAG that demonstrates the usage of YAML to dynamically configure a simple DAG
which loads a .csv file from the configured S3 Bucket, removes every line that
is not related to Athens and then saves it in the configured MongoDB table.

@author: Stavros Grigoriou <unix121@protonmail.com>
@since 0.0.4
"""

with DAG(
        dag_id='csv_loader',
        schedule_interval=None,
        start_date=days_ago(2),
        default_args={
            'owner': 'airflow'
        },
        catchup=False,
        tags=['csv_loader', 'aws', 'mongo', 'airgoodies:examples'],
) as dag:
    import logging

    logger: logging.getLogger = logging.getLogger('airflow.task')

    command_parser: CommandParser = CommandParser(dag=dag)

    tasks: [PythonOperator] = []

    for _task in command_parser.get_commands():
        tasks = tasks >> _task.to_operator(dag=dag)

    tasks
