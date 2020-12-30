## 460. LFU Cache

[Problem link](https://leetcode.com/problems/lfu-cache/)

- My approach

Use two dictionaries to store the frequency, `k_f{key: frequenvy}` and `f_k{frequency: {key1, key2 ...}`, and a list `lru`, when a key is recelently used, put it at the end of lru.

When putting keys, check if the data is larger than capacity, if yes, find the smallest frequency in f_k. If there are more than one keys in f_k[min_freq], find the first key 
in lru, delete it. Then add the frequency of current key, and put current key at the end of lru.

When getting keys, ckeck if the key is in data, then add the frequency and modify lru.

```python
class LFUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.cap = capacity
        self.k_f = collections.defaultdict(int)
        self.f_k = collections.defaultdict(set)
        self.lru = []
        

    def get(self, key: int) -> int:
        if key in self.data:
            if key in self.k_f:
                last_frep = self.k_f[key]
                self.f_k[last_frep].remove(key)
                if not self.f_k[last_frep]:
                    self.f_k.pop(last_frep)
                for i in range(len(self.lru)):
                    if self.lru[i] == key:
                        self.lru.pop(i)
                        break
            self.k_f[key] += 1
            self.f_k[self.k_f[key]].add(key)
            self.lru.append(key)
        
        if key in self.data:
            return self.data[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        self.data[key] = value
        
        if len(self.data) > self.cap:
            min_freq = min(self.f_k.keys())
            for i in range(len(self.lru)):
                k = self.lru[i]
                
                if k in self.f_k[min_freq]:
                    self.f_k[min_freq].remove(k)
                    if not self.f_k[min_freq]:
                        self.f_k.pop(min_freq)
                    self.k_f.pop(k)
                    self.data.pop(k)
                    self.lru.pop(i)
                    break
        
        if key in self.k_f:
            last_frep = self.k_f[key]
            self.f_k[last_frep].remove(key)
            for i in range(len(self.lru)):
                if self.lru[i] == key:
                    self.lru.pop(i)
                    break
        self.k_f[key] += 1
        self.f_k[self.k_f[key]].add(key)
        self.lru.append(key)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

All the operations in this solution use original data structure, so it runs very slowly.


- Other's approach

```python
class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        
class LFUCache:

    def __init__(self, cap: int):
        self.freq = defaultdict(OrderedDict) 
        self.d = {}
        self.minfreq = -1
        self.cap = cap

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        n = self.d[key]
        od = self.freq[n.freq]
        del od[key]
        if not od and self.minfreq == n.freq:
            self.minfreq += 1
        n.freq += 1
        od = self.freq[n.freq]
        od[key] = n
        return n.value

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.d[key].value = value
            return
        if self.cap == 0:
            return
        if len(self.d) == self.cap:
            od = self.freq[self.minfreq]
            k, v = od.popitem(last=False)
            del self.d[k]
        n = Node(value, 1)
        self.d[key] = n
        self.freq[1][key] = n
        self.minfreq = 1
```
