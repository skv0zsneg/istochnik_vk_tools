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

    def get_random_photo(self, n=2):
        """GET /photo/random
        docs: https://unsplash.com/documentation#get-a-random-photo

        :param n: Количество фотографий.
        :type n: int
        """
        collections = {'earth-is-awsome': 220381, 'winter': 3178572, 'pyro': 1254524, 'landscape': 827743,
                       'animals': 1424240, 'patel-pantone': 1074434, 'space': 1111575, 'great-outdoors': 289662,
                       'street-life-photowalk': 1911873, 'texture-colors': 1136512, 'mastering-monochrome-': 400620,
                       "it's-simple-but-very-complex": 1240111, 'beautiful-blur': 162232, 'foggy-days': 910773,
                       'mysterious-landscapes': 397119, 'shadow-and-light': 612689}

        collections_ids_list = [i for i in collections.values()]
        random_params = {
            'collections': collections_ids_list[random.randint(0, len(collections_ids_list) - 1)],
            'count': str(n)
        }
        random_params.update(self.params)

        response = requests.get(self.url + '/photos/random', params=random_params)

        return PhotoResponseWrapper(response)


def get_files_from_links():
    """Скачивание фотграфий.
    Генератор. С каждой итерацией возвращает следующий локальный путь до фотографий.

    :return: Локальный путь до фотографий.
    :rtype: str
    """
    ph = GetPhoto()
    random_photo = ph.get_random_photo()
    download_links = random_photo.photos['download_links']

    for i in range(len(download_links)):
        response = requests.get(download_links[i])
        file_name = f'temp-{i}.jpg'
        with open(file_name, 'wb') as wb:
            wb.write(response.content)
            file_name = f"{os.path.join(os.path.abspath('.'), file_name)}"
            yield file_name
