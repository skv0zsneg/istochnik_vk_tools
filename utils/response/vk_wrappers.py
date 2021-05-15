class VkPhotoUploadWrapper:
    def __init__(self, raw_response):
        base = 'photo'
        self.vk_photo_links = []
        for photo in raw_response:
            self.vk_photo_links.append(base + str(photo['owner_id']) + '_' + str(photo['id']))

