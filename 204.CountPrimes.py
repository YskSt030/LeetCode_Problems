class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        k = math.sqrt(n)
        primes = list(range(2,n))
        print(primes)
        i = 0
        while primes[i] < k:
            count = 2
            base = primes[i]
            while True:
                if base * count in primes:            
                    primes.remove(base * count)
                count += 1
                if base * count > n - 1:
                    break
            i += 1       

        
        return len(primes)

if __name__ == '__main__':
    sol = Solution()
    n = 10
    print(sol.countPrimes(n))