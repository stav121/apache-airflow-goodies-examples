def task1(ti, **kwargs) -> None:
    """
    Task that creates 3 variable and saves them in XCom

    :param ti: the task instance
    :param kwargs: provided arguments
    """

    import logging
    from airgoodies.xcom.manager import XComManager

    logger: logging.Logger = logging.getLogger('airflow.task')

    man = XComManager(ti=ti)

    logger.info('Inserting {`test1`: `val1`, `test2`: `val2`, `dict`:{`some`: `value`}}')
    man.set_variable(name='test1', value='val1')
    man.set_variable(name='test2', value='val2')
    man.set_variable(name='dict', value={'some': 'value'})


def task2(ti, **kwargs) -> None:
    """
    Task that updates variables using the XComManager

    :param ti: the task instance
    :param kwargs: provided arguments
    """

    import logging
    from airgoodies.xcom.manager import XComManager

    logger: logging.Logger = logging.getLogger('airflow.task')

    man = XComManager(ti=ti)

    logger.info("Updating `test1` and `test3`")
    man.set_variable(name='test1', value='val3')
    man.set_variable(name='test3', value='val3')

    val = man.get_variable(name='test2')
    logger.info(f'Pulled `test2`: {val}')
    dic = man.get_variable(name='dict')
    logger.info(f'Pulled `dict`: {dic}')


def task3(ti, **kwargs) -> None:
    """
    Task that updates variables using the XComManager

    :param ti: the task instance
    :param kwargs: provided arguments
    """

    import logging
    from airgoodies.xcom.manager import XComManager

    logger: logging.Logger = logging.getLogger('airflow.task')
    man = XComManager(ti=ti)
    man.set_variable(name='test4', value='val4')
    val = man.get_variable(name='test2')
    logger.info(f'Pulled `test2`: {val}')
    # Remove a variable
    logger.info(f'Removing `dict`')
    man.remove_variable(name='dict')


def task4(ti, **kwargs) -> None:
    """
    Task that updates the values of the task in XCom and clears them in the end.

    :param ti: the task instance
    :param kwargs: provided arguments
    """

    import logging
    from airgoodies.xcom.manager import XComManager

    logger = logging.getLogger('airflow.task')
    man = XComManager(ti=ti)
    man.set_variable(name='test4', value='val4')
    val = man.get_variable(name='test2')
    logger.info(f'Pulled `test2`: {val}')

    logger.info('Clearing XCom for task')
    # Clear all variables
    man.clear_variables()
