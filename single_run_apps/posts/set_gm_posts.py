"""
    made by @skvozsneg
"""
import requests

from utils.connection import vk, VkUpload
from utils.posts_utils.photos.get_photo import GetPhoto, get_files_from_links

ALBUM_ID = 228592736
GROUP_ID = 115546115
OWNER_ID = -115546115


def save_into_album():
    vk_upload = VkUpload(vk)
    photos = [i for i in get_files_from_links()]

    print(vk_upload.photo(
        photos=photos,
        album_id=ALBUM_ID,
        group_id=GROUP_ID
    ))

    return photos


def create_post(photos):
    photos_to_post = []
    # TODO: вытащить ссылки для photos_to_posts
    for size in photos[0]['sizes']:
        photos_to_post.append(size['url'])
    print(vk.wall.post(
        owner_id=OWNER_ID,
        from_group=1,
        message='God bless you!',
        attachments=photos_to_post,
        publish_date=1639598111)
    )


if __name__ == "__main__":
    create_post(save_into_album())
