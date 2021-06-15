import pytest
import roman as ro

def test_parse_1():
    assert ro.parse("CCC") == True
def test_parse_2():
    assert ro.parse("XXX") == True
def test_parse_3():
    assert ro.parse("LL") == True
def test_parse_4():
    assert ro.parse("CCCC") == True