import pytest, requests, json

# Ex12: Тест запроса на метод header
def test_check_header():
    url = 'https://playground.learnqa.ru/api/homework_header'
    response = requests.get(url)
    print(response.headers['x-secret-homework-header'])
    assert 'Some secret value' in response.headers['x-secret-homework-header'], 'Invalid value'
  