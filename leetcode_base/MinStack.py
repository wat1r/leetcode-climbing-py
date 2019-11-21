class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if self.stack:
            self.helper.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]
