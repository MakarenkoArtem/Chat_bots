from threading import Thread
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os
import gif_chat_bot
import weblearn_chat_bot
import rewriter_chat_bot
from data import db_session
from requests import get, post
try:
    from fuzzywuzzy import fuzz, process
except ModuleNotFoundError:
    import pip

    pip.main(["install", "fuzzywuzzy"])

if 'HEROKU' in os.environ:
    TOKEN = os.environ.get("TOKEN", None)
    VK_LOGIN = os.environ.get("VK_LOGIN", None)
    VK_PASSWORD = os.environ.get("VK_PASSWORD", None)
    GIF_TOKEN = os.environ.get("GIF_TOKEN", None)
    WEBLEARN_TOKEN = os.environ.get("WEBLEARN_TOKEN", None)
else:
    from config import *


def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """
    print(vars(captcha))
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)

vk_session = vk_api.VkApi(VK_LOGIN, VK_PASSWORD, token=TOKEN_USER)#, app_id=2685278, captcha_handler=captcha_handler)
#vk_session.auth(token_only=True)
vk = vk_session.get_api()
longpoll_my = VkLongPoll(vk_session)

db_session.global_init()
Thread(target=gif_chat_bot.main, args=(TOKEN, GIF_TOKEN, vk, db_session,)).start()
Thread(target=rewriter_chat_bot.main, args=(vk, longpoll_my,)).start()
Thread(target=weblearn_chat_bot.main, args=(WEBLEARN_TOKEN,)).start()
