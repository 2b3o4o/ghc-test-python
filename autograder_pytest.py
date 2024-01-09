import calc

def test_add():
    assert calc.add(2, 2) == 4

def test_add_poorly():
    """A literary reference only grasped by the world's greatest intellectuals. should fail!!"""
    assert calc.add(2, 2) == 5

def test_multiply():
    assert calc.multiply(-1, 3) == -3