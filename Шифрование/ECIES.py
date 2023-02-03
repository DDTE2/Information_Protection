from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
eth_k = generate_eth_key(
sk = eth_k.to_hex()  # hex string
pk = eth_k.public_key.to_hex()  # hex string

print(sk)
