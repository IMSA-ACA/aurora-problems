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
c = hex(pow(int(flag.encode('hex'),16),e,n))
c = c[:len(c)-1]
n = hex(n)
n = n[:len(n)-1]
p = hex(p)
p = p[:len(p)-1]
q = hex(q)
q = q[:len(q)-1]
e = hex(e)
e = e[:len(e)-1]
d = hex(d)
d = d[:len(d)-1]
print "The ciphertext is:", c 
print "N = ", n
print "p = ", p
print "q = ", q
print "e = ", e
print "d = ", d
c1 = int(c,16)
d1= int(d,16)
n1 = int(n,16)
print binascii.unhexlify(hex(pow(c1,d1,n1))[2:len(hex(pow(c1,d1,n1)))-1])