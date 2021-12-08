import abc

import jsonpath_rw


class Condition:
    def __init__(self):
        pass

    @abc.abstractmethod
    def match(self, response):
        return


class StatusCodeCondition(Condition):
    def __init__(self, code):
        super().__init__()
        self.status_code = code

    def match(self, response):
        assert response.status_code == self.status_code


status_code = StatusCodeCondition


class BodyFieldCondition(Condition):
    def __init__(self, json_path, matcher):
        super().__init__()
        self._json_path = json_path
        self._matcher = matcher

    def match(self, response):
        json = response.json()
        value = jsonpath_rw.parse(self._json_path).find(json)
        assert value is not self._matcher


body = BodyFieldCondition
