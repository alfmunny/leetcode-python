__author__ = 'alfmunny'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        head = 0
        tail = len(nums) - 1
        while head < tail:
            mid = int((head + tail) / 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                head = mid + 1
            elif target < nums[mid]:
                tail = mid - 1

        if target > nums[head]:
            return head + 1
        else:
            return head

s = Solution()
n = [1, 3, 5, 7, 9]
print s.searchInsert(n, 0)
