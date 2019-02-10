from collections import deque

from puzzle8.ffqueue import FFQueue


def test_can_create_FFQueue():
    q = FFQueue()
    assert q.queue == deque()
    assert q.refs == {}


def test_can_create_FFQueue_with_initial_state():
    initial_state = 'hello'
    q = FFQueue([initial_state])
    assert q.queue == deque([initial_state])
    assert q.refs == {initial_state: 1}


def test_can_add_item():
    q = FFQueue()
    q.add('hello')
    q.add('hello')
    assert q.queue == deque(['hello', 'hello'])
    assert q.refs == {'hello': 2}


def test_can_pop_item():
    q = FFQueue(['hello', 'hello'])
    value = q.pop()
    assert value == 'hello'
    assert q.queue == deque(['hello'])
    assert q.refs.get('hello') == 1

    value = q.pop()
    assert value == 'hello'
    assert q.refs.get('hello') is None


def test_can_get_queue_length():
    q = FFQueue(['hello', 'hello'])
    assert len(q) == 2


def test_can_check_if_queue_contains_value():
    q = FFQueue(['hello', 'hello'])
    assert 'hello' in q
    assert 'world' not in q
