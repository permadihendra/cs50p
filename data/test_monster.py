from monster import get_monster


def test_get_monster():
    data = get_monster()
    assert isinstance(data, dict)
