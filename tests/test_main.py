import unittest
from unittest import TestCase
import pytest
import requests
from task_1 import fio
from task_1 import solve
from task_1 import get_cost

class Test_task_1(TestCase):

    def test_fio(self):

        for i, (initials, expected) in enumerate([
            (["Иванов", "Иван", "Иванович"], "ИИИ"),
            (["Жан", "Клот", "Вандамович"], "ЖКВ"),
            (["Павлов", "Иван", "Уралович"], "ПИУ"),
            (["Семейный", "Доминик", "Торретович"], "СДТ")
        ]):
            with self.subTest(i):
                self.assertEqual(expected, fio(initials))


    def test_fio_fail(self):

        for i, (initials, expected) in enumerate([
            (["Иванов", "Иван", "Иванович"], "ыЫы"),
            (["Жан", "Клот", "Вандамович"], "ЖкВ"),
            (["Павлов", "Иван", "Уралович"], "пИУ"),
            (["Семейный", "Доминик", "Торретович"], "ГГГ")
        ]):
            with self.subTest(i):
                self.assertEqual(expected, fio(initials))

    def test_comp_winners(self):

        for i, (recipies, expected_check_list) in enumerate([
            ([123, 145, 346, 246, 235, 166, 112, 351, 436], ([346, 166, 436], 3)),
            ([123, 145], ([123, 145], 2)),
            ([123, 346, 246, 235, 112, 436], ([246, 436], 2))
        ]):
            with self.subTest(i):
                self.assertEqual(expected_check_list, solve(recipies))

    def test_get_cost(self):

        for i, (weight, expected_value) in enumerate([
            (9, "Стоимость доставки: 200 руб."),
            (10, "Стоимость доставки: 500 руб."),
            (15, "Стоимость доставки: 500 руб.")
        ]):
            with self.subTest(i):
                self.assertEqual(expected_value, get_cost(weight))


class TestYandexDisk:

    def setup_method(self):
        self.headers = {
            "Authorization": "OAuth y0_AgAAAABuNhuuAADLWwAAAAEP5zQBAAAiBbrPHFdHbpVy15eybjebFAeAgQ"
        }

    @pytest.mark.parametrize(
        "key,value,status",
        (
            ["path", "Image", 201],
            ["path", "Image", 409],
            ["pah", "Image", 400]
        )
    )
    def test_create_folder(self, key, value, status):

        params = {
            key: value
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        assert response.status_code == status




