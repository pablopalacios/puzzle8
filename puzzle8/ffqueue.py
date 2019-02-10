from collections import deque


class FFQueue:
    """Fast and Fat Queue.

    O(1) for insert/remove/search operations but may have the double
    size of a simple queue.
    """

    def __init__(self, initial_state=None):
        self.queue = deque()
        self.refs = dict()
        if initial_state:
            self._set_initial_state(initial_state)

    def add(self, elm):
        self.queue.append(elm)
        self.refs[elm] = self.refs.get(elm, 0) + 1

    def pop(self):
        elm = self.queue.popleft()
        self.refs[elm] = self.refs.get(elm) - 1
        if not self.refs[elm]:
            del self.refs[elm]
        return elm

    def __len__(self):
        return len(self.queue)

    def __contains__(self, elm):
        return elm in self.refs

    def _set_initial_state(self, initial_state):
        for value in initial_state:
            self.add(value)
