from airflow import DAG
from airflow.operators.python import PythonOperator, Callable


def build_task(dag: DAG, callable: Callable, name: str) -> PythonOperator:
    """
    Build a task with the provided callable and name.

    :param dag: the DAG instance
    :param callable: the python callable
    :param name: the name to use
    :return: the build operator
    """
    return PythonOperator(
        task_id=name,
        python_callable=callable,
        provide_context=True,
        dag=dag
    )
