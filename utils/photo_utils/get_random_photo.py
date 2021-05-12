"""
    made by @skvozsneg
"""
import requests

from utils.secret import unsplash_access_key
from utils.response.photo_wrapper import PhotoResponseWrapper


class GetPhoto:
    """
        Работаем с фото по unsplash api (https://unsplash.com/oauth/applications/230526)
    """
    def __init__(self):
        self.url = 'https://api.unsplash.com'
        self.params = {'client_id': unsplash_access_key}

    def get_random_photo(self):
        ...







def main():
    random_response = requests.get(url + random + token)
    print(response.text)


if __name__ == "__main__":
    main()
