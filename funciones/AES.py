from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

key = b'62503dd746538776'

class AESenc:
    def __init__(self,key):
        self.AES_e = AES.new(key, AES.MODE_EAX)
        self.nonce = self.AES_e.nonce
        self.AES_d = AES.new(key, AES.MODE_EAX, nonce=self.nonce)
    
    def encript(self,data):
        ciphertext, tag = self.AES_e.encrypt_and_digest(data)
        return {'sing':tag,'data':ciphertext}
        
    def decrypt(self,data,sing):
        plaintext = self.AES_d.decrypt(data)
        try:
            self.AES_d.verify(sing)
            return plaintext
        except ValueError:
            return 'error AES sing'
        
AES = AESenc(key)
enCrip = AES.encript(data)
deCrip = AES.decrypt(enCrip['data'],enCrip['sing'])
print(deCrip)