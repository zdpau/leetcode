# 问题描述：给定一个排好序的数组nums，就地删除重复项，使每个元素只出现一次并返回新的长度。Given nums = [1,1,2]，返回length = 2,[1,2]\
#         Given nums = [0,0,1,1,1,2,2,3,3,4], Your function should return length = 5, [0,1,2,3,4]


# 这道题要我们从有序数组中去除重复项，和之前那道 Remove Duplicates from Sorted List 移除有序链表中的重复项 的题很类似，但是要简单一些，
# 因为毕竟数组的值可以通过下标直接访问，而链表不行。
# 那么这道题的解题思路是，我们使用快慢指针来记录遍历的坐标，最开始时两个指针都指向第一个数字，如果两个指针指的数字相同，则快指针向前走一步，
# 如果不同，则两个指针都向前走一步，这样当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数，

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
