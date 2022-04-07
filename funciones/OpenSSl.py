from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.signature import Signature
from ellipticcurve.utils.file import File



# Generate new Keys
privateKey = PrivateKey()
publicKey = privateKey.publicKey()
print(privateKey)
message = "My test message"
p = privateKey.toPem()
print(p)
# Generate Signature
signature = Ecdsa.sign(message, privateKey)
sing = signature.toDer()



signature = Signature.fromDer('./key/sing.txt','bytes')
# To verify if the signature is valid
print(signature)
print(Ecdsa.verify(message, signature, publicKey))

c