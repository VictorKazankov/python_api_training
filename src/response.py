import allure


class AssertableResponse:
    def __init__(self, response):
        self._response = response

    @allure.step('status code shoud be "{code}"')
    def status_code(self, code):
        return self._response.status_code == code

    @allure.step
    def field(self, name):
        return self._response.json()[name]

    def should_have(self, condition):
        condition.match(self._response)
        return self
