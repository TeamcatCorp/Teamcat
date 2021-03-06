#coding=utf-8
'''
Created on 2014-10-10

@author: Devuser
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
from gatesidelib.common.simplelogger import SimpleLogger

class EmailHelper(object):
    '''
    helper for send email
    '''
    
    def __init__(self,emailhost,postuser,password,postfix,port=25):
        self.host=emailhost
        self.user=postuser
        self.password=password
        self.mailpostfix=postfix
        self.port=port

    def sendemaillogin(self,to,subject,message):
        
        try:
            me=self.user+"<"+self.user+"@"+self.mailpostfix+">"
            s = smtplib.SMTP()
            s.connect(host=self.host,port=self.port)
            s.login(self.user,self.password)
            s.sendmail(me,to,message)
            s.close()
            return True
        except Exception as e:
            SimpleLogger.error(str(e))
            return False
    
    def sendmail_nologin(self,to,subject,message):
        try:
            me=self.user+"<"+self.user+"@"+self.mailpostfix+">"
            s = smtplib.SMTP()
            s.connect(host=self.host,port=self.port)
            s.sendmail(me,to,message)
            s.close()
            return True
        except Exception as e:
            SimpleLogger.error(str(e))
            return False
    
    def generatetextmessage(self,message,subject,to,emailformat):
        me=self.user+"<"+self.user+"@"+self.mailpostfix+">"
        msg = MIMEText(message,emailformat,'utf-8')
        msg['Subject'] =subject
        msg['From'] = me
        msg['To'] = to
        return msg
        
        
        