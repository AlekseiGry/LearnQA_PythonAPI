import pytest, requests

# Ex10: Тест на короткую фразу
def test_short():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, 'Too long phrase'

# Ex11: Тест запроса на метод cookie
def test_check_cookies():
    url = 'https://playground.learnqa.ru/api/homework_cookie'
    response = requests.get(url)
    print(dict(response.cookies))
    assert dict(response.cookies)['HomeWork'] == 'hw_value', 'Answer is changed'