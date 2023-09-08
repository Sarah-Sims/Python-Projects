from working import convert
import pytest

def main():
   test_wrong_format()
   test_time()
   test_wrong_hour()
   test_wrong_min()

def test_wrong_format():
    with pytest.raises(ValueError):
        convert(r'9 AM - 9 PM')

def test_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert(r'17 AM to 14 PM')

def test_wrong_min():
      with pytest.raises(ValueError):
        convert(r'9 AM to 1:99 PM')

