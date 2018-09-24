# 问题描述：给定一个排好序的数组nums，就地删除重复项，使每个元素只出现一次并返回新的长度。Given nums = [1,1,2]，返回length = 2,[1,2]\
            Given nums = [0,0,1,1,1,2,2,3,3,4], Your function should return length = 5, [0,1,2,3,4]

class Solution(object): 
    def removeDuplicates(self, nums): #跟上面那个差不多，也是定义两个指针，
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in xrange(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1
