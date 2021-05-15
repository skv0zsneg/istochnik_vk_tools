"""
    made by @skvozsneg
"""
import os
import random
import requests

from utils.secret import unsplash_access_key
from utils.response.photo_wrappers import PhotoResponseWrapper


class GetPhoto:
    """
        Работаем с фото по unsplash api (https://unsplash.com/oauth/applications/230526)
    """
    def __init__(self):
        self.url = 'https://api.unsplash.com'
        self.params = {'client_id': unsplash_access_key}

    def get_random_photo(self):
        """
            GET /photo/random

            docs: https://unsplash.com/documentation#get-a-random-photo
        """
        collections_name = ['film', 'architecture', 'interiors', 'street-photography', 'travel', 'textures-patterns', 'Motion_blur']
        random_params = {
            'query': collections_name[random.randint(0, len(collections_name) - 1)],
            'count': '5'
        }

        random_params.update(self.params)
        response = requests.get(self.url + '/photos/random', params=random_params)
        return PhotoResponseWrapper(response)


def get_files_from_links():
    """
        Возвращает путь до фото.
    """
    ph = GetPhoto()
    random_photo = ph.get_random_photo()
    for i in range(len(random_photo.photos['download_links'])):
        response = requests.get(random_photo.photos['download_links'][i])
        file_name = f'temp-{i}.jpg'
        with open(file_name, 'wb') as wb:
            wb.write(response.content)
            yield f"{os.path.join(os.path.abspath('.'), file_name)}"


def main():
    ph = GetPhoto()
    random_photo = ph.get_random_photo()
    for i in range(len(random_photo.photos['download_links'])):
        response = requests.get(random_photo.photos['download_links'][0])
        print(response)
        with open('temp.jpg', 'wb') as wb:
            wb.write(response.content)
    # get_files_from_links()


if __name__ == "__main__":
     main()
