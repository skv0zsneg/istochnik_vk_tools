import json


class NotOkException(Exception):
    pass


class PhotoResponseWrapper:
    def __init__(self, raw_response):
        self.code = raw_response.status_code
        if self.code == 200:
            self.body = json.loads(raw_response.text)
            self.photos = {'download_links': [], 'descriptions': []}
            if isinstance(self.body, list):  # если несколько фото
                for ph in self.body:
                    self.photos['descriptions'].append(ph['description'])
                    self.photos['download_links'].append(ph['urls']['full'])
            else:
                self.photos['descriptions'].append(self.body['description'])
                self.photos['download_links'].append(self.body['urls']['full'])
        else:
            raise NotOkException(f"Не могу получить фото. HTML статус-код {self.code}")
