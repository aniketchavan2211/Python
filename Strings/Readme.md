### String

String in python are surrounded by either single quotation marks or double quotation marks.

`'hello'` is the same as `"hello"`

Assigning a string to a variable is done with the variable name followed by an equal sign and the string

```Python
a = "Hello"

print (a)
```
**Output:**
```
Hello
```

#### Multiline String

You can assign a multiline string to a variable by using three quotes:

```Python
a = """ This is a 
        Multi line 
        String """
```
OR three single quotes:
```Python
a = ''' Name 
        Age
        Number'''
print (a)
```
**Output**:
```
 Name
 Age 
 Number
```

#### Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

**Example:**
```Python
a = "Hello"
print(a)
```
Output:
```
Hello
```

#### Strings are Arrays

Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

**Example:**

Get the character at position 1 (remember that the first character has the position 0):

```py
a = "Hello, World!"
print(a[1])
```
**Output:**
```
e
```

#### Looping Through a String

Since strings are arrays, we can loop through the characters in a string, with a `for` loop.

**Example:**
Loop through the letters in the word "banana":

```py
for x in "banana":
  print(x)
```
**Output:**
```
b
a
n
a
n
a
```

#### String Length

To get the length of a string, use the `len()` function.

Example
The `len()` function returns the length of a string:

```python
a = "Hello, World!"
print(len(a))
```
**Output:**
```
13
```
#### Check String

To check if a certain phrase or character is present in a string, we can use the keyword `in`.

**Example:**

Check if `free` is present in the following text:

```py
txt = "The best things in life are free!"
print("free" in txt)
```
**Output:**
```
True
```

Use it in an `if` statement:

**Example:**

Print only if `free` is present:

```python
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
```

#### Check if NOT

To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.

**Example:**

Check if `expensive` is NOT present in the following text:

```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```
**Output:**
```
True
```

Use it in an `if` statement:

**Example:**

print only if "expensive" is NOT present:

```python
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```
**Output:**
```
No, 'expensive' is NOT present.
```

#### Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

**Example:**

Get the characters from position 2 to position 5 (not included):

```python
b = "Hello, World!"
print(b[2:5])
```
**Output:**
```
llo
```

***`Note`: The first character has index 0.***

#### Slice From the Start

By leaving out the start index, the range will start at the first character:

**Example:**

Get the characters from the start to position 5 (not included):

```python
b = "Hello, World!"
print(b[:5])
```
**Output:**
```
Hello
```

#### Slice To the End

By leaving out the end index, the range will go to the end:

**Example:**

Get the characters from position 2, and all the way to the end:

```python
b = "Hello, World!"
print(b[2:])
```
**Output:**
```
llo World
```

#### Negative Indexing

Use negative indexes to start the slice from the end of the string:

**Example:**

Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

```python
b = "Hello, World!"
print(b[-5:-2])
```
**Output:**
```
orl
```

#### Upper Case

**Example:**

The `upper()` method returns the string in upper case:

```python
a = "Hello, World!"
print(a.upper())
```
**Output:**
```
HELLO WORLD!
```

#### Lower Case

**Example:**

The `lower()` method returns the string in lower case:

```python
a = "Hello, World!"
print(a.lower())
```
**Output:**
```
hello world
```

#### Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

**Example:**

The `strip()` method removes any whitespace from the beginning or the end:

```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```
**Output:**
```
Hello, World!
```
#### Replace String

**Example:**

The `replace()` method replaces a string with another string:

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```
**Output:**
```
Jello, World
```

#### Split String

The `split()` method returns a list where the text between the specified separator becomes the list items.

**Example:**

The `split()` method splits the string into subs if it finds instances of the separator:

```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```
**Output:**
```
['Hello', ' World!']
```
#### String Concatenation

To concatenate, or combine, two strings you can use the + operator.

**Example:**

Merge variable `a` with variable `b` into variable `c`:

```python
a = "Hello"
b = "World"
c = a + b
print(c)
```
**Output:**
```
HelloWorld
```

**Example:**

To add a space between them, add a `" "`:

```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```
**Output:**
```
Hello World
```

#### String Format

As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

**Example:**
```python
age = 36
txt = "My name is John, I am " + age
print(txt)
```
**Output:**
```
TypeError: ...
```

But we can combine strings and numbers by using the `format()` method!

The `format()` method takes the passed arguments, formats them, and places them in the string where the placeholders `{}` are:

**Example:**

Use the `format()` method to insert numbers into strings:

```python
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
```
**Output:**
```
My name is john, and am 36
```

The `format()` method takes unlimited number of arguments, and are placed into the respective placeholders:

**Example:**
```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
```
**Output:**
```
I want 3 pieces of item 567 for 49.95 dollars.
```

You can use index numbers `{0}` to be sure the arguments are placed in the correct placeholders:

**Example:**
```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
```
**Output:**
```
I want to pay 49.95 dollars for 3 pieces of item 567
```

#### Escape Character

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash `\` followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

**Example:**

You will get an error if you use double quotes inside a string that is surrounded by double quotes:

```python
txt = "We are the so-called "Vikings" from the north."
```
**Output:**
```
SyntaxError: invalid syntax
```

To fix this problem, use the escape character `\"`:


**Example:**
The escape character allows you to use double quotes when you normally would not be allowed:

```python
txt = "We are the so-called \"Vikings\" from the north."
```
**Output:**
```
We are the so-called "Vikings" from the north.
```

#### Escape Characters

Other escape characters used in Python:

| Code |	Result |
| ---- | ------- |
| `\'` | Single Quote	| 
| `\\\\` |	Backslash	 |
| `\n` |	New Line	|
| `\r` |	Carriage Return	| 
| `\t` |	Tab	| 
| `\b` | Backspace	|
| `\f` |	Form Feed	|
| `\ooo` | Octal value	|
| `\xhh` | Hex value |

#### String Methods

Python has a set of built-in methods that you can use on strings.

***`Note`: All string methods return new values. They do not change the original string.***

Checkout: [ String Methods](https://www.w3schools.com/python/python_strings_methods.asp)
