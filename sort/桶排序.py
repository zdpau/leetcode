def bucketSort(nums,independent = False):
    # 选择一个最大的数
    max_num = max(nums)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0]*(max_num+1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in nums:
        bucket[i] += 1
#        print(bucket) 一般都是1，有几个重复的数字就为几

    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:# 相当于一共有max+1的空间，如果列表的下标就是所对应的数字
            for _ in range(bucket[j]): # 这里是考虑到有重复的数字，一般都是1，则只添加一个数字
                sort_nums.append(j)
    
    if independent:
        sort_nums.reverse() 
    return sort_nums

nums = [5,6,3,2,1,1,1]
print (bucketSort(nums, independent = True)) # 从小到大，从大到小设置independent就行
