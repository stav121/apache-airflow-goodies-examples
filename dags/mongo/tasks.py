def task1(ti, **kwargs) -> None:
    """
    Task that checks if a connection exists for Mongo using the goodies.

    :param ti: the task instance
    :param kwargs: provided arguments
    """

    from airgoodies.mongo.connection import MongoConnection

    conn = MongoConnection()
