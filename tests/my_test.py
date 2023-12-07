#import conf_test
from src.main import suma

def test_always_true():
    assert True

def test_suma():
    result = suma(1, 4)
    assert result == 5