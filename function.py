import requests
import config
def send_message(user_id, message):
    response = requests.get('https://api.vk.com/method/messages.send',
                            params={'access_token': config.token['token'], 'user_id': user_id, 'message': message,
                                    'random_id': 0, 'v': config.token['version']}).json()
    if "error" in response and response["error"]["error_code"] == 901: return False
    return True


