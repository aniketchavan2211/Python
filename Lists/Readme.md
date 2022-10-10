### Lists

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
```Python
list = [ 'value1', value2, 1]
```

#### Indexing items

list first items are indexed at `[0]` index, second `[1]`, etc.

**Example:**
```Python
list1 = ["a", "b", "c"]
print (list1[0])
print (list1[1])
print (list1[2])
```
**Output:**
```
a
b
c
```

#### Negative Indexing

Negative indexing means start from the end

`-1` refers to the last item, `-2` refers to the second last item etc.

**Example:**
Print the last item of the list:
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```
**Output:**
```
cheery
```

#### Length

To determine how many items a list has, use the `len()` function:

**Example:**

Print the number of items in the list:
```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```
**Output:**
```
3
```
