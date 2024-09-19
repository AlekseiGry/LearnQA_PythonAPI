from requests import Response
import json, allure

class Assertions:
    @staticmethod
    def assert_format_json(response: Response):
        with allure.step('checking json format'):
            try:
                response_as_dict = response.json()
                return response_as_dict
            except json.JSONDecodeError:
                assert False, f"Rsponse is not in JSON format. Response text is '{response.text}'"

    @staticmethod
    def assert_json_value_by_name( response: Response, name, expected_value, error_message):
        response_as_dict = Assertions.assert_format_json(response)
        
        with allure.step('assert json value by name'):
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
            assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response:Response, name):
        response_as_dict = Assertions.assert_format_json(response)
        
        with allure.step('assert json has key'):
            assert name in response_as_dict, f"Response JSON doesn`t have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response:Response, name):
        response_as_dict = Assertions.assert_format_json(response)
        with allure.step('assert json has not key'):
            assert name not in response_as_dict, f"Response JSON shouldn`t have key '{name}. But it`s present"
    
    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        response_as_dict = Assertions.assert_format_json(response)
        
        with allure.step('assert json has keys'):
            for name in names:
                assert name in response_as_dict, f"Response JSON doesn`t have key '{name}'"
    
    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        with allure.step('assert json has not keys'):
            for name in names:
               Assertions.assert_json_has_not_key(response, name)

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        with allure.step('assert code status'):
            assert response.status_code == expected_status_code, \
                f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

