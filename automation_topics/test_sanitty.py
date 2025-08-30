def test_str_count11():
    s1 = "Python,Pytest ,and ,automation"
    l1 = ["Python,Pytest", 'and', "automation"]
    l2 = ["Python", "Pytest and automation"]
    print( " ".join(s1))
    print(" between ".join(l1))
    print(" joining ".join(l2))


test_str_count11()