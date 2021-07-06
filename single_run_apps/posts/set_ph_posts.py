"""
    made by @skvozsneg
"""
import time

from datetime import datetime

from vk_api.exceptions import ApiError

from utils.utils import time_out
from utils.connection import vk, VkUpload
from utils.secret import ALBUM_ID, GROUP_ID, OWNER_ID
from utils.response.vk_wrappers import VkPhotoUploadWrapper
from utils.posts_utils.time_generator import GetTime, TimeEnum
from utils.posts_utils.photos.get_photo import get_files_from_links


def save_into_album():
    vk_upload = VkUpload(vk)
    photos = [i for i in get_files_from_links()]
    try:
        response = vk_upload.photo(
            photos=photos,
            album_id=ALBUM_ID,
            group_id=GROUP_ID
        )
        return VkPhotoUploadWrapper(response)
    except ApiError as e:
        print(f"Catch exceptions: {e}")
        time_out(10)
        print("Try again...")
        return save_into_album()


def create_post(vk_photo_links, day_from, dx, _time):
    g_time = GetTime()
    publish_date = g_time.random_timestamp(day_from, dx, _time)
    photos_attachments = ','.join(vk_photo_links)
    try:
        print(vk.wall.post(
            owner_id=OWNER_ID,
            from_group=1,
            message='#ph@istchn',
            attachments=photos_attachments,
            publish_date=publish_date
        ))
    except ApiError as e:
        print(f"Catch ApiError: {e}")
        print("publish date:" + publish_date)
        print("attachments:" + photos_attachments)


def create_ph_posts(date_from, day_count, _time):
    """Создаются посты и ставятся на таймер.

    :param date_from: Дата (в timestamp), с которой будут создаваться посты.
    :type date_from: int
    :param day_count: Количество дней, после day_from, в которые будут созданы посты.
    :type day_count: int
    :param _time: Диапазон времени, в который будут создаваться посты.
    :type _time: TimeEnum or tuple
    """
    day_from = datetime.fromtimestamp(date_from) - datetime.today()
    for i, dx in enumerate(range(day_count + 2)):  # Получившийся day_from отстает на один день.
        ph = save_into_album()

        print(f"{i}: Вк ссылки на фото в альбоме: ", end="")
        print(ph.vk_photo_links)

        create_post(ph.vk_photo_links, day_from, dx, _time)



if __name__ == "__main__":
    create_ph_posts(1629023678, 1, TimeEnum.EVENING)
