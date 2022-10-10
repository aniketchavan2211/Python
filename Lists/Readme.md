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

### 

#### Check Datatype

From Python's perspective, lists are defined as objects with the data type 'list':

`<class 'list'>`
**Example:**

What is the data type of a list?
```python
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
```
**Output:**
```
<class 'list'>
```

#### The list() Constructor

It is also possible to use the `list()` constructor when creating a new list.

**Example:**

Using the `list()` constructor to make a List:
```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```
**Output:**
```
['apple', 'banana', 'cherry']
```

#### Slicing 

You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

**Example:**
```python
list = ["abc", "def", "ghi", "jkl", "mno"]
print(list[1:3])
```
**Output:**
```
["def", "ghi"]
```


***`Note`: The search will start at index 1 (included) and end at index 3 (not included).***

***Remember that the first item has index 0.***

#### Append Items

To add an item to the end of the list, use the append() method:

**Example:**
Using the `append()` method to append an item:
```python
list = ["apple", "banana", "cherry"]
list.append("orange")
print(list)
```
**Output:**
```
['apple', 'banana', 'cherry', 'orange']
```

#### Insert Items

To insert a list item at a specified index, use the `insert()` method.

The `insert()` method inserts an item at the specified index:

**Example:**
Insert an item as the second position:
```python
list = ["apple", "banana", "cherry"]
list.insert(1, "orange")
print(list)
```
**Output
```
['apple', 'orange', 'banana', 'cherry']
```

***`Note`: As a result of the examples above, the lists will now contain 4 items.***

#### Remove 

The `remove()` method removes the specified item.
**Example:**
```python
list = ['a', 'b', 'c',]
list.remove('b')
print(list)
```
**Output:**
```
['a', 'c']
```

#### Pop 

If you do not specify the index, the `pop()` method removes the last item.

**Example**python
```
list = ["a", "b", "c"]
list.pop()
print(list)
```
**Output:**
```
["a", "b"]
```

#### To delete complete list

The `del` keyword can also delete the list completely.

**Example:**
```python
list = ["a", "b", "c"]
del list
```

#### Clear list

The `clear()` method empties the list.

The list still remains, but it has no content.

**Example:**
```
list = ["a", "b", "c"]
list.clear()
print(list)
```
**Output:**
```
[]
```

#### Adding elements to lists

```python
print(list + ["x", "y", "z"])
```

#### Join lists

**Example:**
```python
list1 = ['a', 'b']
list2 = ['c', 'd']

list3 = list1 + list2
print(list3)
```
**Output:**
```
['a', 'b', 'c', 'd']
```

#### Minimum & Maximum

```Python
list1 = ['a', 'b', 'z']
list2 = ['1', '2', '9']

print(max(list))
print(max(list))

print(min(list))
print(min(list))
```
**Output:**
```
a
z

1
9
```

#### lists methods

Python has a set of built-in methods that you can use on lists.

| Method |	Description |
| ------ | ------------ |
| `append()` | Adds an element at the end of the list |
| `clear()` |	Removes all the elements from the list |
| `copy()` |	Returns a copy of the list |
| `count()`	| Returns the number of elements with the specified value |
| `extend()` |	Add the elements of a list (or any iterable), to the end of the current list |
| `index()` |	Returns the index of the first element with the specified value |
| `insert()` |	Adds an element at the specified position |
| `pop()` | Removes the element at the specified position |
| `remove()` |	Removes the item with the specified value |
| `reverse()` |	Reverses the order of the list |
| `sort()` | Sorts the list |
