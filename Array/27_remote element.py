from __future__ import print_function
# Time:  O(n)
# Space: O(1)
#
# Given an array and a value, remove all instances of that value in place and return the new length.
# 给定数组nums和值val，在适当位置删除该值的所有实例并返回新长度。
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Given nums = [3,2,2,3], val = 3, Your function should return length = 2,[2,2]
# Given nums = [0,1,2,2,3,0,4,2], val = 2, Your function should return length = 5,[0,1,3,0,4]


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
        for i in range(0, len(nums)):
            if nums[i] != val:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1
