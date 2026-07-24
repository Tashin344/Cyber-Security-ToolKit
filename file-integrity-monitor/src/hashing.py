import os
import hashlib

def hashing(content):
    hash_object = hashlib.sha256(content)
    hash_value = hash_object.hexdigest()

    return hash_value