import pytest


@pytest.fixture(
    scope='function',
    params=[(9, 'IX'), (36, 'XXXVI'), (164, 'CLXIV'), (2380, 'MMCCCLXXX')],
    ids=lambda args: f"Test with args: {args}"
)
def parametrize_to_roman(request):
    """Параметризатор для позитивных тест-кейсов."""
    return request.param


@pytest.fixture(
    scope='function',
    params=['-1', [], {}, set(), -1, 0, 5001],
    ids=lambda args: f"Test with args: {args}"
)
def parametrize_to_roman_neg(request):
    """Параметризатор для негативных тест-кейсов."""
    return request.param
