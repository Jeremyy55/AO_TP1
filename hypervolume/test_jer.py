from jer import domine


def test_true_domine():
    assert domine((2, 3, 4), (1, 2, 3)) == True


def test_false_domine():
    assert domine((2, 3, 4), (2, 4, 3)) == False
