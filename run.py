from rsa import RSA
from crypt import Crypt

rsa = RSA()
pub, priv = rsa.generate_keys()

crypt = Crypt(pub, priv)
pre, enc = crypt.encrypt('Блокчейн')

dec = crypt.decrypt(enc)
print(f'Ключи: {pub}, {priv}')
print(f'До шифрования: {pre}')
print(f'После: {enc}')
print(f'Расшифровка: {dec}')