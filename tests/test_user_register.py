import requests, pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    #Ex15: Тесты на метод user        
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        
        data = self.preapare_registration_data(email)
        response = requests.post('https://playground.learnqa.ru/api/user/', data)

        assert response.status_code == 400, f"Unexpected statis code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpexted response content {response.content}"

    def test_create_user_with_invalid_email(self):
        email = 'vinkotov.example.com'
        data = self.preapare_registration_data(email)
        response = requests.post('https://playground.learnqa.ru/api/user/', data)

        assert response.status_code == 400, f"Unexpected statis code {response.status_code}"
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpexted response content {response.content}"

    @pytest.mark.parametrize('key', ['password','username','firstName','lastName','email'])
    def test_create_user_without_fild(self, key):
        email = 'withoutfild@example.com'
        data = self.preapare_registration_data(email)
        del data[key]
        
        response = requests.post('https://playground.learnqa.ru/api/user/', data)

        assert response.status_code == 400, f"Unexpected statis code {response.status_code}"
        assert response.content.decode("utf-8") == f"The following required params are missed: {key}", f"Unexpexted response content {response.content}"

    def test_create_user_with_short_username(self):
        username = 'v'
        data = self.data_preparator('username', username)
        response = requests.post('https://playground.learnqa.ru/api/user/', data)

        assert response.status_code == 400, f"Unexpected statis code {response.status_code}"
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", f"Unexpexted response content {response.content}"

    def test_create_user_with_long_username(self):
        username = 'viiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiigggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg'
        data = self.data_preparator('username', username)
        response = requests.post('https://playground.learnqa.ru/api/user/', data)

        assert response.status_code == 400, f"Unexpected statis code {response.status_code}"
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long", f"Unexpexted response content {response.content}"


    def data_preparator(self, key, val):
        data = {
                'password':'123',
                'username':'lernqa',
                'firstName':'lernqa',
                'lastName':'lernqa',
                'email':'test@test.com'
            }
        
        data[key] = val

        return data






"""Список тестов:

- Создание пользователя с некорректным email - без символа @

- Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить, что отсутствие любого параметра не дает зарегистрировать пользователя

- Создание пользователя с очень коротким именем в один символ

- Создание пользователя с очень длинным именем - длиннее 250 символов"""