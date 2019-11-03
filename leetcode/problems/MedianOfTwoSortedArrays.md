## 解题

[题目链接](https://leetcode.com/problems/median-of-two-sorted-arrays/)

上来一看题目中要求了时间复杂度是O(log(m+n))，着实捏了一把汗，按照自己的想法：拼接字典然后重新排序，竟然一试就通过了：
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            return (nums1[int(n/2)] + nums1[int(n/2 -1)]) / 2
        else:
            return nums1[int((n-1)/2)]
```

不过成绩还是很差，看了官方的答案，好复杂，要把两个列表分别拆分再比较，结果运行时间比我的还长

找了一个其他人的比较快的答案：
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_joined = sorted(nums1 + nums2)
        if len(sorted_joined) % 2 == 0:
            index = int(len(sorted_joined) / 2)
            return (sorted_joined[index] + sorted_joined[index-1])/2
        else:
            index = (int(len(sorted_joined)/2))
            return sorted_joined
```

和我的做法几乎一模一样，只是拼接两个列表的时候他使用的是`+`，我用的是`entend()`函数。（把我自己的方法改成`+`之后速度也上去了...）

### 结论

- 1.两个列表拼接的方法中，`extend()`函数会循环遍历列表2的每个元素，并依次添加到列表1的末尾，在列表长度很大的时候，速度就会降低，表现不如
直接使用`+`直接拼接
- 2.列表排序的方法中，`list.sort()`要比`list2 = sorted(list1)`速度更快，原因可能是`list.sort()`是对原列表进行修改，而`list2 = sorted(list1)`
方法则要生成一个新的列表，更加耗费资源

## 知识点

- 1.O(log n)的时间复杂度：常见于`二分法`，每次去总长的一半进行分割，对于长度为n的序列，要查找到某一元素需要进行 2<sup>k</sup> = n， 
k = log<sub>2</sub> n 
次操作。  [参考](https://juejin.im/entry/593f56528d6d810058a355f4)

