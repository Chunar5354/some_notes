## Approach

[Problem link](https://leetcode.com/problems/tenth-line/)

- My approach

This problem can besolved by `awk` command.

```
awk 'NR == 10' file.txt
```

And we can also solve it by using `sed` in `cat`.

```
cat file.txt | sed -n 10p
```

`sed` is a command that can deal with texts.
