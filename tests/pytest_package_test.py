import pytest


def test_stupid_test():
    assert 1 == 1


def test_throws_stupid_test():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0 == 1


@pytest.mark.parametrize("num1, num2, expected_result", [
    (1, 2, 3),
    (5, 3, 8),
    pytest.param(1, 4, 6, marks=pytest.mark.xfail(reason="This test is expected to fail"))
])
def test_add(num1, num2, expected_result, monkeypatch):
    """
    This is unnecessary comant. Testing sum operator
    """
    assert num1 + num2 == expected_result
