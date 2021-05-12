"""
    made by @skvozsneg
"""
import vk_api

import utils.secret as sec

vk_session = vk_api.VkApi(sec.vk_login, sec.vk_password)
vk_session.auth()

vk = vk_session.get_api()


