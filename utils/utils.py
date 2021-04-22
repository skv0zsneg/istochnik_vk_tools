import re

def format_comment_to_link_action_id(comment_link):
    res = re.findall(r'wall(.*)_.*reply=(\d*)', comment_link)
    number, reply = res[0][0], res[0][1]
    delete_id_template = f'reply_delete{number}_{reply}'
    return delete_id_template

if __name__ == "__main__":
    print(format_comment_to_link_action_id('https://vk.com/wall605055737_49?reply=50'))
    print(format_comment_to_link_action_id('https://vk.com/wall-97882810_469908?reply=469970&thread=469909'))
