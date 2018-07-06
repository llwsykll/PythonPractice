import  re

print(re.match(r'^\d{3}\-\d{3,8}$','010 12345'))

print(re.split(r'\s+','a b        c       d'))

print(re.split(r'[\s\,]+','a b   ,     c    ,,   d'))

print(re.split(r'[\s\,\;]+','a b   ,   ;  c    ,,   d'))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)

print(m.groups())

#贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

#预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

#验证Email地址
def is_valid_email(addr):
    re_email = re.compile(r'^(<\w[\s\w+]+>\s)?(\w+[\w+.]*@\w+.(org|com)$)')
    #提出名字
    print(re_email.match('<Tom Paris> tom@voyager.org').groups(2))
    if(re_email.match(addr)):
        return True

if is_valid_email('someone@gmail.com')==True:
    print('True1')

if is_valid_email('bill.gates@microsoft.com')==True:
    print('True2')

if is_valid_email('<Tom Paris> tom@voyager.org')==True:
    print('True3')