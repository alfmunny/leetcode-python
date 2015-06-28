class Solution:
    def __init__(self):
        pass

    def countPrimes(self, n):
        if n < 2:
            return 0
        sieve = [True] * n
        sieve[0] = False
        sieve[1] = False
        i = 2
        while i * i < n:
            if sieve[i]:
                j = i
                while i * j < n:
                    sieve[i * j] = False
                    j += 1
            i += 1
        return sum(sieve)

if '__main__' == __name__:
    s = Solution()
    for i in [10, 100, 1000, 10000, 100000]:
        print(s.countPrimes(i))
