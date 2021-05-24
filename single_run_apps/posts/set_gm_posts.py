"""
    made by @skvozsneg
"""
import requests

from vk_api.exceptions import ApiError

from utils.connection import vk, VkUpload
from utils.posts_utils.time_generator import GetTime
from utils.response.vk_wrappers import VkPhotoUploadWrapper
from utils.posts_utils.photos.get_photo import get_files_from_links

ALBUM_ID = 228592736
GROUP_ID = 115546115
OWNER_ID = -115546115


def save_into_album():
    vk_upload = VkUpload(vk)
    photos = [i for i in get_files_from_links()]

    response = vk_upload.photo(
        photos=photos,
        album_id=ALBUM_ID,
        group_id=GROUP_ID
    )

    return VkPhotoUploadWrapper(response)


def create_post(vk_photo_links, day_from, dx):
    time = GetTime()
    publish_date = time.random_am_timestamp(day_from=day_from, dx=dx)
    photos_attachments = ','.join(vk_photo_links)
    try:
        print(vk.wall.post(
            owner_id=OWNER_ID,
            from_group=1,
            message='#music@sourcem',
            attachments=photos_attachments,
            publish_date=publish_date
        ))
    except ApiError:
        print("Catch ApiError")
        print("publish date:" + publish_date)
        print("attachments:" + photos_attachments)


def set_gm_post(day_from: int, day_count: int):
    """Создаются посты и ставятся на таймер в первой половине дня.

    :param day_from: Смешение от сегодня для определения дня, с которого будут создаваться посты.
    :param day_count: Количество дней, в которые будут созданы посты.
    """
    for dx in range(day_count + 1):
        ph = save_into_album()
        print("Вк ссылки на фото в альбоме: ", end="")
        print(ph.vk_photo_links)
        create_post(ph.vk_photo_links, day_from, dx)


if __name__ == "__main__":
    set_gm_post(8, 5)
