import requests, json, time

#Ex4: GET-запрос
response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)

# Ex5: Парсинг JSON
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)
print(obj['messages'][1]['message'], '\n')

# Ex6: Длинный редирект
response = requests.get('https://playground.learnqa.ru/api/long_redirect')

print('Ex6: Длинный редирект')
print("Колличество редиректов: ", len(response.history))
print("Конечный URL: ",response.history[1].url, '\n')


# Ex7: Запросы и методы
print('Ex7: Запросы и методы')

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

response = requests.get(url)
print('Ответ на пустой get: ',response.text)

response = requests.post(url)
print('Ответ на пустой post: ', response.text)


response = requests.head(url)
print('Статус код на head: ', response.status_code, ' - неправильный запрос')
print('В теле ответа ничего: ', response.text, '\n')

methods = ['GET', 'POST', 'PUT', 'DELETE']
def cheker(method, req_method, response):   
    if method == req_method and response.text == '{"success":"!"}':
        print(method, req_method, response.text, ' Ok')
    elif method == req_method and response.text != '{"success":"!"}':
        print(method, req_method, response.text, ' Fail. Ожидался {"success":"!"}')
    elif method != req_method and response.text == '{"success":"!"}':
        print(method, req_method, response.text, ' Fail. Ожидался Wrong method provided')
    else:
        print(method, req_method, response.text, ' Ok')

for method in methods:
    
    req_method = 'GET'
    response = requests.get(url, params={'method': method})
    cheker(method, req_method, response)

    req_method = 'POST'
    response = requests.post(url, data={'method': method})
    cheker(method, req_method, response)

    req_method = 'PUT'
    response = requests.put(url, data={'method': method})
    cheker(method, req_method, response)

    req_method = 'DELETE'
    response = requests.delete(url, data={'method': method})
    cheker(method, req_method, response)

# Ex8: Токены
import json.decoder as JSONDecodeError

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

def get_longtime_job(url):
    response = requests.get(url)
    try:
        obj = response.json()
        sleep_time = int(obj['seconds'])
        token = obj['token']
    except JSONDecodeError:
        return 'JSONDecodeError in first requests'
        
    #print(sleep_time)
    #print(token)

    response = requests.get(url, params={'token':token})
    
    try:
        obj = response.json()
        if obj['status'] != 'Job is NOT ready':
            return 'status: unexpected answer'
    except JSONDecodeError:
        return 'JSONDecodeError in seconde requests'

    time.sleep(sleep_time)

    response = requests.get(url, params={'token':token})
    
    try:
        obj = response.json()
        result = obj['result']
    except JSONDecodeError:
        return 'JSONDecodeError in final requests'
        
    return result


print(get_longtime_job(url))

# Ex9: Подбор пароля

url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'

login = 'super_admin'
password = '1111'
passwords = ['123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345', 'iloveyou', '111111', '123123', 'abc123', 'qwerty123', '1q2w3e4r', 'admin', 'wertyuiop', '654321', '555555', 'lovely', '7777777', 'welcome', '888888', 'princess', 'dragon', 'password1', '123qwe']


for password in passwords:
    response_cookie = requests.post(url,data={'login': login,
                                       'password':password})
    auth_cookie = response_cookie.cookies.get('auth_cookie')
    url_check = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
    response_checker = requests.post(url_check, cookies={'auth_cookie':auth_cookie})
    
    if response_checker.text == 'You are authorized':
        print(password)
        print(response_checker.text)
        break