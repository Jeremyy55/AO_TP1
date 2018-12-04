from jer import domine, generate_from_domination


def test_true_domine():
    assert domine([2, 3, 4], [1, 2, 3]) == True


def test_false_domine():
    assert domine([2, 3, 4], [2, 4, 3]) == False


def test_generate_from_domination_3():
    assert generate_from_domination([2, 3, 4], [1, 2, 3]) == [
        [2, 2, 3], [1, 3, 3], [1, 2, 4]]
