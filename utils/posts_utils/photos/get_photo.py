"""
    made by @skvozsneg
"""
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
            'count': str(random.randint(1, 5))
        }

        random_params.update(self.params)
        response = requests.get(self.url + '/photos/random', params=random_params)
        return PhotoResponseWrapper(response)


def main():
    ph = GetPhoto()
    random_photo = ph.get_random_photo()
    print(random_photo.photos)


if __name__ == "__main__":
    main()
