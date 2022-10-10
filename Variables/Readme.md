### Variables

 Variables are containers for storing data values.

 Python has no command for declaring a variable.

 A variable is created the moment you first assign a value to it.

 ```py
 Variable_Name = "Variable_Value"
 # Double Quotes ""
 Variable_Name = 'Variable_Value'
 # Single Quotes ''
 ```

 Variables do not need to be declared with any particular type, and can even change type after they have been set.
 
 If you want to specify the data type of a variable, this can be done with casting.

 ```py
 x = str(3) # x will be string '3'
 y = int(3) # y will be integer 3
 z = float(3) # z will be floating-point number 3.0
 ```

#### Get the Type()

 You can get the data type of a variable with 
 the `type()` function.

 ```py
 # DataType
 string = "value" # str()
 integer = 2 # Don't use quotes for Numbers int()
 float = 2.1 # Don't use quotes for Numbers float()
 boolean = True # bool()
 list = ["A", "B"] # list()
 tuple = ("a", "b") # tuple()
 set = {"C", "D"} # set()
 dictionary = { "key":"value" , "key1":1 } #dict()
 
 print(type(string))
 ```
 
 **Output**:
 ```py 
 <class 'str'> 
 ```
 
#### Datatypes

Variables can store data of different types, and different types can do different things.

| DataTypes |  Types |
| --------- | ------ |
| Text Type |	`str` |
| Numeric Types |	`int`, `float`, `complex`|
| Sequence Types	|`list`, `tuple`, `range`|
| Mapping Type |	`dict`|
| Set Types	|`set`, `frozenset`|
| Boolean Type |`bool`|
| Binary Types|`bytes`, `bytearray`, `memoryview`|

#### Type Conversion

To convert between types, you simply use the type name as a function.

There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.

| Function | Description |
| -------- | ----------- |
| int(x [,base]) | Converts x to an integer. base specifies the base if x is a string. |
| long(x [,base] ) | Converts x to a long integer. base specifies the base if x is a string. |
| float(x) | Converts x to a floating-point number. |
| complex(real [,imag]) | Creates a complex number. |
| str(x) | Converts object x to a string representation. |
| repr(x) | Converts object x to an expression string. |
| eval(str) | Evaluates a string and returns an object. |
| tuple(s) | Converts s to a tuple. |
| list(s) | Converts s to a list. |
| set(s) | Converts s to a set. |
| dict(d) | Creates a dictionary. d must be a sequence of (key,value) tuples. |
| frozenset(s) |Converts s to a frozen set. |
| chr(x) | Converts an integer to a character. |
| unichr(x) || Converts an integer to a Unicode character. |
| ord(x) | Converts a single character to its integer value. |
| hex(x) | Converts an integer to a hexadecimal string. |
| oct(x) | Converts an integer to an octal string. |
