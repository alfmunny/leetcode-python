class Solution:
	  # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    		sum = 0
    		for i in range(32):
    			sum += ((n>>i)%2) * 2 ** (31-i)

    		return sum 


if __name__ == '__main__':
		s = Solution()
		print s.reverseBits(43261596)

