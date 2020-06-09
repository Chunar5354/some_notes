## Approach

[Problem link](https://leetcode.com/problems/transpose-file/)

- My approach

We can use `awk` command and write some codes in it.

```shell
awk '{ for (i=1; i<=NF; i++) {
            if (NR==1) s[i]=$i; 
            else s[i] = s[i] " " $i;
        }
     } END { for (i in s) print s[i] }' file.txt
```

Here `NF` is the number of lines, and `NR` is the index of every line, but start with 0.

For more details about NF and NR, please see [here](https://blog.csdn.net/a1414345/article/details/79071951).
