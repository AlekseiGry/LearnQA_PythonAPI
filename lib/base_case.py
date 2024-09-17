from requests import Response
import json
from datetime import datetime

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find header with name {cookie_name} in the last response"
        return response.cookies[cookie_name]
    
    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with the name {headers_name} in the last response"
        return response.headers[headers_name]
    
    def get_json_value(self, response: Response, name):

        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn`t have key '{name}'"

        return response_as_dict[name]
    
    def preapare_registration_data(self, email=None, **kwargs):

        if email is None:
            base_part = "test"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'Test',
            'lastName': 'Example',
            'email': email
        }

        data.update(kwargs)
        return data