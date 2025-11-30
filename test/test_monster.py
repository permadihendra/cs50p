from data.monster import get_monster


def test_get_monster():
    data = get_monster()
    assert isinstance(data, dict)


def test_is_monster_str():
    data = get_monster()
    if data is not None:
        assert isinstance(data["name"], str)
