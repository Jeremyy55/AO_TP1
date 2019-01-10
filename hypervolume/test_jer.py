from jer import domine_max, domine_min, generate_from_domination


def test_true_domine_max():
    assert domine_max([2, 3, 4], [1, 2, 3]) == True


def test_true_domine_min():
    assert domine_min([1, 2, 3], [2, 3, 4]) == True


def test_false_domine_max():
    assert domine_max([2, 3, 4], [2, 4, 3]) == False


def test_false_domine_min():
    assert domine_min([2, 3, 4], [2, 4, 3]) == False


def test_equal_domine_max():
    assert domine_max([1, 2, 3, 4], [1, 2, 3, 4]) == False


def test_equal_domine_min():
    assert domine_min([1, 2, 3, 4], [1, 2, 3, 4]) == False


def test_generate_from_domination_3():
    assert generate_from_domination([2, 3, 4], [1, 2, 3]) == [
        [2, 2, 3], [1, 3, 3], [1, 2, 4]]
