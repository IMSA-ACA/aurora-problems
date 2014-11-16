import os
import binascii
from Crypto.PublicKey import RSA

#Generate a random RSA object
rsa = RSA.generate(1024,os.urandom)

#Get the modulus, primes, and keys
n = getattr(rsa, 'n')
p = getattr(rsa, 'p')
q = getattr(rsa, 'q')
e = getattr(rsa, 'e')
d = getattr(rsa, 'd')

#Make a flag
flag = "ThisIsJustTheBeginningOfRSA!"

#Turn them into hex.
c = hex(pow(int(flag.encode('hex'),16),e,n))
#Snip the first two characters "0x" and the last "L"
#Repeat for all variables
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

#Print out our cleaned up hex strings
print "The ciphertext is:", c 
print "N = ", n
print "p = ", p
print "q = ", q
print "e = ", e
print "d = ", d

#Compute the flag
c1 = int(c,16)
d1= int(d,16)
n1 = int(n,16)
print binascii.unhexlify(hex(pow(c1,d1,n1))[2:len(hex(pow(c1,d1,n1)))-1])