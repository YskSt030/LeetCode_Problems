class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.p = list(range(combinationLength))
        self.N = len(characters)
        self.Last = list(range(self.N - combinationLength, self.N))
        debug = 1
    def next(self) -> str:
        pass

    def hasNext(self) -> bool:
        pass
if __name__=='__main__':
    sol = CombinationIterator('abcde',2)
    sol.hasNext()
    
