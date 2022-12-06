import pytest
from Zadanie_1.MethodsCode import show_csv,avg_age

def test_wrong_age():
    with pytest.raises(ZeroDivisionError):
        assert avg_age()

def show_error():
    with pytest.raises(FileNotFoundError):
        assert show_csv()