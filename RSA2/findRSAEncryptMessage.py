n = "c20a1d8b3903e1864d14a4d1f32ce57e4665fc5683960d2f7c0f30d5d247f5fa264fa66b49e801943ab68be3d9a4b393ae22963888bf145f07101616e62e0db2b04644524516c966d8923acf12af049a1d9d6fe3e786763613ee9b8f541291dcf8f0ac9dccc5d47565ef332d466bc80dc5763f1b1139f14d3c0bae072725815f"
e = 65537
C="49f573321bdb3ad0a78f0e0c7cd4f4aa2a6d5911c90540ddbbaf067c6aabaccde78c8ff70c5a4abe7d4efa19074a5249b2e6525a0168c0c49535bc993efb7e2c221f4f349a014477d4134f03413fd7241303e634499313034dbb4ac96606faed5de01e784f2706e85bf3e814f5f88027b8aeccf18c928821c9d2d830b5050a1e"

key = "b7a69b4584371182ca5cca738c96dbd0fee0e7f66655bbcb688b66c98e528e794f92a48fb48e8a928cc16fff6a835cdfe55ec77f5480c206dee3dbd40c3e3d24e700af4b4edd01de9a51e9e9f5dd6aa6fb94f55f4b36498de37ec9d65ac32efa39e618ffb8200a8ef7f6868886088e918fa4d57f7b337e17f23aec4b513cbf85"

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