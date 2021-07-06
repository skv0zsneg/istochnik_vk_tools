import enum
import random

from datetime import datetime, timedelta


class TimeEnum(enum.Enum):
    EARLY_MORNING = (0, 5)
    MORNING = (6, 11)
    DAY = (12, 16)
    EVENING = (17, 20)
    NIGHT = (21, 23)

    def __init__(self, hour_from, hour_to):
        self.hour_from = hour_from
        self.hour_to = hour_to


class GetTime:
    """Класс для работы со верменем для постов."""
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

    def random_timestamp(self, day_from, dx, _time):
        """Возвращает случайное время в диапазоне от _time.
        
            :params day_from: Дата (в timestamp), с которой будут создаваться посты.
            :type day_from: int
            :params dx: Смещение от сегодня + day_from для получения очередного дня.
            :type dx: int
            :params time: Диапазон часов в который попавдает создаваемый пост.
            :type _time: TimeEnum
        """
        cur_time = datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            hour=random.randint(_time.hour_from, _time.hour_to),
            minute=random.randint(0, 59),
            second=self.second
        )
        time_dx = cur_time + timedelta(days=day_from.days + dx)

        return datetime.timestamp(time_dx)
