from Crypto.Util.number import getPrime
from .secret import flag, d1, d2

assert (d2 - d1 == 30)

p = getPrime(1024)
q = getPrime(1024)

n = p*q
phi = (p-1)*(q-1)

e1 = pow(d1, -1, phi)
e2 = pow(d2, -1, phi)

m = int.from_bytes(flag, 'big')

c = pow(m, e2, n)

print('c =', c)
print('n =', n)
print('e1 =', e1)
print('e2 =', e2)
