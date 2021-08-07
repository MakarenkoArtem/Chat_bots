from requests import get, post
from threading import Thread
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random


def print_with_title(*args):
    print("rewrite:", " ".join([str(i) for i in args]))


def rewrite(event, vk):
    if event.text[0] == ",":
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
    me_in_chat, me = None, None
    for event in longpoll_my.listen():
        try:
            print_with_title(vars(event))
            if '"type":"audio_message"' in event.attachments[
                'attachments'] and event.type == VkEventType.MESSAGE_NEW and event.to_me and not event.from_chat:
                vk.messages.send(peer_id=event.peer_id, message="https://vk.com/video-205470982_456239017",
                                 random_id=random.randint(0, 1000))
        except BaseException as e:
            pass#print_with_title("!!!", e.__class__, e)
        if (event.type == VkEventType.MESSAGE_NEW and event.from_me) or (event.type == VkEventType.MESSAGE_EDIT and (
                event.user_id == me or (event.from_chat and event.user_id == me_in_chat))):
            t = Thread(target=rewrite, args=(event, vk,))
            t.start()
