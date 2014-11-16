import os
import binascii
from Crypto.PublicKey import RSA
import findRSAEncryptMessage

p = 521419622856657689423872613771
q = 671998030559713968361666935769
n = p*q
e = 65537
d = findRSAEncryptMessage.findDKey(e,p,q)
print n,p,q,e,d
flag = "RSAwithSmallNumsIsEasy"
c = pow(int(flag.encode('hex'),16),e,n)

print "The ciphertext is:", c 
print "N = ", n
print "p = ", p
print "q = ", q
print "e = ", e
print "d = ", d
print binascii.unhexlify('%02x' % pow(c,d,n))