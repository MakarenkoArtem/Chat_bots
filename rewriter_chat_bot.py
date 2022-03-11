from requests import get, post
from threading import Thread
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
import random


def print_with_title(vk, args):
    t, c = "", ""
    '''try:
        t = args.to_me()
    except BaseException:
        pass
    try:
        c = vk.users.get(user_id=args.user_id)[0]
        c = f"{c['first_name']} {c['last_name']}"
    except BaseException:
        pass'''
    print(f"rewrite: {c}", args.type.name, t, vars(args))  # " ".join([str(i) for i in list(vars(args))]))


def rewrite(event, vk):
    if len(event.text) and event.text[0] == ",":
        text = []
        k = get(
            f"https://speller.yandex.net/services/spellservice.json/checkText?text={'+'.join(event.text[1:].split())}").json()
        i = 0
        if len(k):
            for word in event.text[1:].split():
                try:
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
                except IndexError:
                    text.append(word)

            text = " ".join(text)
        else:
            text = event.text[1:]
        if len(text):
            vk.messages.edit(peer_id=event.peer_id, message_id=event.message_id,
                             message=text, random_id=random.randint(0, 1000))


def main(vk, longpoll_my):
    people_send_audio = {}
    white_list = [422445727, 385929442]
    me_in_chat, me = None, None
    for event in longpoll_my.listen():
        try:
            # print_with_title(vk, event)
            # print("white_list", event.peer_id, vk.users.get(user_id=event.peer_id))
            if '"type":"audio_message"' in event.attachments[
                'attachments'] and event.type == VkEventType.MESSAGE_NEW and event.to_me and not event.from_chat:
                if event.peer_id in people_send_audio.keys() and datetime.datetime.now() - people_send_audio[
                    event.peer_id] < datetime.timedelta(minuts=30) and (event.peer_id not in white_list or 75<random.randint(0, 100)):
                    a = 0 / 1
                people_send_audio[event.peer_id] = datetime.datetime.now()
                vk.messages.send(peer_id=event.peer_id, message="",
                                 attachment="video-205470982_456239017",
                                 random_id=random.randint(0, 1000))  # https://vk.com/video-205470982_456239017
        except KeyError:
            pass
        except BaseException as e:
            print(e.__class__, e)
            # print_with_title("!!!", e.__class__, e)
        finally:
            if (event.type == VkEventType.MESSAGE_NEW and event.from_me) or (
                    event.type == VkEventType.MESSAGE_EDIT and event.from_user and (
                    event.user_id == me or (event.from_chat and event.user_id == me_in_chat))):
                t = Thread(target=rewrite, args=(event, vk,))
                t.start()
