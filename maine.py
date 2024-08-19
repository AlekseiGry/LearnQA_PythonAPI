import requests, json

#Ex4: GET-запрос
response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)

# Ex5: Парсинг JSON
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)
print(obj['messages'][1]['message'])

# Ex6: Длинный редирект
response = requests.get('https://playground.learnqa.ru/api/long_redirect')

print('Ex6: Длинный редирект')
print("Колличество редиректов: ", len(response.history))
print("Конечный URL: ",response.history[1].url)