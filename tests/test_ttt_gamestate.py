from src.ttt_gamestate import TTTGameState


def test_str():
    t0 = TTTGameState()
    assert str(t0) == ('[- - -]\n'
                       '[- - -] (X to move)\n'
                       '[- - -]')


def test_repr():
    t0 = TTTGameState()
    assert (repr(t0) == 'TTTGameState([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)')


def test_is_valid_state():
    t0 = TTTGameState([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    assert t0.is_valid_state()
    t1 = TTTGameState([0, 0, 0, 1, 1, 1, 2, 2, 2], 0)
    assert t1.is_valid_state()


def test_replace_with():
    t0 = TTTGameState([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    t1 = t0.replace_with(0, 1)
    assert t0 == TTTGameState([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    assert t1 == TTTGameState([1, 0, 0, 0, 0, 0, 0, 0, 0], 0)


def test_get_next_states():
    t0 = TTTGameState([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    list_t0 = t0.get_next_states()
    assert list_t0 == [TTTGameState([1, 0, 0, 0, 0, 0, 0, 0, 0], 1),
                       TTTGameState([0, 1, 0, 0, 0, 0, 0, 0, 0], 1),
                       TTTGameState([0, 0, 1, 0, 0, 0, 0, 0, 0], 1),
                       TTTGameState([0, 0, 0, 1, 0, 0, 0, 0, 0], 1),
                       TTTGameState([0, 0, 0, 0, 1, 0, 0, 0, 0], 1),
                       TTTGameState([0, 0, 0, 0, 0, 1, 0, 0, 0], 1),
                       TTTGameState([0, 0, 0, 0, 0, 0, 1, 0, 0], 1),
                       TTTGameState([0, 0, 0, 0, 0, 0, 0, 1, 0], 1),
                       TTTGameState([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)]
    t1 = TTTGameState([2, 0, 1, 0, 1, 0, 2, 0, 0], 0)
    list_t1 = t1.get_next_states()
    assert list_t1 == [TTTGameState([2, 1, 1, 0, 1, 0, 2, 0, 0], 1),
                       TTTGameState([2, 0, 1, 1, 1, 0, 2, 0, 0], 1),
                       TTTGameState([2, 0, 1, 0, 1, 1, 2, 0, 0], 1),
                       TTTGameState([2, 0, 1, 0, 1, 0, 2, 1, 0], 1),
                       TTTGameState([2, 0, 1, 0, 1, 0, 2, 0, 1], 1)]


def test_is_goal_state():
    t0 = TTTGameState()
    assert not t0.is_goal_state()
    t1 = TTTGameState([1, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    assert not t1.is_goal_state()
    t2 = TTTGameState([1, 2, 1,
                       1, 1, 2,
                       2, 1, 2], 1)
    assert t2.is_goal_state()
    t3 = TTTGameState([1, 2, 1,
                       2, 1, 2,
                       2, 1, 1], 1)
    assert t3.is_goal_state()
