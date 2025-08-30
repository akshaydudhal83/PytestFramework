import pytest
import sys
pytestmark = pytest.mark.skipif(sys.platform =="win32", reason='will only run on linux')
print(sys.version)
print (sys.version_info)
# here is the glitch when module level skip and function level skip is applied
# when module level skipif is applied and function level skip is present and if module level skipif satisfy the
# it will show the reason from the module level skip
# When module level skipif is present and and also function level skipif is present
# if both skipf if satisfy then it will show the fucntin level reason

cons=9/5
def cent_to_mm(cent=0):
    fah =(cent * cons)+32
    return fah
@pytest.mark.skip(reason="Skipped muddam")
def test_92929_case0():
    assert type(cons)== float
#@
# pytest.mark.skipif(sys.version_info >(3,11), reason='skipiff scenarios')
@pytest.mark.skipif(cent_to_mm()==32, reason='Default')
def test_case1():
    assert cent_to_mm()== 32

@pytest.mark.skipif(pytest.__version__>'8.4.11', reason='version test')
def test_case02():
    assert cent_to_mm(38) == 100.4