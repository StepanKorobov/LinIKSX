from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import data
import random
import time
import gay
import pictures
from datetime import datetime

login, password = data.LoginAndData()
vk_session = vk_api.VkApi(token="ab9917efbfc2bb8c383d3ef6b32afcc33d5b103b734f1072a6d63be92e6bcd29bfe07d25516650fa8a702")

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send', {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print("ID " + str(event.user_id))
            print('НВРЕМЯ: '+ str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print("Надпись: " + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, Степана нет', 'random_id': 0})
                elif response == "пока":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'и с кем ты общался?', 'random_id': 0})
                elif response == "приветик":
                    send_message(vk_session, 'user_id', event.user_id, message='степан щас делает минетик')
                elif response == "!команды":
                    send_message(vk_session, 'user_id', event.user_id, message='какие?\n бля')
                elif response == "спать":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'хочу негров ибать и реп не читать при луне', 'random_id': 0})
                elif response == "гей":
                    attachment = gay.get(vk_session, -47249819, session_api)
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Держи котиков!', 'random_id': 0, 'attachment':attachment})
                elif response == "котики":
                    attachment = pictures.get(vk_session, -130670107, session_api)
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Держи котиков!', 'random_id': 0, "attachment": attachment})