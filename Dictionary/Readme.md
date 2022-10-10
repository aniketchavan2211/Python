### Dictionary 

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

**Example:**
```Python
dict_name = {
  "key1" : "value1",
  "key2" : 1,
}

print(dict_name('key1')) # prints value1
print(dict_name.keys()) # prints all keys
print(dict_name.values()) # prints all values
```
**Output:**
```
value1
{ "key1", "key2" }
{ 'value1', 1}
```


Dictionaries cannot have two items with the same key:

#### Adding Items

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

**Example:**
```
dict = { "key1" : "value1", "key2" : "value2", }
dict["key3"] = "value3"
print(dict)
```
**Output:**
```
{ "key1" : "value1", "key2" : "value2", "key3" : "value3",}
```

#### Updating 

The `update()` method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

**Example:**
```Python
dict_name.update({'key1' : 'val'})
print(dict_name[key1])
```
**Output:**
```
val
```

#### Removing Items

There are several methods to remove items from a dictionary:

The `pop()` method removes the item with the specified key name:
**Example:**
```
dict.pop("key")
```

The del keyword removes the item with the specified key name:
**Example:**
```
del dict["key"]
```

The `del` keyword can also delete the dictionary completely:
**Example:**
```
del dict
```

The `clear()` method empties the dictionary:
**Example:**
```
dict.clear()
```

#### Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

| Method | Description |
| ------ | ----------- |
| `clear()` |	Removes all the elements from the dictionary |
| `copy()` | Returns a copy of the dictionary |
| `fromkeys()` |	Returns a dictionary with the specified keys and value |
| `get()`	| Returns the value of the specified key |
| `items()` |	Returns a list containing a tuple for each key value pair |
| `keys()` |	Returns a list containing the dictionary's keys |
| `pop()` |	Removes the element with the specified key
| `popitem()`	| Removes the last inserted key-value pair
| `setdefault()` | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| `update()` |	Updates the dictionary with the specified key-value pairs |
| `values()` |	Returns a list of all the values in the dictionary |
