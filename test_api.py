import pytest, requests, json

# Ex12: Тест запроса на метод header
def test_check_header():
    url = 'https://playground.learnqa.ru/api/homework_header'
    response = requests.get(url)
    print(response.headers['x-secret-homework-header'])
    assert 'Some secret value' in response.headers['x-secret-homework-header'], 'Invalid value'

# Ex13: User Agent
parameters = [('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 
                    {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}),
                    ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
                    {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}),
                    ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                    {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}),
                    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
                    {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}),
                    ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                    {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}),
]

class TestAPI:
    @pytest.mark.parametrize('user_agent, expected_vals', parameters)
    def test_user_agent(self, user_agent, expected_vals):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'

        response = requests.get(url, headers={"User-Agent": user_agent})
        parameters_name = ['platform', 'browser', 'device']
        
        for parametr_name in parameters_name:
            assert parametr_name in response.text, f"Parameter '{parametr_name}' does't exist"
        
        obj = response.json()
        
        for parametr_name in parameters_name:
            assert obj[parametr_name] == expected_vals[parametr_name], f"Unexpected pararameter '{parametr_name}'"