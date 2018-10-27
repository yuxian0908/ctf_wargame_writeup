import requests
import re

user = "natas0"
pwd = "natas0"

url = 'http://%s.natas.labs.overthewire.org/' % user
session = requests.Session()

response = session.get(url, auth=(user,pwd))
content = response.text

print(re.findall('<!--The password for natas1 is (.*) -->',content)[0])