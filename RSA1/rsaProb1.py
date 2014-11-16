import os
import binascii
from Crypto.PublicKey import RSA

rsa = RSA.generate(1024,os.urandom)
n = getattr(rsa, 'n')
p = getattr(rsa, 'p')
q = getattr(rsa, 'q')
e = getattr(rsa, 'e')
d = getattr(rsa, 'd')
flag = "ThisIsJustTheBeginningOfRSA!"
c = pow(int(flag.encode('hex'),16),e,n)
print "The ciphertext is:", c 
print "N = ", n
print "p = ", p
print "q = ", q
print "e = ", e
print "d = ", d
print binascii.unhexlify('%02x' % pow(c,d,n))