# Написать функцию to_roman, которая принимает целое число, а возвращает строку, отображающую это число
# римскими цифрами. Например, на вход подается 6, возвращается - "VI"; на вход подается 23, возвращается
# "XXIII". Входные данные должны быть в диапазоне от 1 до 5000, если подается число не из этого диапазона,
# или не число, то должны выбрасываться ошибка типа NonValidInput. Этот тип ошибки надо создать отдельно. 
# Также необходимо в папке с файлом, содержащим вашу функцию, создать файл tests.py, внутри которой 
# необходимо определить тесты для вашей функции. Тесты должны покрывать все возможное поведение функции, 
# включая порождения ошибки при некорректных входных данных.

import pytest 
from lec_12_1 import to_roman, NonValidInput


class TestTasksSuite:
    # Фикстура и параметризатор для позитивного тестирования
    @pytest.fixture(
        scope='function',
        params=[(9, 'IX'), (36, 'XXXVI'), (164, 'CLXIV'), (2380, 'MMCCCLXXX')],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrize_to_roman(self, request):
        return request.param

    # Фикстура и параметризатор для негативного тестирования
    @pytest.fixture(
        scope='function',
        params=['-1', [], {}, set(), -1, 0, 5001],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrize_to_roman_neg(self, request):
        return request.param

    # Позитивный тест-кейс
    def test_to_roman_pos(self, parametrize_to_roman):
        data, result = parametrize_to_roman
        assert to_roman(data) == result

    # Негативный тест-кейс
    def test_is_prime_neg(self, parametrize_to_roman_neg):
        data = parametrize_to_roman_neg
        with pytest.raises(NonValidInput):
            to_roman(data)


if __name__ == '__main__': 
    pytest.main() 
