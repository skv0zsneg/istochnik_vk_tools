"""
    made by @skvozsneg
"""
import requests

from utils.connection import vk, VkUpload
from utils.posts_utils.photos.get_photo import GetPhoto

ALBUM_ID = 279240419
GROUP_ID = 115546115
OWNER_ID = -115546115


def save_into_album():
    vk_upload = VkUpload(vk)
    ph = GetPhoto()
    photo = ph.get_random_photo()

    print(vk_upload.photo(
        # TODO: Нужен file like объект, а подается просто ссылка.
        photos=photo.photos['download_links'],
        album_id=ALBUM_ID,
        group_id=GROUP_ID
    ))
    # for link in photos['downloads_links']:
    #     url = vk.photos.getUploadServer(
    #         album_id=ALBUM_ID,
    #         group_id=GROUP_ID
    #     )
    #     response = requests.post(url['upload_url'], files=)
    return response


def create_post():
    print(vk.wall.post(
        owner_id=OWNER_ID,
        from_group=1,
        message='God bless you!',
        attachments='...',
        publish_date=1621284782)
    )


if __name__ == "__main__":
    response = save_into_album()
    # create_post()
