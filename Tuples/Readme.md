### Tuples 

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

**Example:**
```Python
tuple1 = ( 1, 2, 3)

print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
```
**Output:**
```
( 1, 2, 3)
1
2
3
```

***'Note': You can't change values, So to update Convert tuple to list by using `list()` function and update as list then convert back to tuple using `tuple()` function.***

***Example:**
```
tuple1 = (1, 2)
list1 = list(tuple1)
# update the list
updated_tuple= tuple(list1)
```

you can use `len()`, `max()`, `min()` function also.
```Python
tuple1 = (1, 2, 3, 4)

print(len(tuple1)) # length 4
print(max(tuple1)) # maximum value = 4
print(min(tuple1)) # minimum value = 1
```
