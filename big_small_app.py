import pytest
import time

@pytest.mark.small
def test_1():
	time.sleep(0.1)
	assert "aaa" == "bbb"

@pytest.mark.small
def test_2():
	time.sleep(0.1)
	assert "bbb" == "bbb"

@pytest.mark.large
def test_3():
	time.sleep(10)
	assert "aaa" == "bbb"
