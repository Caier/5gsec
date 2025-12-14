# /// script
# dependencies = ["pycryptodome"]
# ///

from Crypto.Cipher import AES
from random import randbytes

OP = b"hilosiakhilosiak"
assert len(OP) == 16

K = randbytes(16)

aes = AES.new(K, AES.MODE_EAX)

OPc = bytes(b1 ^ b2 for b1, b2 in zip(aes.encrypt(OP), OP))

print(f"K = {K.hex()}\nOPc = {OPc.hex()}")
