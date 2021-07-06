"""
    made by @skvozsneg
"""
from single_run_apps.posts.set_ph_posts import create_ph_posts
from utils.posts_utils.time_generator import TimeEnum


def main():
    create_ph_posts(
        date_from=1629314478,
        day_count=30,
        _time=TimeEnum.EVENING
    )


if __name__ == "__main__":
    main()
