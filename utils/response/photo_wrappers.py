"""
{
   "id":"ECteVg5suUg",
   "created_at":"2021-04-22T13:54:31-04:00",
   "updated_at":"2021-05-14T12:49:24-04:00",
   "promoted_at":"2021-04-23T03:15:02-04:00",
   "width":2220,
   "height":2254,
   "color":"#0ca6c0",
   "blur_hash":"LbCuVSpy9ZIA-;r=OYNbO@ibrqtS",
   "description":"𝑻𝒂𝒌𝒆 𝒎𝒆 𝒅𝒐𝒘𝒏 𝒕𝒉𝒆𝒓𝒆 🏝 ",
   "alt_description":"aerial view of green trees on seashore during daytime",
   "urls":{
      "raw":"https://images.unsplash.com/photo-1619114057582-2033419f4f7e?ixid=MnwyMzA1MjZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjEwMjYyNTc\u0026ixlib=rb-1.2.1",
      "full":"https://images.unsplash.com/photo-1619114057582-2033419f4f7e?crop=entropy\u0026cs=srgb\u0026fm=jpg\u0026ixid=MnwyMzA1MjZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjEwMjYyNTc\u0026ixlib=rb-1.2.1\u0026q=85",
      "regular":"https://images.unsplash.com/photo-1619114057582-2033419f4f7e?crop=entropy\u0026cs=tinysrgb\u0026fit=max\u0026fm=jpg\u0026ixid=MnwyMzA1MjZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjEwMjYyNTc\u0026ixlib=rb-1.2.1\u0026q=80\u0026w=1080",
      "small":"https://images.unsplash.com/photo-1619114057582-2033419f4f7e?crop=entropy\u0026cs=tinysrgb\u0026fit=max\u0026fm=jpg\u0026ixid=MnwyMzA1MjZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjEwMjYyNTc\u0026ixlib=rb-1.2.1\u0026q=80\u0026w=400",
      "thumb":"https://images.unsplash.com/photo-1619114057582-2033419f4f7e?crop=entropy\u0026cs=tinysrgb\u0026fit=max\u0026fm=jpg\u0026ixid=MnwyMzA1MjZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjEwMjYyNTc\u0026ixlib=rb-1.2.1\u0026q=80\u0026w=200"
   },
   "links":{
      "self":"https://api.unsplash.com/photos/ECteVg5suUg",
      "html":"https://unsplash.com/photos/ECteVg5suUg",
      "download":"https://unsplash.com/photos/ECteVg5suUg/download",
      "download_location":"https://api.unsplash.com/photos/ECteVg5suUg/download?ixid=MnwyMzA1MjZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjEwMjYyNTc"
   },
   "categories":[

   ],
   "likes":66,
   "liked_by_user":false,
   "current_user_collections":[

   ],
   "sponsorship":null,
   "user":{
      "id":"x1-q6QyV6U0",
      "updated_at":"2021-05-14T04:43:01-04:00",
      "username":"saudedum",
      "name":"Saud Edum",
      "first_name":"Saud",
      "last_name":"Edum",
      "twitter_username":"saudedum ",
      "portfolio_url":"https://instagram.com/saudedum",
      "bio":"Sharing the beauty of small nation called Maldives (ދިވެހިރާއްޖެ) 🇲🇻. الله ☝️.",
      "location":"Maldives ",
      "links":{
         "self":"https://api.unsplash.com/users/saudedum",
         "html":"https://unsplash.com/@saudedum",
         "photos":"https://api.unsplash.com/users/saudedum/photos",
         "likes":"https://api.unsplash.com/users/saudedum/likes",
         "portfolio":"https://api.unsplash.com/users/saudedum/portfolio",
         "following":"https://api.unsplash.com/users/saudedum/following",
         "followers":"https://api.unsplash.com/users/saudedum/followers"
      },
      "profile_image":{
         "small":"https://images.unsplash.com/profile-1540499635200-df6572d31bf7?ixlib=rb-1.2.1\u0026q=80\u0026fm=jpg\u0026crop=faces\u0026cs=tinysrgb\u0026fit=crop\u0026h=32\u0026w=32",
         "medium":"https://images.unsplash.com/profile-1540499635200-df6572d31bf7?ixlib=rb-1.2.1\u0026q=80\u0026fm=jpg\u0026crop=faces\u0026cs=tinysrgb\u0026fit=crop\u0026h=64\u0026w=64",
         "large":"https://images.unsplash.com/profile-1540499635200-df6572d31bf7?ixlib=rb-1.2.1\u0026q=80\u0026fm=jpg\u0026crop=faces\u0026cs=tinysrgb\u0026fit=crop\u0026h=128\u0026w=128"
      },
      "instagram_username":"saudedum ",
      "total_collections":0,
      "total_likes":10,
      "total_photos":26,
      "accepted_tos":true,
      "for_hire":false
   },
   "exif":{
      "make":null,
      "model":null,
      "exposure_time":null,
      "aperture":null,
      "focal_length":null,
      "iso":null
   },
   "location":{
      "title":"Thaa, Maldives",
      "name":"Thaa, Maldives",
      "city":null,
      "country":"Maldives",
      "position":{
         "latitude":2.1676485,
         "longitude":73.0240947
      }
   },
   "views":189471,
   "downloads":1502
}
"""
import json


class NotOkException(Exception):
    pass


class PhotoResponseWrapper:
    def __init__(self, raw_response):
        self.code = raw_response.status_code
        if self.code == 200:
            self.body = json.loads(raw_response.text)
            self.photos = {'download_links': [], 'descriptions': []}
            if isinstance(self.body, list): # если несколько фото
                for ph in self.body:
                    self.photos['descriptions'].append(ph['description'])
                    self.photos['download_links'].append(ph['links']['download'])
            else:
                self.photos['descriptions'].append(self.body['description'])
                self.photos['download_links'].append(self.body['links']['download'])
        else:
            raise NotOkException(f"Не могу получить фото. HTML код {self.code}")
