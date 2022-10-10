### Sets 

Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable, ,unindexed and not allow duplicate values.

***`Note`: Set items are unchangeable, but you can remove items and add new items.***

Sets are written with curly brackets.

**Example:**
```Python
set = { 'value1', 'value2' }
```

***`Note`: Sets are unordered, so you cannot be sure in which order the items will appear***

#### length, type & set() constructor

```Python
set = { 'a', 'b', 'c', 'd', 'e' }
print(len(dict)

print(type(dict))

tuple = ("a", "b")
set = set(tuple)
print(set)
```
**Output:**
```
5

<class 'set'>

{ 'a',  'b' }
```

#### Access Items

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

**Example:**
Loop through the set, and print the values:
```python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```
**Output:**
```
banana
apple
cherry 
```

**Example:**
Check if "banana" is present in the set:
```python
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```
**Output:**
```
True
```

#### Add Items

To add one item to a set use the add() method.

**Example:**
Add an item to a set, using the `add()` method:
```python
set = {"apple", "banana", "cherry"}

set.add("orange")

print(set)
```
**Output:**
```
{'orange', 'banana', 'apple', 'cherry'}
```

#### Add Sets

To add items from another set into the current set, use the `update()` method.

**Example:**
Add elements from ``tropical` into `thisset`:
```python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
```
**Output:**
```
{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}
```

#### Add Any Iterable

The object in the `update()` method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

**Example:**
Add elements of a list to at set:
```python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
```
**Output:**
```
{'banana', 'cherry', 'apple', 'orange', 'kiwi'}
```

#### Remove Item

To remove an item in a set, use the `remove()`, or the `discard()` method.

**Example:**
```
set = { 'a', 'b', 'c'}

set.remove('b')
```

***`Note`: If the item to remove does not exist, remove() will raise an error.***

**Example:**
```
set.discard('b')
```

***`Note`: If the item to remove does not exist, `discard()` will NOT raise an error.***


You can also use the `pop()` method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the `pop()` method is the removed item.

**Example:**
```
set.pop()
```

***`Note`: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.***

The `clear()`  Method empties the set:
```
set.clear()
```

The `del` keyword will delete the set completely:
```
del set
```

#### Set Methods

Python has a set of built-in methods that you can use on sets.

| Method | Description |
| ------ | ----------- |
| `add()` |	Adds an element to the set |
| `clear()`	| Removes all the elements from the set |
| `copy()` |	Returns a copy of the set |
`difference()` |	Returns a set containing the difference between two or more sets |
`difference_update()`	| Removes the items in this set that are also included in another, specified set
`discard()`	Remove the specified item |
| `intersection()` |	Returns a set, that is the intersection of two other sets |
`intersection_update()` |	Removes the items in this set that are not present in other, specified set(s) |
| `isdisjoint()` | Returns whether two sets have a intersection or not |
| `issubset()` | Returns whether another set contains this set or not |
| `issuperset()` | Returns whether this set contains another set or not |
| `pop() | Removes an element from the set |
| `remove()` | Removes the specified element |
| `symmetric_difference()` | Returns a set with the symmetric differences of two sets |
| `symmetric_difference_update()`	| inserts the symmetric differences from this set and another |
| `union()` |	Return a set containing the union of sets |
| `update()` |	Update the set with the union of this set and others |
