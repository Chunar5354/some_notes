## 解题

[题目链接](https://leetcode.com/problems/two-sum/)

第一次在LeetCode刷题，上来就hardcode了一个：
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = []
        for i in range(len(nums)):
            first_num = nums[i]
            for j in range(len(nums)):
                if j != i:
                    if first_num + nums[j] == target:
                        return_list.append(i)
                        return_list.append(j)
                        return return_list
                    else:
                        pass
```

少量数据测试的时候完全没问题（甚至还最短），但是submit的时候就超时了

第二次用了`enumerate()`函数，成功通过了，但成绩不太理想：
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, fir in enumerate(nums):
            sec = target - fir
            if sec in nums and nums.index(sec) != i:
                return [i, nums.index(sec)]
            else:
                pass
```

问题应该是出在了多次进行的`index()`查找索引值上

最后看了别人的solutions，最快的方法是使用hash表（Python中的dict）：
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
```

### 结论

对于这种需要查找索引值以及数值的问题，在数据量大的情况下，应该优先考虑使用类字典的存储方式

## 知识点

hashmap：java中的一种数据结构，可类比于python中的字典结构

hashmap中元素的存储位置是由key的hashcode和hashmap的长度计算出来的[参考](https://zhuanlan.zhihu.com/p/31610616)

hashmap的扩展长度必须是2的n次方（为计算存储位置考虑）

- 区别：
    - 1.hashmap的初始长度，在java中是16，python中是8
    - 1.在java中，hashmap的结构是`数组+链表`，当存在冲突的时候，会将新元素存放在该地址对应的链表中的下一个结点；在python中使用的
    是开放寻址法[参考](https://www.cnblogs.com/lianzhilei/p/9275115.html)，存在冲突时会继续向下扩展存储单元，找到新的合适地址
