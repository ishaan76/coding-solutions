# test-if-tuple-is-distinct

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T09:47:39.355Z  

```py
arr = tuple(map(int, input().split()))

# code here
print("True" if len(arr)==len(set(arr)) else "False")

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/test-if-tuple-is-distinct/1)