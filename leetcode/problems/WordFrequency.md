## Approach

[Problem link](https://leetcode.com/problems/word-frequency/)

- My approach

This is a problem of `bash`. I didn't know much about bash, this is a start of learning.

Here is one of the answers, I will split the code and show the feature of every part.

```
xargs -n1 < words.txt | sort | uniq -c | sort -r | awk '{print $2" "$1}'
```

For example, here is a file named `words.txt`:

```
the day is sunny the the
the sunny is is
```

Firstly, `xargs` can print the context of file `words.txt`.

```
$ xargs < words.txt
the day is sunny the the the sunny is is
```

And `-n1` can format the output as each line one word.

```
$ xargs -n1 < words.txt
the
day
is
sunny
the
the
the
sunny
is
is
```

Then `sort` can sort the output by alphabetical order.

```
$ xargs -n1 < words.txt | sort
day
is
is
is
sunny
sunny
the
the
the
the
```

And `uniq` will make every word appear once, `-c` will add the count of the word at the front of the word.

```
$ xargs -n1 < words.txt | sort | uniq -c
      1 day
      3 is
      2 sunny
      4 the
```

The second `sort` has a parameter `-r`, it will make the output by reverse order.

```
$ xargs -n1 < words.txt | sort | uniq -c | sort -r
      4 the
      3 is
      2 sunny
      1 day
```

Finally, `awk` will format every line. Here `'{print $2" "$1}'` means print the second element firstly, then add a whitespace between 
the two elements, finally print the first element.

```
$ xargs -n1 < words.txt | sort | uniq -c | sort -r | awk '{print $2" "$1}'
the 4
is 3
sunny 2
day 1
```

And this is the answer of this problem.
