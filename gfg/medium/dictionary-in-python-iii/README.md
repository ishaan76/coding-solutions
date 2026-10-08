# dictionary-in-python-iii

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T14:04:41.584Z  

```py
# # insert into dictionary
# def insert_dict(query, dict):
#     # Your code here

# # deleting from dictionary
# def del_dict(query, dict):
#     # Your code here
    
# # print marks of required name
# def print_dict(key, dict):
#     # Your code here
def insert_dict(query, dict):
    dict[query[1]] = int(query[2])
    return "Inserted"

    # deleting from dictionary
def del_dict(query, dict):
       del dict[query[1]]
       return "Deleted"

    # print marks of required name
def print_dict(key, dict):
    if key in dict:
        print(f"Marks of {key} is {dict[key]}")
    else:
        print(-1)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/dictionary-in-python-iii/1)