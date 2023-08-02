import pytest
from pyport.security import Security


def test_create_security():
    security_name = "AAPL"
    s = Security(security_name)
    assert s.name == security_name


def test_empty_security_name_raises():
    security_name = ""
    with pytest.raises(ValueError):
        Security(security_name)
