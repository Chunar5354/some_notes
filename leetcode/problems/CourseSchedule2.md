## Approach

[Problem link](https://leetcode.com/problems/course-schedule-ii/)

- My approach

We can use the method like [](). See this problem as a graph, and save the relationship into two dictionaries.

Every time take the course which indegree(value in num_dic) is 0. Then reduce the indegree of the courses after current course(find from pre_dic).

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        # Save the relationship in two dictionaries
        pre_dic = collections.defaultdict(list)
        num_dic = collections.defaultdict(int)
        for l in prerequisites:
            pre_dic[l[1]] += [l[0]]
            num_dic[l[0]] += 1
            num_dic[l[1]] += 0
        
        # The function to find 0-indegree course
        def helper():
            for k in num_dic.keys():
                if num_dic[k] == 0:
                    num_dic.pop(k)
                    return k
            return None
        
        res = []
        # There may be some courses which don't appear in prerequisites, means they don't have relationship
        if len(num_dic) < numCourses:
            res = [i for i in range(numCourses) if i not in num_dic.keys()]
        for j in range(numCourses):
            curr_course = helper()
            if curr_course == None:
                return []
            res.append(curr_course)
            if not num_dic:
                return res
            for c in pre_dic[curr_course]:
                num_dic[c] -= 1
        
        return res
```
