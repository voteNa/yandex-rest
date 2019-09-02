from __future__ import absolute_import

from flask import json
from tests.test import BaseTestCase


class TestControllers(BaseTestCase):
    def test_import_post(self):
        """
        Создание импорта
        """
        body = {
            "citizens": [
                {
                    "citizen_id": 1,
                    "town": "Москва",
                    "street": "Льва Толстого",
                    "building": "16к7стр5",
                    "apartment": 7,
                    "name": "Иванов Иван Иванович",
                    "birth_date": "26.12.1986",
                    "gender": "male",
                    "relatives": [2]
                },
                {
                    "citizen_id": 2,
                    "town": "Москва",
                    "street": "Льва Толстого",
                    "building": "16к7стр5",
                    "apartment": 7,
                    "name": "Иванов Сергей Иванович",
                    "birth_date": "01.04.1997",
                    "gender": "male",
                    "relatives": [1]
                },
                {
                    "citizen_id": 3,
                    "town": "Керчь",
                    "street": "Иосифа Бродского",
                    "building": "2",
                    "apartment": 11,
                    "name": "Романова Мария Леонидовна",
                    "birth_date": "23.11.1986",
                    "gender": "female",
                    "relatives": []
                }
            ]
        }
        response = self.client.open(
            '/imports',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_people_import_list(self):
        """
        Получение всех граждан из импорта
        """
        response = self.client.open(
            '/imports/{import_id}/citizens'.format(import_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_people_patch(self):
        """
        Метод редактирования гражданина
        """
        body = {
            "name": "Иванова Мария Леонидовна",
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "relatives": [1]
        }
        response = self.client.open(
            '/imports/{import_id}/citizens/{citizen_id}'.format(import_id=1, citizen_id=1),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
