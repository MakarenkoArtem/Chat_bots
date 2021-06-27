import sys
from requests import get, post
import json

try:
    import vk_api
except ModuleNotFoundError:
    import pip

    pip.main(["install", "vk_api"])
    import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

try:
    from fuzzywuzzy import fuzz, process
except ModuleNotFoundError:
    import pip

    pip.main(["install", "fuzzywuzzy"])
    from fuzzywuzzy import fuzz, process
import datetime
from time import sleep
from config import *

login, password = VK_LOGIN, VK_PASSWORD
vk_session_bot = vk_api.VkApi(token=TOKEN)
vk_session = vk_api.VkApi(login, password, app_id=2685278)
vk_session.auth(token_only=True)
vk_bot = vk_session_bot.get_api()
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session_bot, wait=1)
longpoll_my = VkLongPoll(vk_session, wait=1)


def send_messages(chat_id, text, attachment=''):
    random_id = random.randint(0, 1000)
    try:
        if not len(attachment):
            return vk_bot.messages.send(chat_id=chat_id, message=text, random_id=random_id)
        else:
            return vk_bot.messages.send(chat_id=chat_id, message=text, random_id=random_id,
                                        attachment=attachment)
    except vk_api.exceptions.ApiError as e:
        print(f'Error {e.__class__.__name__}: {e}')


gif_url = "http://api.giphy.com/v1/gifs/search"

me_in_chat, me = None, None
while 1:
    for event in longpoll.check():
        if event.from_chat and not event.from_me and (
                event.type == VkEventType.MESSAGE_NEW or event.type == VkEventType.MESSAGE_EDIT):
            print(vars(event))
            print(event.from_chat, event.from_me, event.type == VkEventType.MESSAGE_NEW, event.type == VkEventType.MESSAGE_EDIT)
            if event.text[0] != ",":
                params = {
                    "api_key": GIF_TOKEN,
                    "q": event.text,
                    "limit": "1"
                }
                #print(vars(event))
                #print(gif_url)
                #print(params)
                data = get(gif_url, params=params).json()
                #print(data)
                gif = data["data"][0]["images"]["fixed_height"]["url"]
                with open('test.gif', 'wb') as file:
                    file.write(get(gif).content)
                '''upload_url = vk.photos.getUploadServer(group_id=205470982, album_id=279908245, v=5.95)["upload_url"]
                post_r = post(upload_url, files={"file": open("test.gif", "rb")}).json()
                print(post_r)
                save = vk.photos.save(group_id=205470982, album_id=279908245, v=5.95, photos_list=post_r['photos_list'],
                                           server=post_r['server'], hash=post_r['hash'], aid=post_r['aid'])
                saved_photo = "gif" + str(save[0]['owner_id']) + "_" + str(save[0]['id'])
                print(saved_photo)'''
                upload_url = vk.docs.getUploadServer(group_id=205470982, v=5.95)["upload_url"]
                post_r = post(upload_url, files={"file": open("test.gif", "rb")}).json()
                #print(post_r)
                save = vk.docs.save(v=5.95, file=post_r['file'])
                #print(save)
                saved_gif = "https://vk.com/doc" + str(save["doc"]['owner_id']) + "_" + str(save["doc"]['id'])
                print(saved_gif)
                vk_bot.messages.send(chat_id=event.chat_id, message=saved_gif,
                                     random_id=random.randint(0, 1000))

    for event in longpoll_my.check():
        if (event.type == VkEventType.MESSAGE_NEW and event.from_me) or (
                event.type == VkEventType.MESSAGE_EDIT and (
                event.user_id == me or (event.from_chat and event.user_id == me_in_chat))):
            if event.from_chat:
                me_in_chat = event.user_id
            else:
                me = event.user_id
            if event.text[0] == ",":
                text = []
                k = get(
                    f"https://speller.yandex.net/services/spellservice.json/checkText?text={'+'.join(event.text[1:].split())}").json()
                i = 0
                for word in event.text[1:].split():
                    if len(k) and k[i]["word"] in word:
                        c = 0
                        while len(word) >= c + len(k[i]["word"]):
                            if word[c:c + len(k[i]["word"])] == k[i]["word"]:
                                text.append(word[:c] + k[i]["s"][0] + word[c + len(k[i]["word"]):])
                                i += 1
                                break
                    else:
                        text.append(word)
                print(k)
                text = " ".join(text)
                if len(text):
                    vk.messages.edit(peer_id=event.peer_id, message_id=event.message_id,
                                     message=text, random_id=random.randint(0, 1000))