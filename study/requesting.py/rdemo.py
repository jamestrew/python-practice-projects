import requests

payload = {
    'username': 'james',
    'password': 'testing'
}
r = requests.get('http://httpbin.org/basic-auth/james/testing', auth=('james', 'testing1'))

print(r)
