class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0,nums[-1])
            nums.pop()

if __name__ == '__main__':
		s = Solution()
		a = [1, 2, 3, 4, 5, 6, 7]
		k = 3
		s.rotate(a,k)
		print a