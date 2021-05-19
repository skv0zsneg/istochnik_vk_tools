import random

from datetime import datetime, timedelta


class GetTime:
    """
        Возвращает время в timestamp.
    """
    def __init__(
            self,
            year=None,
            month=None,
            day=None,
            hour=None,
            minute=None,
            second=None
    ):
        self.today = datetime.today()

        self.year = year if year is not None else self.today.year
        self.month = month if month is not None else self.today.month
        self.day = day if day is not None else self.today.day
        self.hour = hour if hour is not None else self.today.hour
        self.minute = minute if minute is not None else self.today.minute
        self.second = second if second is not None else self.today.second

        self.today_timestamp = datetime.timestamp(self.today)

    def random_am_timestamp(self, days):
        """
            Возвращает случайное время в первой половине дня.

            :params: days - шаг для дня от сегодня.
        """
        time = datetime(self.year, self.month, self.day, random.randint(7, 12), random.randint(0, 59), self.second)
        time_dx = time + timedelta(days=days)
        return datetime.timestamp(time_dx)


if __name__ == "__main__":
    s = GetTime()
    print(s.random_am_timestamp())
