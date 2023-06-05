class MinStack:
    def __init__(self):
        self.stack = []
        self.minarr = []
        self.topvar = -1
    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append(val)
            self.topvar += 1
            self.minarr.append(self.topvar)
        else:
            self.stack.append(val)
            self.topvar += 1
            if val < self.stack[self.minarr[-1]]:
                self.minarr.append(self.topvar)
    def pop(self) -> None:
        if self.stack != []:
            a = self.stack.pop()
            if(self.minarr[-1] == self.topvar):
                self.minarr.pop()
            self.topvar -= 1
    def top(self) -> int:
        if self.stack != []:
            return self.stack[self.topvar]
    def getMin(self) -> int:
        return self.stack[self.minarr[-1]] 

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()