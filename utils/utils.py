import time


def time_out(seconds=10):
    """Таймаут на `seconds` секунд.
    Выводит соответсвующие сообщения в консоль.

    :param seconds: Время таймаута в секундах (по умолчанию 10 секунд).
    :type seconds: int
    """
    print(f"Timeout for {seconds} seconds", end='')
    for _ in range(seconds):
        time.sleep(1)
        print('.', end='')
    print()
