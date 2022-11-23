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


# test_func.py
import pytest 
from src.func import to_roman, NonValidInput

class TestTasksSuite:
    @pytest.mark.parametrize('value, result', [
        (9, 'IX'), (36, 'XXXVI'), (164, 'CLXIV'), (2380, 'MMCCCLXXX')
    ])
    def test_to_roman_pos(self, value, result):
        """Позитивные тест-кейсы."""
        assert to_roman(value) == result

    @pytest.mark.parametrize('value', ['-1', [], {}, set(), -1, 0, 5001])
    def test_to_roman_neg(self, value):
        """Негативные тест-кейсы."""
        with pytest.raises(NonValidInput):
            to_roman(value)

if __name__ == '__main__': 
    pytest.main()
