from requests import get, post
import os
import sqlalchemy
from data import db_session
from data.gifs import Gif
from data.users import User
import datetime

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

if 'HEROKU' in os.environ:
    TOKEN = os.environ.get("TOKEN", None)
    VK_LOGIN = os.environ.get("VK_LOGIN", None)
    VK_PASSWORD = os.environ.get("VK_PASSWORD", None)
    GIF_TOKEN = os.environ.get("GIF_TOKEN", None)
else:
    from config import *
login, password = VK_LOGIN, VK_PASSWORD
vk_session_bot = vk_api.VkApi(token=TOKEN)
vk_session = vk_api.VkApi(login, password, app_id=2685278)
vk_session.auth(token_only=True)
vk_bot = vk_session_bot.get_api()
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session_bot, wait=1)
longpoll_my = VkLongPoll(vk_session, wait=1)


def load_image(file):
    upload = vk_api.VkUpload(vk_bot)
    photo = upload.photo_messages(file)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment


db_session.global_init()
gif_url = "http://api.giphy.com/v1/gifs/search"
me_in_chat, me = None, None
users = {}
db_sess = db_session.create_session()
for user in db_sess.query(User).all():
    users[user.id] = datetime.datetime.now() - datetime.timedelta(hours=3)
db_sess.commit()
while 1:
    for event in longpoll.check():
        if event.from_chat and event.to_me and (
                event.type == VkEventType.MESSAGE_NEW or event.type == VkEventType.MESSAGE_EDIT) and len(
            event.text):
            response = vk_bot.users.get(user_id=event.user_id)
            print(response)
            if response[0]['id'] not in users.keys():
                vk_bot.messages.send(peer_id=event.peer_id, random_id=random.randint(0, 100),
                                     message=f"Привет {response[0]['first_name']}. Я чат бот для сайта http://weblearn-project.herokuapp.com/weblearn",
                                     attachment="https://vk.com/album-205470982_279908245?z=photo-205470982_457239024%2Falbum-205470982_279908245")
                db_sess = db_session.create_session()
                user_db = User(id=int(response[0]['id']), TOKEN="")
                db_sess.add(user_db)
                db_sess.commit()
            elif datetime.datetime.now() - users[response[0]['id']] > datetime.timedelta(hours=2):
                vk_bot.messages.send(peer_id=event.peer_id, random_id=random.randint(0, 100),
                                     message=f"С возвращением {response[0]['first_name']}. Хочешь перейти на сайта http://weblearn-project.herokuapp.com/weblearn?",
                                     attachment="https://vk.com/album-205470982_279908245?z=photo-205470982_457239024%2Falbum-205470982_279908245")
            users[response[0]['id']] = datetime.datetime.now()
            print(users)
            if event.text[0] != ",":
                lang = "ru"
                text_ru = event.text
                if 64 < ord(event.text[0]) < 123:
                    lang = "en"
                    text_ru = ""
                    text_en = event.text
                params = {"api_key": GIF_TOKEN, "q": event.text, "limit": "3", "lang": lang}
                data = get(gif_url, params=params).json()
                print(data)
                if data["meta"]["status"] == 429:
                    vk_bot.messages.send(chat_id=event.chat_id, random_id=random.randint(0, 1000),
                                         message="Количество обращений к сайту превышено, поиск будет из сохраненных гифок")
                for gif_file in data["data"]:
                    gif = gif_file["images"]["fixed_height"]["url"]
                    with open(f"static/img/{gif_file['id']}.gif", 'wb') as file:
                        file.write(get(gif).content)
                    '''upload_url = vk.photos.getUploadServer(group_id=205470982, album_id=279908245, v=5.95)["upload_url"]
                    post_r = post(upload_url, files={"file": open(f"static/img/{gif_file['id']}.gif", "rb")}).json()
                    print(post_r)
                    save = vk.photos.save(group_id=205470982, album_id=279908245, v=5.95, photos_list=post_r['photos_list'],
                                               server=post_r['server'], hash=post_r['hash'], aid=post_r['aid'])
                    saved_photo = "gif" + str(save[0]['owner_id']) + "_" + str(save[0]['id'])
                    print(saved_photo)'''
                    upload_url = vk.docs.getUploadServer(group_id=205470982, v=5.95)["upload_url"]
                    post_r = post(upload_url,
                                  files={"file": open(f"static/img/{gif_file['id']}.gif", "rb")}).json()
                    # print(post_r)
                    save = vk.docs.save(v=5.95, file=post_r['file'])
                    # print(save)
                    saved_gif = "https://vk.com/doc" + str(save["doc"]['owner_id']) + "_" + str(
                        save["doc"]['id'])
                    db_sess = db_session.create_session()
                    gif_db = Gif(id=gif_file['id'], en=text_en, ru=text_ru, address=saved_gif)
                    db_sess.add(gif_db)
                    db_sess.commit()
                    os.remove(f"static/img/{gif_file['id']}.gif")
                    # saved_gif = "https://vk.com/doc-205470982_606197486"
                    # print(saved_gif)
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
                if len(k):
                    for word in event.text[1:].split():
                        if k[i]["word"] in word:
                            c = 0
                            while len(word) >= c + len(k[i]["word"]):
                                if word[c:c + len(k[i]["word"])] == k[i]["word"]:
                                    text.append(
                                        word[:c] + k[i]["s"][0] + word[c + len(k[i]["word"]):])
                                    i += 1
                                    break
                        else:
                            text.append(word)
                    text = " ".join(text)
                else:
                    text = event.text[1:]
                if len(text):
                    vk.messages.edit(peer_id=event.peer_id, message_id=event.message_id,
                                     message=text, random_id=random.randint(0, 1000))
