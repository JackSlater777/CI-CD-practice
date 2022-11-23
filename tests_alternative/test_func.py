# Запуск через терминал
# pytest -s -v src/test_func.py
# -v - более детальный принт результата теста
# -s - отображение принтов внутри тестов
# --duration=int -vv - все тесты, прохождение которых займет более int секунд, будут отмечены, как slowest

# Для генерации файлов отчета allure
# pytest -s -v src/test_func.py --alluredir=results
# Не забыть добавить папку results в .gitignore
# Для отображения отчета в браузере в командной строке в папке с проектом
# allure serve results

import pytest 
from func import to_roman, NonValidInput


class TestTasksSuite:
    # Positive test case
    def test_to_roman_pos(self, parametrize_to_roman):
        data, result = parametrize_to_roman
        assert to_roman(data) == result

    # Negative test case
    def test_to_roman_neg(self, parametrize_to_roman_neg):
        data = parametrize_to_roman_neg
        with pytest.raises(NonValidInput):
            to_roman(data)


if __name__ == '__main__': 
    pytest.main()
