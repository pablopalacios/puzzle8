from collections import deque


class Node:

    def __init__(self, value, parent=None, context=None):
        self.value = value
        self.parent = parent
        self.context = context

    def get_path(self):
        path = deque([self])
        parent = self.parent
        while parent is not None:
            path.appendleft(parent)
            parent = parent.parent
        return tuple(path)
