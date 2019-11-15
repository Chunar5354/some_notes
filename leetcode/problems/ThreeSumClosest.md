## 解题

[题目链接](https://leetcode.com/problems/3sum-closest/)

和[Three Sum](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/ThreeSum.md)类似，不过是要找一个三个数的和与目标最接近的数组，直接暴力解法最容易：
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        t = float('inf')
        for i in range(len(nums) - 2):
            two_tar = target - nums[i]
            for j in range(i+1, len(nums)-1):
                tar_last = two_tar - nums[j]
                for k in nums[j+1:]:
                    dif = tar_last - k
                    # print([nums[i], nums[j], k], dif)
                    if dif == 0:
                        return target
                    if abs(dif) < abs(t):
                        t = dif
        return target - t
```
出乎意料的没有超时（超过了5%），这种方法没啥好说的，挨个遍历就完事了

比较快速的那些答案中，又是加上了一堆五花八门的判断条件，没有啥通用性可言

其实自己在思考更快速方法的时候，想到了排序再根据左右端点加一减一的这种方法，但是实际操作的时候不会写判断条件了，这次要记住，判断条件就是：
```python
while left < right:
    Dosomething
```

程序示例
```python
class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        result = [float('inf'), None]  
		
        for k in range(n-2):
            a = nums[k]
            left_pointer = k + 1   # 从k+1开始查找，因为前面的都出现过了
            right_pointer = n - 1
            # 注意判断条件
            while left_pointer < right_pointer:
                b, c = nums[left_pointer], nums[right_pointer]
                diff = abs(target - (a + b + c))

                if diff == 0:
                    # if the abs value == 0 just return target which is our sum
                    return target
                if a + b + c < target:
				    # increment left pointer by 1 to get high value
                    left_pointer += 1
                else:
				    # decrement right pointer by 1 to get low value
                    right_pointer -= 1
                # if diff is less than our current result then we update it with new value
				# in the result field we need two fields: 1. to store diff 2. to store the sum
                if diff < result[0]:
                    result[0], result[1] = diff, a + b + c

        return result[1]
```

思想就是先把原来的列表排序，然后两头加，要是结果偏大了，就将左端点左移（相当于取一个更小的元素），要是结果偏小了，
就将右端点右移（相当于取一个更大的元素）

### 结论

- 牢记左右端点这种问题的判断方法：`while l < r`

## 知识点

- Python中获取一个无穷大值
  - 1.`m = sys.maxsize`
  - 2.`m = float('inf')`
  
