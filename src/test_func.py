# pytest -s -v src/test_func.py --alluredir=results
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
