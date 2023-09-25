import programm

def test_plusmal():
    assert programm.plusmal(2, 3) == (2 + 3) * 2
    assert programm.plusmal(0, 0) == (0 + 0) * 2
    assert programm.plusmal(-1, 1) == (-1 + 1) * 2

def test_unterschreiben():
    assert programm.unterschreiben("test") == "test_unterschrieben"
    assert programm.unterschreiben("") == "_unterschrieben"
    assert programm.unterschreiben("123") == "123_unterschrieben"

def test_kubieren():
    assert programm.kubieren(2) == 8
    assert programm.kubieren(3) == 27
    assert programm.kubieren(0) == 0
