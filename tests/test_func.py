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
