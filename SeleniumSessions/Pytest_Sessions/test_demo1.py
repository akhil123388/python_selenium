import pytest
@pytest.mark.login
def test_m1():
    a=3
    b=4
    assert a+1 == b ,"test passed"
    assert a == b,  "test is failed a is not equal to b"
def test_m2():
    name = "Selenium"
    assert name.upper()== "SElENIUM"

@pytest.mark.login
def test_m3():
    assert True
def test_m4():
    assert False
@pytest.mark.login
def test_m5():
    assert 100 == 100
def test_m6():
    assert "naveen" == "NAVEEN"
