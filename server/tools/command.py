# async def lcr_name() -> str:
#     """Запрос имени прибора

#     Returns:
#         str: Команда с запросом имени прибора
#     """

#     command: str = "0xAA, 64"
#     return command


# async def avp_start() -> str:
#     """Установка режима автоматического выбора предела измерений

#     Returns:
#         str: Команда с запросом установки АВП
#     """

#     command: str = "0xAA, 65"
#     return command


# async def avp_stop() -> str:
#     """Остановка режима автоматического выбора предела измерений

#     Returns:
#         str: Команда с запросом остановки АВП
#     """

#     command: str = "0xAA, 66"
#     return command


# async def set_frequency(freq: float) -> str:
#     """Установка частоты
#     Передается число из 4 байтов

#     Returns:
#         str: Команда с запросом установки частоты
#     """

#     # Разбить частоту на 4 байта
#     f4, f3, f2, f1 = ""
#     command: str = f"0xAA, 67, {f4}, {f3}, {f2}, {f1}"
#     return command


# async def set_shift(shift: float) -> str:
#     """Установка смещения
#     Передается число из 2 байтов

#     Returns:
#         str: Команда с запросом установки смещения
#     """

#     # Разбить смещение на 2 байта
#     u2, u1 = ""
#     command: str = f"0xAA, 70, {u2}, {u1}"
#     return command


# async def reset() -> str:
#     """Cброс в состояние по умолчанию

#     Returns:
#         str: Команда с запросом сброса в состояние по умолчанию
#     """

#     command: str = "0xAA, 71"
#     return command


# async def get_info() -> str:
#     """Выдача полной измеряемой информации

#     Returns:
#         str: Команда с запросом выдачи полной измеряемой информации
#     """


#     command: str = "0xAA, 72, 0"
#     return command
def lcr_name() -> str:
    """Запрос имени прибора

    Returns:
        str: Команда с запросом имени прибора
    """

    command: str = "0xAA, 64"
    return command


def avp_start() -> str:
    """Установка режима автоматического выбора предела измерений

    Returns:
        str: Команда с запросом установки АВП
    """

    command: str = "0xAA, 65"
    return command


def avp_stop() -> str:
    """Остановка режима автоматического выбора предела измерений

    Returns:
        str: Команда с запросом остановки АВП
    """

    command: str = "0xAA, 66"
    return command


def set_frequency(freq: float) -> str:
    """Установка частоты
    Передается число из 4 байтов

    Returns:
        str: Команда с запросом установки частоты
    """

    # Разбить частоту на 4 байта
    f4, f3, f2, f1 = ""
    command: str = f"0xAA, 67, {f4}, {f3}, {f2}, {f1}"
    return command


def set_shift(shift: float) -> str:
    """Установка смещения
    Передается число из 2 байтов

    Returns:
        str: Команда с запросом установки смещения
    """

    # Разбить смещение на 2 байта
    u2, u1 = ""
    command: str = f"0xAA, 70, {u2}, {u1}"
    return command


def reset() -> str:
    """Cброс в состояние по умолчанию

    Returns:
        str: Команда с запросом сброса в состояние по умолчанию
    """

    command: str = "0xAA, 71"
    return command


def get_info() -> str:
    """Выдача полной измеряемой информации

    Returns:
        str: Команда с запросом выдачи полной измеряемой информации
    """

    command: str = "0xAA, 72, 0"
    return command
