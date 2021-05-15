"""
    made by @skvozsneg
"""
import requests

from utils.connection import vk, VkUpload
from utils.response.vk_wrappers import VkPhotoUploadWrapper
from utils.posts_utils.photos.get_photo import GetPhoto, get_files_from_links

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


def create_post(photos: VkPhotoUploadWrapper):
    print(vk.wall.post(
        owner_id=OWNER_ID,
        from_group=1,
        message='#music@sourcem',
        attachments=','.join(photos.vk_photo_links),
        publish_date=1639770911)
    )


if __name__ == "__main__":
    create_post(save_into_album())
