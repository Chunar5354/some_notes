## Approach

[Problem link](https://leetcode.com/problems/valid-phone-numbers/)

- My approach

To search valid content from files, we can use `grep`(global regular expression print) command.

Here we use `perl regular expression`, which is `-P` in grep.

```
grep '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
```

`^` means start, `$` means the end.

`\d{3}` means three digitals.

`|` means or.
