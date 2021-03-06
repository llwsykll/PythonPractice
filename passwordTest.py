import hashlib,random

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())
    return md5.hexdigest()


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user = db[username]
    print(user.username)
    print(user.password)
    print(get_md5(password))
    if get_md5(password) == user.password:
        print('Login Success!')
        return True
    else:
        print('Wrong Password')
        return False

login('michael','123456')

login('bob', 'abc999')

login('alice', 'alice2008')
