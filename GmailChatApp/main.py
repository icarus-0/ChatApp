import eel
import os
import json
from SendMail import Message_send
from ReceveMail import Message_recieve
import time
eel.init("Web")
pre_msg = None
@eel.expose
def catch_creads(email_id_login,pwd_login,client_id):
    print(email_id_login,'     ',pwd_login)
    creads = {
            'email_id' : email_id_login,
            'password' : pwd_login,
            'des_id' : client_id
    }
    a = {
        'pre_msg' : None
    }
    
    with open("login.json", "w") as outfile:  
        json.dump(creads, outfile) 
    try:
        os.mkdir('msg_data')
    except:
        pass
    with open("./msg_data/pre_msg_data.json", "w") as outfile:  
        json.dump(a, outfile)
    

@eel.expose
def catch_send_message(msg):
    with open('login.json') as f:
        c = json.load(f)
    idx = c['email_id']
    pwd = c['password']
    des_id = c['des_id']
    sender = Message_send(idx,pwd)
    sender.send_message(des_id,msg)

@eel.expose
def get_reply():
    print('kisine tho bulya')
    with open('login.json') as f:
        c = json.load(f)
    idx = c['email_id']
    pwd = c['password']
    des_id = c['des_id']
    while True:
        with open('./msg_data/pre_msg_data.json') as f:
            reverts = json.load(f)
        
        reciver = Message_recieve(idx,pwd)
        revert_msg = reciver.get_msg(des_id)
        if reverts['pre_msg'] != revert_msg:
            reverts['pre_msg'] = revert_msg
            if revert_msg != None:
                with open("./msg_data/pre_msg_data.json", "w") as outfile:  
                    json.dump(reverts, outfile)
                break
        time.sleep(1)
        
    print(des_id,' > ',revert_msg)
    return revert_msg
    

if os.path.exists('login.json'):
    eel.start('chatpage.html')
else:   
    eel.start('index.html')
    