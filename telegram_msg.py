import requests
TOKEN = "5"
chat_id = "-1"


def send_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
