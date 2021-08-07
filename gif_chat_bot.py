from requests import get, post
import os
import sqlalchemy
from data.gifs import Gif
from data.users import User
import datetime
import random
from threading import Thread
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def print_with_title(*args):
    print("gif:", " ".join([str(i) for i in args]))


def traslater(text):
    api = 'dict.1.1.20210625T163032Z.8ae5e3c147239b47.a46d4abe26b7190787e913b265d869a7c49f5069'
    if 64 < ord(text[0]) < 123:
        lang = "en-ru"
        text_en = text
    else:
        lang = "ru-en"
        text_ru = text
    a = []
    for word in text.split():
        k = get(
            f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={api}&ui=ru&lang={lang}&text={word}").json()
        k = k['def']
        if len(k):
            k = k[0]['tr']
            if len(k):
                a.append(k[0]['text'])
    a = " ".join(a)
    if lang == "ru-en":
        text_en = a
    else:
        text_ru = a
    return text_ru, text_en, lang


def load_gif(file, vk, db_session, text_en, text_ru=""):
    gif = file["images"]["fixed_height"]["url"]
    print_with_title("gif", gif)
    with open(f"static/img/gif/{file['id']}.gif", 'wb') as f:
        f.write(get(gif).content)
    upload_url = vk.docs.getUploadServer(group_id=205470982, v=5.95)["upload_url"]
    post_r = post(upload_url, files={"file": open(f"static/img/gif/{file['id']}.gif", "rb")}).json()
    save = vk.docs.save(v=5.95, file=post_r['file'])
    saved_gif = "https://vk.com/doc" + str(save["doc"]['owner_id']) + "_" + str(save["doc"]['id'])
    db_sess = db_session.create_session()
    gif_db = Gif(id=file['id'], words_en=text_en, words_ru=text_ru, link=saved_gif)
    db_sess.add(gif_db)
    db_sess.commit()
    os.remove(f"static/img/gif/{file['id']}.gif")
    print_with_title(f"static/img/gif/{file['id']}.gif")
    return saved_gif


def random_gif(event, params, text, vk, vk_bot, chat_id, db_session, text_en, text_ru, time=datetime.timedelta(seconds=45)):
    try:
        count = int(text.split()[-1])
    except ValueError:
        count = 3
    start = datetime.datetime.now()
    while count and datetime.datetime.now() - start <= time:
        print_with_title(2.1, event.text)
        data = get("http://api.giphy.com/v1/gifs/random", params=params).json()
        if data["meta"]["status"] == 429:
            vk_bot.messages.send(chat_id=event.chat_id, random_id=random.randint(0, 1000),
                                 message="Количество обращений к сайту превышено, поиск будет из сохраненных гифок")
            return
        db_sess = db_session.create_session()
        try:
            saved_gif = db_sess.query(Gif).filter(Gif.id == data["data"]['id']).one().link
        except sqlalchemy.exc.NoResultFound:
            saved_gif = load_gif(data["data"], vk, db_session, text_en, text_ru)
        vk_bot.messages.send(chat_id=chat_id, message=saved_gif, random_id=random.randint(0, 1000))
        count -= 1


def search_gif(event, params, text, vk, vk_bot, chat_id, db_session, text_en, text_ru, time=datetime.timedelta(seconds=45)):
    try:
        count = int(text.split()[-1])
    except ValueError:
        count = 3
    i = 2 * count
    start = datetime.datetime.now()
    while count and datetime.datetime.now() - start <= time:
        print_with_title(2.2, text)
        params["limit"] = str(count)
        data = get("http://api.giphy.com/v1/gifs/search", params=params).json()
        if data["meta"]["status"] == 429:
            vk_bot.messages.send(chat_id=event.chat_id, random_id=random.randint(0, 1000),
                                 message="Количество обращений к сайту превышено, поиск будет из сохраненных гифок")
            return
        for gif in data["data"]:
            db_sess = db_session.create_session()
            try:
                saved_gif = db_sess.query(Gif).filter(Gif.id == gif['id']).one().link
            except sqlalchemy.exc.NoResultFound:
                saved_gif = load_gif(gif, vk, db_session, text_en, text_ru)
            vk_bot.messages.send(chat_id=chat_id, message=saved_gif, random_id=random.randint(0, 1000))
            count -= 1
            if not count:
                return
        params["offset"] = random.randint(0, 100)
        params["limit"] = count
        i -= 1


def new_mess(event, vk, vk_bot, db_session, GIF_TOKEN):
    print_with_title(1, event.text)
    users = {}
    db_sess = db_session.create_session()
    response = vk_bot.users.get(user_id=event.user_id)
    print_with_title(response)
    try:
        print_with_title(event.user_id)
        user = db_sess.query(User).filter(User.id == event.user_id).one()
        if datetime.datetime.now() - user.modified_date > datetime.timedelta(hours=2):
            vk_bot.messages.send(peer_id=event.peer_id, random_id=random.randint(0, 100),
                                 message=f"С возвращением {response[0]['first_name']}",
                                 attachment="https://vk.com/album-205470982_279908245?z=photo-205470982_457239024%2Falbum-205470982_279908245")
        user.modified_date = datetime.datetime.now()
    except sqlalchemy.exc.NoResultFound:
        vk_bot.messages.send(peer_id=event.peer_id, random_id=random.randint(0, 100),
                             message=f"Привет {response[0]['first_name']}. Я гиф чат бот",
                             attachment="https://vk.com/album-205470982_279908245?z=photo-205470982_457239024%2Falbum-205470982_279908245")
        db_sess = db_session.create_session()
        user_db = User(id=int(response[0]['id']), token=GIF_TOKEN, first_name=response[0]['first_name'],
                       last_name=response[0]['last_name'])
        db_sess.add(user_db)
        db_sess.commit()
    users[response[0]['id']] = datetime.datetime.now()
    print_with_title(users)
    if event.text[0] != ",":
        text_ru, text_en, lang = traslater(event.text.split(" _ ")[0])
        if len(event.text.split(" _ ")) > 1 and "random" in event.text.split(" _ ")[1].split():
            random_gif(event=event, params={"api_key": GIF_TOKEN, "tag": event.text.split(" _ ")[0]}, text=event.text, vk_bot=vk_bot,
                       db_session=db_session, chat_id=event.chat_id, text_en=text_en, text_ru=text_ru, vk=vk)
        else:
            search_gif(event=event, params={"api_key": GIF_TOKEN, "q": event.text, "limit": "3", "offset": random.randint(0, 10),
                               "lang": lang[:2]}, text=event.text, db_session=db_session, chat_id=event.chat_id,
                       text_en=text_en, text_ru=text_ru, vk=vk, vk_bot=vk_bot)
    print_with_title(3, event.text)


def main(TOKEN, GIF_TOKEN, vk, db_session):
    vk_session_bot = vk_api.VkApi(token=TOKEN)
    vk_bot = vk_session_bot.get_api()
    longpoll = VkLongPoll(vk_session_bot, wait=1)
    for event in longpoll.listen():
        if event.from_chat and event.to_me and not event.from_me and (
                event.type == VkEventType.MESSAGE_NEW or event.type == VkEventType.MESSAGE_EDIT) and len(event.text):
            t = Thread(target=new_mess, args=(event, vk, vk_bot, db_session, GIF_TOKEN))
            t.start()
            # t.join()
