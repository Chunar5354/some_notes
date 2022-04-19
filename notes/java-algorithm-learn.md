# 刷题中学java语法

## 1.两数之和

[原题地址](https://leetcode-cn.com/problems/two-sum/)

### 解题代码

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target-nums[i])) {
                res[0] = map.get(target-nums[i]);
                res[1] = i;
                return res;
            }
            map.put(nums[i], i);
        }
        return res;
    }
}
```

### 相关知识

- 1.初始化变量

Java中初始化变量的基本形式为`类型 变量名 = new 初始化值`

在本题中初始化了数组和map：

```java
int[] res = new int[2];  // 普通数组初始化时必须带上长度
Map<Integer, Integer> map = new HashMap<>();
```

- 2.数组长度

获取数组长度通过`list.length`实现

- 3.map一些操作

向map中插入键值对：

```java
map.put(key, value);
```

根据键取值：

```java
value = map.get(key);
```

判断键是否在map中：

```java
map.containsKey(key);
```

## 2.两数相加

[原题地址](https://leetcode-cn.com/problems/add-two-numbers/)

### 解题代码

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0, curr = 0;
        ListNode root = new ListNode();
        ListNode n = root;

        while (l1 != null && l2 != null) {
            curr = l1.val + l2.val + carry;
            if (curr >= 10) {
                curr -= 10;
                carry = 1;
            } else {
                carry = 0;
            }
            ListNode currNode = new ListNode(curr);
            n.next = currNode;
            n = n.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        if (l1 != null) {
            while (l1 != null || carry > 0) {
                if (l1 != null) {
                    curr = l1.val + carry;
                    if (curr >= 10) {
                        curr -= 10;
                        carry = 1;
                    } else {
                        carry = 0;
                    }
                    l1 = l1.next;
                } else {
                    curr = carry;
                    carry = 0;
                }
                ListNode currNode = new ListNode(curr);
                n.next = currNode;
                n = n.next;
            }
        }

        if (l2 != null) {
            while (l2 != null || carry > 0) {
                if (l2 != null) {
                    curr = l2.val + carry;
                    if (curr >= 10) {
                        curr -= 10;
                        carry = 1;
                    } else {
                        carry = 0;
                    }
                    l2 = l2.next;
                } else {
                    curr = carry;
                    carry = 0;
                }
                ListNode currNode = new ListNode(curr);
                n.next = currNode;
                n = n.next;
            }
        }

        if (carry > 0) {
            ListNode currNode = new ListNode(carry);
            n.next = currNode;
        }

        return root.next;
    }
}
```

### 相关知识

- 1.定义类时可以指定多种声明方式

如题目中给出的ListNode类，提供了三种声明方式，分别可以带上不同种类的参数

```java
ListNode() {}
ListNode(int val) { this.val = val; }
ListNode(int val, ListNode next) { this.val = val; this.next = next; }
```

- 2.局部变量需要初始化赋值，否则会报错

不能直接`int n`需要赋值`int n = 0`


## 3.无重复字符的最长子串

[原题地址](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

### 解题代码

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int res = 0, start = 0, currL = 0, i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                currL = i - start;
                start = Math.max(start, map.get(c)+1);
                if (currL > res) {
                    res = currL;
                }
            }
            map.put(c, i);
            i++;
        }
        // System.out.println(start);
        if (s.length() - start > res) {
            res = s.length() - start;
        }
        return res;
    }
}
```

### 相关知识

- 1.遍历字符串的方法

```java
char c = s.charAt(i);  // i是字符串中的索引
```

注意这里的c是`char`类型，如果用在声明map等变量时，应写为`Character`

还有一种常用的方法是先将字符串转换为char类型的数组：

```java
String s = "abcd";
char[] a = s.toCharArray();
for (char i:a) {  // i:a 是直接遍历数组元素的方法，类似于python的 for i in a
    System.out.println(i);
}
```

- 2.最大值最小值

```java
Math.max(a, b);
Math.min(a, b);
```


## 4.最长回文子串

[原题地址](https://leetcode-cn.com/problems/longest-palindromic-substring/)

### 解题代码

```java
class Solution {
    public String longestPalindrome(String s) {
        int l = s.length();
        if (l == 1) {
            return s;
        }
        String res = s.substring(0, 1);
        int maxL = 1, currL = 0;
        int[] index = new int[2];
        
        for (int i = 0; i < l; i++) {
            index = findPali(i, i+1, l, s);
            currL = index[1] - index[0] - 1;
            if (currL > maxL) {
                maxL = currL;
                res = s.substring(index[0]+1, index[1]);
            }

            index = findPali(i-1, i+1, l, s);
            currL = index[1] - index[0] - 1;
            if (currL > maxL) {
                maxL = currL;
                res = s.substring(index[0]+1, index[1]);
            }
        }
        return res;
    }

    static int[] findPali(int left, int right, int l, String s) {
        int[] res = new int[2];
        while (left >= 0 && right < l && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        res[0] = left;
        res[1] = right;
        return res;
    }
}
```

### 相关知识

- 1.java函数不能返回多个值，在需要返回多值的场景中可以使用数组或map等类型封装

- 2.定义函数的传参时每一个变量前面都要根类型：

```java
static int[] findPali(int left, int right, int l, String s) {}

static int[] findPali(int left, right, l, String s) {}  // 这样会报错
```

- 3.截取字符串

```java
s = 'abcd';
s.substring(start, end);
```


## 5.整数反转

[原题地址](https://leetcode-cn.com/problems/reverse-integer/)

### 解题代码

```java
class Solution {
    public int reverse(int x) {
        boolean negative = false, prev = true;
        if (x < 0) {
            negative = true;
            x = -x;
        }
        int ans = 0, maxN = (1 << 31) - 1, curr = 0, currMax = 0, i = 0;
        String s = Integer.toString(maxN), sOfX = Integer.toString(x);

        if (s.length() < sOfX.length()) {
            return 0;
        } else if (s.length() > sOfX.length()) {
            prev = false;
        }

        while (x > 0) {
            curr = x % 10;
            currMax = Integer.parseInt(s.substring(i, i+1));
            if (prev) {
                if (curr > currMax) {
                    return 0;
                } else if (curr < currMax) {
                    prev = false;
                } else {
                    prev = true;
                }
            }
            ans = ans*10 + curr;
            x = x / 10;
            i++;
        }
        if (negative) {
            ans = -ans;
        }
        return ans;
    }
}
```

### 相关知识

- 1.字符串与整数相互转换

```java
String s = Integer.toString(n);
n = Integer.parseInt(s);
```


## 6.回文数

[原题地址](https://leetcode-cn.com/problems/palindrome-number/)

#### 解题代码

```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        String s = Integer.toString(x);
        StringBuilder sb = new StringBuilder(s);
        // System.out.println(sb.getClass());
        String ns = sb.reverse().toString();

        if (s.equals(ns)) {
            return true;
        }
        return false;
    }
}
```

### 相关知识

- 1.反转字符串

需要借助`StringBuilder`类型的`reverse()`方法

```java
StringBuilder sb = new StringBuilder(s);
String rs = sb.reverse().toString();
```

- 2.获取变量类型

通过`getClass()`方法

```java
System.out.println(s.getClass());
```

## 7.最长公共前缀

[原题地址](https://leetcode-cn.com/problems/longest-common-prefix/)

### 解题代码

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String res = "", curr = "";
        // int l = 200;
        double l = Double.POSITIVE_INFINITY;
        for (String s : strs) {
            l = Math.min(l, s.length());
        }
        for (int i = 0; i < l; i++) {
            curr = strs[0].substring(0, i+1);
            for (String s : strs) {
                if (!curr.equals(s.substring(0, i+1))) {
                    return res;
                }
            }
            res = curr;
        }
        return res;
    }
}
```

### 相关知识

- 1.正无穷与负无穷

```java
double posInf = Double.POSITIVE_INFINITY;
double negInf = Double.NEGATIVE_INFINITY;
```

也可以用float类型实现

```java
float posInf = Float.POSITIVE_INFINITY;
float negInf = Float.NEGATIVE_INFINITY;
```

它们都可以与int类型直接比较

- 2.浮点数相关

java中的浮点数分为32位的单精度浮点数`float`与64为的双精度浮点数`double`

在声明变量时，如果声明float类型要在数字后面加上一个字母`F`，如果不加就默认是double类型：

```java
float a = 1.1F;
double b = 1.1;
```

在赋值时，将位数较低的变量赋给位数较高的变量时会自动隐式转换类型，反之则会报错：

```java
float a = 1.1F;  // 4字节
double b = 1.1;  // 8字节
int c = 1;       // 4字节
b = a;   // 可以
b = c;   // 可以
a = c;   // 可以
a = b;   // 报错
c = a;   // 报错
c = b;   // 报错
```

在进行计算时也会将结果隐式转换为`位数较高`的类型
