__author__ = 'alfmunny'

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

# Solution 1:
# When the array is sorted, then the middle one is always the answer
class Solution_1:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)/2]

# Solution 2:
# use Moore's voting algorithm
class Solution_2:
    def majorityElement(self, nums):
        count = 0
        element = nums[0]
        for i in range(len(nums)):
            if element == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                element = nums[i]
                count = 1
        return  element