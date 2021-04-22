import re
import os
import requests

from bs4 import BeautifulSoup
from selenium import webdriver

def get_comment_pages(path_to_vk_dir):
    for name_html_file in os.listdir(os.path.join(path_to_vk_dir, 'comments')):
        yield name_html_file


def get_comment_links(path_to_html) -> set:
    links = set()
    soup = BeautifulSoup(open(path_to_html), "html.parser")

    for div in soup.findAll('div', class_='item__main'):
        for a in div.findAll('a', href=True):
            links.add(a.text)
    return links


def delete_comments(comments: dict()):
    for k, v in comments.items():
        print(f"Deleting for {k}")
        for link in v:
            ...



# -- launch --
def main():
    VK_PATH = os.path.join('.', 'vk')
    COMMENTS_PATH = os.path.join(VK_PATH, 'comments')
    # -- comments --
    comments_links = dict()
    for comments in get_comment_pages(VK_PATH):
        comments_links.update({comments: get_comment_links(os.path.join(COMMENTS_PATH, comments))})

    print(comments_links)

if __name__ == "__main__":
    main()