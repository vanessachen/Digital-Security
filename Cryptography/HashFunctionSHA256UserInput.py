import hashlib
mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.sha256(mystring.encode())
print(hash_object.hexdigest())
