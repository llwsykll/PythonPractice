import hmac,random

# def calc_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     print(md5.hexdigest())
#     return md5.hexdigest()


def hmac_md5(key,s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key , password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user = db[username]
    print(user.username)
    print(user.password)
    print(hmac_md5(user.key,password))
    if hmac_md5(user.key,password) == user.password:
        print('Login Success!')
        return True
    else:
        print('Wrong Password')
        return False

login('michael','123456')

login('bob', 'abc999')

login('alice', 'alice2008')
