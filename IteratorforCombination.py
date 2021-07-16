class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.p = list(range(combinationLength))
        self.N = len(characters)
        self.Last = list(range(self.N - combinationLength, self.N))
        self.q = len(self.p) - 1

    def next(self) -> str:
        if self.p[self.q] < self.N - len(self.p) - self.q:
            self.p[self.q] += 1
        else:
            self.q -= 1 

    def hasNext(self) -> bool:
        return self.p == self.Last

if __name__=='__main__':
    sol = CombinationIterator('abcde',2)
    sol.hasNext()
    
