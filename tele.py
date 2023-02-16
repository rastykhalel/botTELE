from flask import Flask
from flask import request
from flask import Response
import requests
 
TOKEN = "6074685106:AAHoNB5ifHi86rZU-goOAEx1yNgW5jUJSXQ"

app = Flask(__name__)
 
def tel_parse_message(message):
    print("message-->",message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)
 
        return chat_id,txt
    except:
        print("NO text found-->>")
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
 
    return r
 
def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://pbs.twimg.com/profile_images/1461721835612086278/aRU8UWni_400x400.jpg",
        'caption': "This is a sample image"
    }
 
    r = requests.post(url, json=payload)
    return r
 
@ app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        try:
            chat_id, txt = tel_parse_message(msg)
            if txt == "hi":
                tel_send_message(chat_id,"Hello, world!")
            if txt == "rasty":
                tel_send_message(chat_id,"i love this name")
            if txt == "/start":
                tel_send_image(chat_id)
 
            else:
                tel_send_message(chat_id, 'from webhook')
        except:
            print("from index-->")
 
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
    app.run(threaded=True)
     