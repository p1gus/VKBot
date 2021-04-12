#! /usr/bin/python
# Внешние библиотеки
import json
import requests
import threading
# Мои файлы
import config
import controller

# Получение всех токенов и ключей ---------------------------------
version = config.token['version']  # Версия api
token = config.token['token']  # Токен сообщества
response = requests.get('https://api.vk.com/method/groups.getLongPollServer',
                        params={'access_token': token, 'group_id': config.token['group_id'], 'v': version,
                                }).json()['response']
data = {'ts': response['ts']}  # Номер последнего события
key = response['key']  # Ключ запроса
server = response['server']  # Сервер для ожидания ответа


# ----------------------------------

while True:  # Проверка и обработка запросов
    data = requests.get(server, params={'act': 'a_check', 'key': key, 'ts': data['ts'], 'wait': 90, }).json()
    try:
        if data['updates']:
            for mas in data['updates']:
                controller.controller(mas['object']['message']['from_id'], mas['object']['message']['text'])


    except Exception as e:
        response = requests.get('https://api.vk.com/method/groups.getLongPollServer',
                                params={'access_token': token, 'group_id': config.token['group_id'],
                                        'v': version, }).json()['response']
        data = {'ts': response['ts']}  # Номер последнего события
        key = response['key']  # Ключ запроса
        server = response['server']  # Сервер для ожидания ответа
        response = requests.get('https://api.vk.com/method/groups.enableOnline',
                                params={'access_token': token, 'group_id': config.token['group_id'], 'v': version, })
        print('Ошибочное сообщение от ВК')
