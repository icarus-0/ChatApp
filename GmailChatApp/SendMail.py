import smtplib

class Message_send:
    def __init__(self,sender_email,sender_pwd):
        self.host = sender_email
        
        self.server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        self.server.login(sender_email,sender_pwd)
        #server.sendmail('neuron9889@gmail.com','ezrio1234@gmail.com','HEY BSDK')
        #server.quit() 

    def send_message(self,des_email,msg):
        msg = 'Subject: {}\n\n{}'.format(msg, ' ')
        self.server.sendmail(self.host,des_email,msg)
        
        

