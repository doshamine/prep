class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(-1)

    def peek(self):
        return self.data[-1]

    def size(self) -> int:
        return len(self.data)
