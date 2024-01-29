
'''
Runtime: O(n)，50.01%
Memory: O(n)，80.67%
'''
class MyQueue:

    def __init__(self):
        self.oldToNew = [] # empty in ususal
        self.newToOld = []

    def push(self, x: int) -> None:
        while self.newToOld:
            self.oldToNew.append(self.newToOld.pop())
        self.oldToNew.append(x)
        while self.oldToNew:
            self.newToOld.append(self.oldToNew.pop())

    def pop(self) -> int:
        return self.newToOld.pop()

    def peek(self) -> int:
        return self.newToOld[-1]

    def empty(self) -> bool:
        return not self.newToOld
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()