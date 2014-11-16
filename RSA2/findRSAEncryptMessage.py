def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def findDKey(pubExp, prime1, prime2):
	phi = (prime1-1)*(prime2-1)
	#solve e*d % phi = 1
	#Extended Euclidean algorithm: 
	#for some a*x % m = 1
	# ax - qm = 1
	d = modinv(pubExp,phi)
	return d