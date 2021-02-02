import imaplib 
import email 
from email.header import decode_header 
import webbrowser 
import os


class Message_recieve:
    
    def __init__(self,mail_id,pwd):
        self.mail_id = mail_id
        self.pwd = pwd
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com')
        self.result = self.imap.login(self.mail_id,self.pwd)
        
        
    def get_msg(self,msg_from):
        
        while True:
            self.imap.select('"[Gmail]/All Mail"',  readonly = True)  
            
            response, messages = self.imap.search(None,  
                                            'UnSeen') 
            messages = messages[0].split() 
            
            # take it from last 
            latest = int(messages[-1]) 
            
            # take it from start 
            oldest = int(messages[0]) 
            
            for i in range(latest, latest-20, -1): 
                # fetch 
                res, msg = self.imap.fetch(str(i), "(RFC822)") 
                
                for response in msg: 
                    if isinstance(response, tuple): 
            
                        msg = email.message_from_bytes(response[1]) 
                        # print required information 
                        #print(msg["Date"]) 
                        sender_id = msg["From"] 
                        #print(msg["Subject"])
                        #print(sender_id)
                        try: 
                            sender_id = sender_id.split('<')[1][:-1]
                        except Exception as e:
                            #print(e)
                            if sender_id == msg_from:
                                #print(msg['Subject'])
                                return msg['Subject'] 
                            return None
                        if sender_id == msg_from:
                            #print(msg['Subject'])
                            return msg['Subject']




