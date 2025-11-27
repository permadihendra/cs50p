from monster import get_monster


def test_get_monster():
    data = get_monster()
    assert isinstance(data, dict)


def test_is_monster_int():
    data = get_monster()
    assert isinstance(data["name"], str)
