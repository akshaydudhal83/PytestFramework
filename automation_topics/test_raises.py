
import pytest
def func1():
    raise ValueError("Exception is raised")
def test_case0():
    with pytest.raises(Exception) as excinfo:
        func1()

    print(str(excinfo.value))
    assert str(excinfo.value) == "Exception is raised"
