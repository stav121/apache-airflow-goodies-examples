from airflow.models import Variable


def task1(ti, **kwargs) -> None:
    """
    Task that loads a file from the configured S3 bucket

    :param ti: the task instance
    :param kwargs: provided arguments
    """

    from airgoodies.aws.s3.wrapper import S3Wrapper

    wrapper: S3Wrapper = S3Wrapper()
    wrapper.load_file(key=Variable.get(key='aws-s3-example-csv'))


def task2(ti, **kwargs) -> None:
    """
    Task that loads a file from the configured S3 bucket into a pandas DataFrame.
    """
    import pandas as pd
    import logging
    from airgoodies.aws.s3.wrapper import S3Wrapper

    logger: logging.Logger = logging.getLogger('airflow.task')

    wrapper: S3Wrapper = S3Wrapper()
    df: pd.Dataframe = wrapper.load_as_dataframe(key=Variable.get(key='aws-s3-example-csv'))

    logger.info(df)


def task3(ti, **kwargs) -> None:
    """
    Task that loads a file from the configured S3 bucket into a pandas DataFrame
    and applies a simple transformation lambda.
    """
    import logging
    from airgoodies.aws.s3.wrapper import S3Wrapper
    import pandas as pd
    from typing import Callable

    logger: logging.Logger = logging.getLogger('airflow.task')

    wrapper: S3Wrapper = S3Wrapper()
    l: Callable[[pd.DataFrame], pd.DataFrame] = lambda i: logger.info(f'Loaded {i}')
    df: pd.DataFrame = wrapper.load_and_transform(key=Variable.get(key='aws-s3-example-csv'), transform_method=l)


def task4(ti, **kwargs) -> None:
    """
    Task that loads a file from the configured S3 bucket into the provided
    table of the given pre-configured MongoDB Connection.
    """
    import logging
    from airgoodies.aws.s3.wrapper import S3Wrapper
    from airgoodies.mongo.connection import MongoConnection
    import pandas as pd
    from typing import Callable

    logger: logging.Logger = logging.getLogger('airflow.task')

    wrapper: S3Wrapper = S3Wrapper()
    mongo: MongoConnection = MongoConnection()
    l: Callable[[pd.DataFrame], pd.DataFrame] = lambda i: logger.info(f'Loaded {i}')
    wrapper.load_to_mongo(key=Variable.get(key='aws-s3-example-csv'),
                          connection=mongo,
                          load_table_name=Variable.get(key='aws-s3-example-csv'),
                          sep=';')
