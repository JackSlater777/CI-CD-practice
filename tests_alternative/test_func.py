import pytest
from src.func import to_roman, NonValidInput


class TestTasksSuite:
    def test_to_roman_pos(self, parametrize_to_roman):
        """Позитивные тест-кейсы."""
        data, result = parametrize_to_roman
        assert to_roman(data) == result

    def test_to_roman_neg(self, parametrize_to_roman_neg):
        """Негативные тест-кейсы."""
        data = parametrize_to_roman_neg
        with pytest.raises(NonValidInput):
            to_roman(data)


if __name__ == '__main__': 
    pytest.main()
