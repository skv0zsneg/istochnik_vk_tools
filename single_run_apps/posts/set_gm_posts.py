"""
    made by @skvozsneg
"""
from utils.connection import vk


def create_post():
    print(vk.wall.post(
        owner_id=-115546115,
        from_group=1,
        message='God bless you!',
        publish_date=1620937584)
    )


if __name__ == "__main__":
    create_post()