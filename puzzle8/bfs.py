from .ffqueue import FFQueue
from .node import Node
from .utils import is_solved, get_available_paths, swap_tiles


def bfs(initial_state):
    if is_solved(initial_state):
        return tuple()

    frontier = FFQueue([Node(initial_state)])
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(node.value)
        for action in get_available_paths(node.value):
            value = swap_tiles(node.value, action)
            child = Node(value, parent=node, context=action)
            if child.value not in explored and child not in frontier:
                if is_solved(child.value):
                    return tuple(n.context for n in child.get_path()[1:])
                frontier.add(child)
