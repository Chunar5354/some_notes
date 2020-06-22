## Approach

[Problem link](https://leetcode.com/problems/course-schedule/)

- My approach

To solve this problem, I create two dictonaries to store the relationship of the courses.

`dic_of_pre`: the key is course number, and the value is a list of the courses after the key.
`dic_of_num`: the key is course number, and the value is how many prepositive course does the key have.

So we can traverse `dic_of_num`, if current value is 0, means this course doesn't have prepositive course, we can take this course. 
And after taking this course, we can get the courses after current course from `dic_of_pre`. And reduce their values in `dic_of_num`. 
Do this until all the courses have been taken.

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        # Save the relationship in two dictionaries
        dic_of_pre = collections.defaultdict(list)
        dic_of_num = collections.defaultdict(int)
        for l in prerequisites:
            dic_of_num[l[0]] += 0
            for i in range(len(l)-1):
                dic_of_pre[l[i]] += [l[i+1]]
                dic_of_num[l[i+1]] += 1

        # A function to find available course
        def helper():
            for k in dic_of_num.keys():
                if dic_of_num[k] == 0:
                    # Clear current taking course from dic_of_num
                    dic_of_num.pop(k)
                    return k
            return None
        
        for i in range(numCourses):
            next_course = helper()
            # next_course == None means there is no available course
            if next_course == None:
                return False
            # If dic_of_num is empty, means all the courses are taken
            if not dic_of_num:
                return True
            # Because this prepositive course 'next_course' is taken, the courses after it can be released
            for n in dic_of_pre[next_course]:
                dic_of_num[n] -= 1
        
        return True
```
