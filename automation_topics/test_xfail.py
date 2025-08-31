import pytest
import sys

def test_str_join():
    s1 = "Python,Pytest and automation"
    l1 = [ "Python,Pytest", 'and', "automation"]
    l2 = [ "Python","Pytest and automation"]

    assert " ".join(l1)==s1

@pytest.mark.xfail(raises=TypeError ,reason="failing for known isssue ")
def test_str_index():
    letters ="abcdedfhfhffjsjfhjsfsfsfksaj"
    assert letters[100]

@pytest.mark.xfail(reason='failing on windows')
def test_str_add():
    letters ="abcd"
    num =1234
    assert letters + str(num) =="abcd1234"



