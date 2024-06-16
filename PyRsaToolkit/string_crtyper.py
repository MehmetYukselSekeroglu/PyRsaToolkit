from .rsa_key_loader import loadPrivateKey, loadPublicKey
import rsa


DEFAULT_CHARSET_ENCODINGS = "utf-8"


def encrypte_string(public_key, target_string:str) -> str:
    target_string = str(target_string)
    return rsa.encrypt(target_string.encode(DEFAULT_CHARSET_ENCODINGS),pub_key=public_key)

def decrypte_string(private_key, target_string) -> str:
    return rsa.decrypt(target_string,priv_key=private_key).decode(DEFAULT_CHARSET_ENCODINGS) 