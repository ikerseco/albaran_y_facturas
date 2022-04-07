from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


import json
from localStoragePy import localStoragePy
import base64
import smtplib
import secrets
import os


#from decouple import config



class encrypt:
  def __init__(self):
      self.prybate = ECC.generate(curve='P-256')
      self.public = self.prybate.public_key()
      self.signature = None
      self.localStorage = localStoragePy('me.jkelokky.mypythonapp', 'json')
      self.mail = None
      self.localStorage = {
        'user' : None,
        'token': None,
      }
      
  def createFolder(self):
      print()
      try:
        os.mkdir('key',mode = 511)
      except FileExistsError:
        None
      os.chdir('key')
      filePU = open('publickey.pem','wt')
      filePU.write(self.public.export_key(format='PEM'))
      filePU.close()
      filePI = open('pribatekey.pem','wt')
      filePI.write(self.prybate.export_key(format='PEM'))
      filePI.close()
     
  def generatemessagesing(self,mail):
       #smtp
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user="secoiker13@gmail.com",password = "$'^(c1[Rhl")
       #firma digital
        messageSt = secrets.token_hex(nbytes=32)#generar secret token
        messageByte = bytes(messageSt,'utf-8')
        menssage = SHA256.new(messageByte)#has generar
        signer = DSS.new(self.prybate,'fips-186-3',encoding='der')
        self.signature = signer.sign(menssage)
        filePI = open('sing.der','wb')
        filePI.write(self.signature)     
        server.sendmail(from_addr="none@gmail.com",to_addrs=mail,msg=messageSt)
        self.mail = mail
      
  def verifyer(self,message):
      messageByte = bytes(message,'utf-8')
      hasMesage = SHA256.new(messageByte)
      verifier = DSS.new(self.public,'fips-186-3',encoding='der')
      try:
          verifier.verify(hasMesage, self.signature)
          mailLocal = self.localStorage.getItem('mailUser')
          if mailLocal == None:
            tokenAES = secrets.token_hex(nbytes=32)
            arrToken = []
            Jsonusers = {
              'user' : self.mail,
              'token': tokenAES,
            }
            arrToken.append(Jsonusers)
            self.localStorage.setItem('mailUser', json.dumps(arrToken))
            data = {'user':self.mail,'pritokenAES':tokenAES,'secotokenAES':None,'error':None}
            return data
          else:
            js = json.loads(mailLocal)
            print(js)
            jsV = False
            xData = None
            for x in js :
              if x['user'] == self.mail:
                jsV = True
                xData = x 
            if jsV == True:
                tokenAES = secrets.token_hex(nbytes=32)
                Jsonusers = {
                  'user' : self.mail,
                  'token': tokenAES,
                }
                data = {'user':self.mail,'pritokenAES':xData['token'],'secotokenAES':tokenAES,'error':None}
                newArray =  AldaArray(self.mail,js,Jsonusers)
                self.localStorage.setItem('mailUser',json.dumps(newArray))
                print(newArray)
                return data
            else:
                tokenAES = secrets.token_hex(nbytes=32)
                Jsonusers = {
                  'user' : self.mail,
                  'token': tokenAES,
                }
                js.append(Jsonusers)
                self.localStorage.setItem('mailUser', json.dumps(js))
                data = {'user':self.mail,'pritokenAES':tokenAES,'secotokenAES':None,'error':None}
                return data
      except ValueError:
            data = {'user':self.mail,'pritokenAES':None,'secotokenAES':None,'error':True}
            return data
      pass


def AldaArray(name,data,json):
    newArray = []
    for x in data :
      if x['user'] != name:
        newArray.append(x)
    newArray.append(json)
    return newArray





