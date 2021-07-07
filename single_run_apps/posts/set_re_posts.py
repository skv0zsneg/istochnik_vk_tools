"""
    made by @skvozsneg
"""
from datetime import datetime

from utils.posts_utils.time_generator import GetTime, TimeEnum
from utils.posts_utils.reposts.get_reposts import GettingReposts


def set_re_posts(date_from, day_count, _time):
    """Берется запись с другого паблика и делатся репост.

    :param date_from: Дата (в timestamp), с которой будут создаваться посты.
    :type date_from: int
    :param day_count: Количество дней, после day_from, в которые будут созданы посты.
    :type day_count: int
    :param _time: Диапазон времени, в который будут создаваться посты.
    :type _time: TimeEnum or tuple
    """
    day_from = datetime.fromtimestamp(date_from) - datetime.today()
    for i, dx in enumerate(range(day_count + 2)):  # Получившийся day_from отстает на один день.
        gp = GettingReposts

        print(f"{i + 1}: Вк ссылки на фото в альбоме: ", end="")
        print(ph.vk_photo_links)

        create_post(ph.vk_photo_links, day_from, dx, _time)
