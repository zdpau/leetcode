from __future__ import print_function
# Time:  O(n)
# Space: O(1)
#
# Given an array and a value, remove all instances of that value in place and return the new length.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# 定义两个指针，一个从-1开始，一个从0开始，依次遍历。

class Solution:
    # @param    A       a list of integers　列表
    # @param    elem    an integer, value need to be removed　需要删除的那个数
    # @return an integer
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = -1
        for i in xrange(0, len(nums)):
            if nums[i] != val:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1
