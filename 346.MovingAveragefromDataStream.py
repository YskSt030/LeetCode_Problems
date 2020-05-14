"""
Given a stream of integers and a window size, 
calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
 
"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.data = list()

    def next(self, val: int) -> float:
        self.data.append(val)
        if len(self.data) > self.size:
            self.data = self.data[1:]
        return sum(self.data) / len(self.data)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)