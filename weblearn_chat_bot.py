from requests import get
from time import sleep
import datetime
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from threading import Thread
from os import remove, listdir
from fuzzywuzzy import fuzz, process


def print_with_title(*args):
    print("weblearn:", " ".join([str(i) for i in args]))


def load_image(file):
    upload = vk_api.VkUpload(vk_bot)
    photo = upload.photo_messages(file)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment


def messages_send(peer_id, lesson):
    global localhost
    t = "*" * 30
    try:
        with open(f"static/img/weblearn/{lesson['id']}.png", 'wb') as file:
            file.write(bytes.fromhex(lesson['top_image']))
        # with open(f"static/img/weblearn/{lesson['id']}.png", 'rb') as file:
        #    print_with_title(file.read())
        #sleep(4)
        print_with_title(load_image(f"static/img/weblearn/{lesson['id']}.png"))
        print_with_title(lesson.keys())
        vk_bot.messages.send(peer_id=peer_id,
                             message=lesson['title'] + "\n" + "\n" + lesson[
                                 'text'] + "\n" + t + "\n" + f"http://{localhost}/lesson/{lesson['id']}",
                             random_id=random.randint(0, 100),
                             attachment=load_image(f"static/img/weblearn/{lesson['id']}.png"))
    except KeyError:
        vk_bot.messages.send(peer_id=peer_id,
                             message=lesson['title'] + "\n" + "\n" + lesson[
                                 'text'] + "\n" + t + "\n" + f"http://{localhost}/lesson/{lesson['id']}",
                             random_id=random.randint(0, 100))
    print_with_title(listdir("static/img/weblearn"))
    [remove("static/img/weblearn/" + i) for i in listdir("static/img/weblearn") if i.split(".")[0] == str(lesson['id']) and i.split(".")[-1] == 'png']


def answer_mess(event):
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        response = vk_bot.users.get(user_id=event.user_id)
        #print_with_title(response)
        if response[0]['id'] not in users.keys():
            vk_bot.messages.send(peer_id=event.peer_id,
                                 message=f"Привет {response[0]['first_name']}! Я чат бот для сайта http://weblearn-project.herokuapp.com/weblearn",
                                 random_id=random.randint(0, 100),
                                 attachment="photo-204142875_457239297_89b95b3fa5f8750e8e")  # load_image("static/img/hi.png"))
            sleep(1)
            vk_bot.messages.send(peer_id=event.peer_id,
                                 message="У меня есть следующие функции:\n" + "\n".join(command_out),
                                 random_id=random.randint(0, 100))
        elif datetime.datetime.now() - users[response[0]['id']] > datetime.timedelta(hours=2):
            vk_bot.messages.send(peer_id=event.peer_id,
                                 message=f"С возвращением {response[0]['first_name']}. Хочешь перейти на сайта http://weblearn-project.herokuapp.com/weblearn?",
                                 random_id=random.randint(0, 100),
                                 attachment="photo-204142875_457239297_89b95b3fa5f8750e8e")  # load_image("static/img/hi.png"))
        users[response[0]['id']] = datetime.datetime.now()
        mes = event.text.lower()
        print_with_title(event.user_id, mes)
        res = process.extractOne(" ".join(mes.split()), [i for i in command if len(mes) >= len(i)])
        print_with_title(res)
        if res is not None and res[1] >= 90:
            if res[0] in command[3:5]:
                vk_bot.messages.send(peer_id=event.peer_id,
                                     message="У меня есть следующие функции:\n" + "\n".join(command_out),
                                     random_id=random.randint(0, 100))
            elif res[0] in command[5:9]:
                print_with_title(datetime.datetime.now().strftime('%d-%B-%y %H:%M:S %A'))
                vk_bot.messages.send(peer_id=event.peer_id,
                                     message=f"Сейчас: {datetime.datetime.now().strftime('%d-%B-%y %H:%M:%S %A')}",
                                     random_id=random.randint(0, 100))
            elif res[0] in command[:3]:
                if res[0] == command[0]:
                    try:
                        print_with_title(f'http://{localhost}/api/v1/lesson/{int(mes.split()[-1])}/j')
                        s = get(f'http://{localhost}/api/v1/lesson/{int(mes.split()[-1])}/j').json()
                    except ValueError:
                        print_with_title(f'http://{localhost}/api/v1/lesson/0/{"-".join(mes.split()[2:])}')
                        s = get(f'http://{localhost}/api/v1/lesson/0/{"-".join(mes.split()[2:])}').json()
                else:
                    s = get(f'http://{localhost}/api/v1/lessons').json()
                try:
                    l = [int(i) for i in s['lessons'].keys()]
                    l.sort(reverse=True)
                    l = [str(i) for i in l]
                    if not (res[0] != command[1] or len(l) <= 10):
                        l = l[:10]
                    id = random.choice(l)
                    s = s['lessons'][id]
                    s['id'] = id
                    print_with_title(s['title'])
                    messages_send(event.peer_id, s)
                except KeyError as e:
                    print_with_title("!!!", e.__class__, e)
                    if res[0] == command[0]:
                        vk_bot.messages.send(peer_id=event.peer_id, message="Такой урок не найден",
                                             random_id=random.randint(0, 100))
                    else:
                        vk_bot.messages.send(peer_id=event.peer_id, message="Нет ничего нового",
                                             random_id=random.randint(0, 100))


# localhost = "127.0.0.1:8080"
localhost = "weblearn-project.herokuapp.com"


def main(WEBLEARN_TOKEN):
    if WEBLEARN_TOKEN is None:
        print_with_title("Нет токена")
        return "Нет токена"
    global vk_session_bot, vk_bot, longpoll, command, command_out, users
    vk_session_bot = vk_api.VkApi(token=WEBLEARN_TOKEN)
    vk_bot = vk_session_bot.get_api()
    longpoll = VkLongPoll(vk_session_bot)
    command = ["Выведи урок", "Выведи последние уроки", "Выведи новые уроки", "помоги", "help", "время", "число",
               "дата", "день"]
    command_out = ["Выведи урок <название>", "Выведи урок <номер>", "Выведи последние уроки", "Выведи новые уроки",
                   "помоги", "help", "время", "число", "дата", "день"]
    users = {}
    work()


def work():
    for event in longpoll.listen():
        t = Thread(target=answer_mess, args=(event,))
        t.start()
