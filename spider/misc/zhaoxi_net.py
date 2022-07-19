import  hashlib


m = hashlib.md5()
m.update(b'1234')
print(m.hexdigest())