import base64, json, urllib.request
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

BASE = "http://80-f2fe9d81-8f60-474f-ad63-91de29f9d6d1.challenge.ctfplus.cn"
#每次启动实例记得改

jwks = json.load(urllib.request.urlopen(BASE + "/.well-known/jwks.json"))
jwk = jwks["keys"][0]

def b64u_dec(s):
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))

n = int.from_bytes(b64u_dec(jwk["n"]), "big")
e = int.from_bytes(b64u_dec(jwk["e"]), "big")

pub = rsa.RSAPublicNumbers(e, n).public_key()
pem = pub.public_bytes(
    serialization.Encoding.PEM,
    serialization.PublicFormat.SubjectPublicKeyInfo,
)

print(pem.decode())
open("public.pem", "wb").write(pem)