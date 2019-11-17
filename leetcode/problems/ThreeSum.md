## 解题

[题目链接](https://leetcode.com/problems/3sum/)

[Two Sum](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/TwoSum.md)的升级版，不光是数量升级，返回的结果也从只获取一个满足条件的数组变成了所有满足条件的数组，而且还不能重复

这道题还有一个解法是[Four Sum](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/FourSum.md)中的利用边界条件，很奇怪的是这种方法在Four Sum中很快，在这里却很慢，存疑？

首先自己想的是对每一个元素i，除去i后对剩下的列表做Two Sum的操作，target变成`-nums[i]`，对Two Sum稍加修改即可：
```python
class Solution:
    def __init__(self):
        self.res_list = []
    def twosum(self, sub_l, tar):
        d = []
        for j in sub_l:
            n = tar - j
            if j not in d:
                d.append(n)
            else:
                sub_list = [-tar, n, j]
                sub_list.sort()   # 根据排序来判断是否有重复
                if sub_list not in self.res_list:
                    self.res_list.append(sub_list)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums) - 2):
            tar = -nums[i]
            self.twosum(nums[i+1:], tar)
        return self.res_list
```
超时了，之后怎么也没想出更快的方法（有点苗头但没去试）

看了别人的答案，基本思想都是将整个列表分成正负两部分，然后就是各自的奇思妙想，都要加上一堆判断，如：
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        first_number = set()
        answers = []
        if len(nums) < 3:
            return []
        # 排序，也相当于把正负值分开了
        nums.sort()
        # 如果全为正或全为负就不会出现和为0
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        for first in range(len(nums) - 2):
            # 对于相同的数字没必要多次判断
            if first > 0 and nums[first] == nums[first-1]:
                continue
            # 只遍历前面的负值
            if nums[first] > 0:
                return answers
            low = first + 1
            high = len(nums) - 1
            while low < high:
                target = nums[first] + nums[low] + nums[high]
                # 如果target>0，说明正值大了，就往前找一个
                if target > 0:
                    high -=  1
                # 如果target<0，说明负值小了，就往后找一个
                elif target < 0:
                    low += 1
                # 如果target=0，记录结果，并继续往中间找
                else:
                    answers.append([nums[first],nums[low], nums[high]])
                    low += 1
                    high -=  1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1
        return answers
```

逻辑上面有些复杂

还有一种方法比较快：
```python
class Solution:
    def threeSum(self, nums):
        if not nums:
            return []

        res = []
        dic = {}
        # 记录每个数字的出现次数
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1

        if 0 in dic and dic[0] > 2:
            res.append([0,0,0])
        
        # 将正值和负值分开存放
        pos = []
        neg = []
        for n in dic:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)

        for p in pos:
            for n in neg:
                target = -(p + n)
                if target in dic:
                    if target == p and dic[p] > 1:
                        res.append([p, p, n])
                    elif target == n and dic[n] > 1:
                        res.append([n, n, p])
                    # 只添加在[n, p]这个区间之内的target，避免重复
                    elif target < p and target > n:
                        res.append([n, p, target])
        return res
```

最后一种方法逻辑上更清晰一些，使用字典来存储，运行的速度也比较快
