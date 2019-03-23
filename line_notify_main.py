import requests

def lineNotifyMessage(token,message):
    # 依照官方設定既有格式，post至server
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message':message}
    r = requests.post('https://notify-api.line.me/api/notify',headers=headers,params=payload)
    return r.status_code

token = ''  # token設定位置
while(True):
    msg = input('msg >> ')
    if msg == '!exit':
        break
    sc = lineNotifyMessage(token,msg)
