from stars2.set_coll import set_
import pytest

@pytest.fixture
def coll():
    return {"a": {"b": {"c": 3}}}

def test_set_same(coll):
    assert set_(coll,["a", "b", "c"], 4) == {'a': {'b': {'c': 4}}}

def test_set_another(coll):
    assert set_(coll,['x', 'y', 'z'], 5) == {'a': {'b': {'c': 3}}, 'x': {'y': {'z': 5}}}


