__author__ = 'alfmunny'

'''
Given an array of integers, every element appears twice except for one. Find that single one.
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        h_nums = set()
        for i in nums:
            if i not in h_nums:
                h_nums.add(i)
            else:
                h_nums.remove(i)

        return h_nums.pop()



