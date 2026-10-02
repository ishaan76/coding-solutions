# Print Square

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an integer  **n**, write a program to print the square of size  **n**  using "  *" character **.** 

 **Examples :** 

```
Input: n = 4
Output:
 **   ** 
 ** 
 ** 
 **   ** 
Explanation: It's a square! Each side contains n = 4.

```

```
Input: n = 3
Output:
 **  * 
 ** 
 **  *
Explanation: It's a square! Each side contains n = 3.
```

 **Constraints:** 
1 ≤ n ≤ 10

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T09:06:37.582Z  

```py

# code here
n = int(input())
for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "* ")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/print-square--105330/1)