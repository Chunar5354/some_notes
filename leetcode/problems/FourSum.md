## 解题

[题目链接](https://leetcode.com/problems/4sum/)

基本承袭了[Three Sum](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/ThreeSum.md)的套路，用类似的左右端点方法就能解决，只不过多遍历了一次（因为多了一个数）：

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        # 排序很重要
        nums.sort()
        res_list = []
        for i in range(len(nums) - 3):
            tar3 = target - nums[i]
            for j in range(i+1, len(nums)-2):
                tar2 = tar3 - nums[j]
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    cur_l = nums[l]
                    cur_r = nums[r]
                    if cur_l + cur_r == tar2:
                        res = [nums[i], nums[j], cur_l, cur_r]
                        # 避免重复
                        if res not in res_list:
                            res_list.append(res)                      
                        l += 1
                        r -= 1
                    elif cur_l + cur_r > tar2:
                        r -= 1
                    else:
                        l += 1
        return res_list
```

当然这种近似暴力的解法速度不会很快（超过30%）

看了一个高分答案，思路清奇：
```python
class Solution:
    def fourSum(self, n: List[int], t:int) -> List[List[int]]:
        n.sort()
        if not n:
            return []
        length = len(n)
        posi = {j:i for i,j in enumerate(n)}
        # 用集合来储存结果，直接就可以避免重复
        # 不过注意集合里面不能放列表
        res = set()
        biggest = n[-1]
        
        for i in range(length-3):
            a = n[i]
            # 此时a是最小的，如果4倍的a都比目标t大的话，后面无论怎么加，结果都比t大，所以可以直接break
            if 4*a > t:
                break
            # a + 3*biggest是a和其他三个数能计算出的最大值，如果比t小的话，说明a不够大，要向后继续取
            if a + 3*biggest < t:
                continue
            for j in range(i+1,length-2):
                b = n[j]
                # 和上面一样的道理，如果最小值都比目标大，就没有计算的必要
                if a + 3*b > t:
                    break
                # 如果最大值比目标小，就向后取
                if a + b + 2*biggest < t:
                    continue
                for k in range(j+1,length-1):
                    c = n[k]
                    d = t - a - b - c
                    # d是目标与其他三个数的差值
                    # 如果d比最大的数还要大，说明c取小了，继续向后取
                    if d > biggest:
                        continue
                    # 如果d比当前最小的数c还要小，说明无论c怎么取，d都不会在列表中，直接break
                    if d < c:
                        break
                    if d in posi and posi[d] > k:
                        res.add((a,b,c,d))
        return res
```

他这个按边界条件来判断，能够省去很多的遍历，是个好思路

但有一个问题是，同样把这个边界条件的方法用到Three Sum中，就慢了很多，难道是因为Three Num的target始终为0？还是Three Num的测试比较多？

### 结论

- 1.排序之后根据边界条件来判断，如果不满足边界条件，那么之后的遍历都可以省略

- 2.使用set()集合来代替字典，能够避免出现重复的元素。但是要注意集合里面不能存放列表；而且似乎用集合会比列表加个判断`if element not in l`慢一些
