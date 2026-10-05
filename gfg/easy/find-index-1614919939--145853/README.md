# Find index

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a tuple  **arr**  with distinct elements and an integer  **x**, find the index position of  **x**. Assume to have  **x** in the tuple always. Print the index (0-based).

 **Examples:** 

```
Input: arr = (1, 2, 3, 4, 5), x = 3
Output: 2
```

```
Input: arr = (3, 2, 1, 5, 4), x = 5
Output: 3
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T19:24:31.015Z  

```py
arr = tuple(map(int, input().split()))
x = int(input())

##we have been given the index value and we hae=ve to tell which value is there on that
#index value
print(arr.index(x))

#bas arr ka index value nikala

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-index-1614919939--145853/1)