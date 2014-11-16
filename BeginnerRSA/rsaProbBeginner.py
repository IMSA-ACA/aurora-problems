import os
import binascii
from Crypto.PublicKey import RSA
import findRSAEncryptMessage

#Found two 30 digit primes. Not too high, but high enough for N to be able to encrypt the plaintext.
# Ex: 5 and 7 would not be good primes as N would be too small to encrypt the long flag we have.
p = 521419622856657689423872613771
q = 671998030559713968361666935769
#N is always the mutliplication of the two primes
n = p*q
#Pick an e.
e = 65537
#Find a D with modular inverse through eGCD
d = findRSAEncryptMessage.findDKey(e,p,q)
#Make our flag
flag = "RSAwithSmallNumsIsEasy"

#Get the ciphertext
c = pow(int(flag.encode('hex'),16),e,n)

#Print out our variables
print "The ciphertext is:", c 
print "N = ", n
print "p = ", p
print "q = ", q
print "e = ", e
print "d = ", d

#Compute the flag
print binascii.unhexlify('%02x' % pow(c,d,n))