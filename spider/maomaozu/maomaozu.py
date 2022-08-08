# from Cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.Cipher import AES
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

import base64


def aes_cbc_encrypt(decrypt_text: str, key: str, iv: str):
    aes2 = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypt_text = aes2.encrypt(pad(decrypt_text.encode('utf-8')), AES.block_size, style='pkcs7')
    encrypt_text = str(base64.encodebytes(encrypt_text), encoding='utf-8').replace("\n", "")
    print(encrypt_text)
    return encrypt_text


iv = '55b3b62613aef1a0'

