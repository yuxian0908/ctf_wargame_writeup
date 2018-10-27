import requests
import re

user = "natas4"
pwd = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url = 'http://%s.natas.labs.overthewire.org/' % user
session = requests.Session()

response = session.get(url, auth=(user,pwd))
content = response.text

print(content)