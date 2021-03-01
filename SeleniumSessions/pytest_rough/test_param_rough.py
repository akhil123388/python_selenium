import pytest

@pytest.mark.parametrize("num,result", [(1,11), (2,22), (3,10)])
def test_calucualtion(num,result):
      assert num*11 == result
