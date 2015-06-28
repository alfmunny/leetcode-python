class Solution:
    # @param n, an integer
    # @return an integer
    def __init__(self):
        pass

    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res += ((n >> i) % 2) * 2 ** (31 - i)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.reverseBits(43261590433)
    print s.reverseBits(23131231231231)
    print s.reverseBits(485943238912832341321)

