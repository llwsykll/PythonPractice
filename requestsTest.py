import requests

# r = requests.get('https://www.douban.com/')
# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# 需要HTTP Header时
# r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.json())
# print(r.status_code)
# print(r.text)
# print(r.content)

# post

r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})