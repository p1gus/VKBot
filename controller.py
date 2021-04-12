from function import send_message

def controller(user_id, message):
    message = message.lower()
    if message == "начать":
        send_message(user_id, "Привет, друг!")

