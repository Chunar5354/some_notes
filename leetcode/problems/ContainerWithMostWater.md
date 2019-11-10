## 解题

[题目链接](https://leetcode.com/problems/container-with-most-water/)

这道题的原理很容易搞清，就是一个`底乘高`，但是自己写了两个版本，全都超时了

优化方法的原理可以看一下官方给出的这个[视频](https://leetcode.com/problems/container-with-most-water/solution/)，非常生动形象

思路大致为：
- 首先从两个端点开始计算，保存结果
- 然后将其中数值较大的那一个端点保留，取数值较小的点的下一个点继续进行计算
  - 因为类似于`木桶效应`的问题要取最短的一根计算容积，那么对于短的那一根来说，肯定是与它`距离最远`的点计算出来的容积是最大的，中间的那些点可以省略
- 依次逐个点进行计算，直到两个端点相遇

算法实现：
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_res = 0
        # l为左端点，r为右端点
        l = 0
        r = len(height) - 1
        while l < r:
            #3 取其中数值小的一个计算容积，并取数值较小点的下一个点继续计算
            if height[l] < height[r]:
                max_res = max(max_res, height[l] * (r - l))
                l += 1
            else:
                max_res = max(max_res, height[r] * (r - l))
                r -= 1
            
        return max_res
```

### 结论

- 1.多思考问题的本质，尽量减少遍历的次数
- 2.别再使用像：
```python
max_a = 0
if a > max_a:
    max_a = a
```
这种取最大值的方法了，直接`max(max_a, a)`多简洁
