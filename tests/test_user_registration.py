from src.conditions import status_code, body
from src.services import UserApiService


def test_can_register_user_valid_credentials(faker):
    user = {'username': faker.name(), 'password': '123456', 'email': 'demoztest@gmail.com'}
    response = UserApiService().create_user(user)

    response.should_have(status_code(200))
    response.should_have(body('$.id', None))


def test_can_not_register_user_with_same_credentials_twice(faker):
    user = {'username': faker.name(), 'password': '123456', 'email': 'demoztest@gmail.com'}

    response = UserApiService().create_user(user)
    response.should_have(status_code(200))

    response = UserApiService().create_user(user)
    response.should_have(status_code(500))

# can add verify schema

# for verify data for BD better add via API
