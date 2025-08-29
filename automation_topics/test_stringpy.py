import pytest

pytestmark =[pytest.mark.moduelwise,pytest.mark.testwise]
# ---------- String Slicing ----------
def test_str_slice():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[:] == letters  # full slice
    assert letters[10:] == "klmnopqrstuvwxyz"  # from index
    assert letters[-3:] == "xyz"  # from negative index
    assert letters[:10:5] == "af"  # step slice

# this is test
# ---------- String Split ----------
def test_str_split():
    text = "one two three four"
    assert text.split() == ["one", "two", "three", "four"]  # default split by space
    assert text.split(" ", 2) == ["one", "two", "three four"]  # maxsplit
    csv = "a,b,c,d"
    assert csv.split(",") == ["a", "b", "c", "d"]


# ---------- String Join ----------
def test_str_join():
    words = ["a", "b", "c"]
    assert "-".join(words) == "a-b-c"
    assert "".join(words) == "abc"
    assert " ".join(words) == "a b c"


# ---------- String Strip ----------
def test_str_strip():
    word = "   hello   "
    assert word.strip() == "hello"
    assert word.lstrip() == "hello   "
    assert word.rstrip() == "   hello"


# ---------- String Find & Index ----------
@pytest.mark.checks
def test_str_find_index():
    text = "hello world"
    assert text.find("world") == 6
    assert text.find("xyz") == -1
    assert text.index("hello") == 0
    with pytest.raises(ValueError):
        text.index("notfound")  # raises error


# ---------- String Replace ----------
def test_str_replace():
    text = "one one two three"
    assert text.replace("one", "1") == "1 1 two three"
    assert text.replace("one", "1", 1) == "1 one two three"  # only once


# ---------- String Upper / Lower / Title ----------
def test_str_case():
    text = "hello world"
    assert text.upper() == "HELLO WORLD"
    assert text.lower() == "hello world"
    assert text.title() == "Hello World"
    assert text.capitalize() == "Hello world"


# ---------- String Start / End ----------
def test_str_start_end():
    text = "pytest is great"
    assert text.startswith("pytest")
    assert text.endswith("great")
    assert not text.startswith("unit")


# ---------- String Contains ----------
@pytest.mark.sanity
@pytest.mark.sanity11
def test_str_contains():
    text = "automation testing"
    assert "auto" in text
    assert "xyz" not in text


# ---------- String Formatting ----------
@pytest.mark.sanity
def test_str_format():
    assert "{} + {} = {}".format(2, 3, 5) == "2 + 3 = 5"
    assert f"{2} + {3} = {5}" == "2 + 3 = 5"


# ---------- String Count ----------
@pytest.mark.sanity
def test_str_count():
    text = "banana"
    assert text.count("a") == 3
    assert text.count("na") == 2

def test_str_count11():
    pass

    s1 = "Python,Pytest and automation"
    l1 = [ "Python,Pytest", 'and', "automation"]
    l2 = [ "Python","Pytest and automation"]
