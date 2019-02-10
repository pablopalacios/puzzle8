from puzzle8.node import Node


def test_can_create_root_node():
    value = 42
    node = Node(value)
    assert node.value == value
    assert node.parent is None


def test_can_create_node():
    parent = Node(52)
    node = Node(42, parent)
    assert node.parent == parent
    assert node.value == 42


def test_can_get_path():
    root = Node(52)
    n1 = Node(42, root)
    n2 = Node(32, n1)
    n3 = Node(22, n2)
    path = n3.get_path()
    assert path == (root, n1, n2, n3)
