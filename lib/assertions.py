from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_format_json(response: Response):
        try:
            response_as_dict = response.json()
            return response_as_dict
        except json.JSONDecodeError:
            assert False, f"Rsponse is not in JSON format. Response text is '{response.text}'"

    @staticmethod
    def assert_json_value_by_name( response: Response, name, expected_value, error_message):
        response_as_dict = Assertions.assert_format_json(response)

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response:Response, name):
        response_as_dict = Assertions.assert_format_json(response)
        assert name in response_as_dict, f"Response JSON doesn`t have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response:Response, name):
        response_as_dict = Assertions.assert_format_json(response)

        assert name not in response_as_dict, f"Response JSON shouldn`t have key '{name}. But it`s present"
    
    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        response_as_dict = Assertions.assert_format_json(response)

        for name in names:
            assert name in response_as_dict, f"Response JSON doesn`t have key '{name}'"
    

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):

        for name in names:
           Assertions.assert_json_has_not_key(response, name)
