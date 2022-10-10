### Try Except Else Finally

The `try` block lets you test a block of code for errors.

The `except` block lets you handle the error.

The `else` block lets you execute code when there is no error.

The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

#### Exception Handling

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the `try` statement:

**Example:**
The `try` block will generate an exception, because x is not defined:
```python
try:
  print(x)
except:
  print("An exception occurred")
```
**Output:**
```
An exception occurred
```

Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error:

**Example:**
This statement will raise an error, because `x` is not defined:
```python
print(x)
```
**Output:**
```
NameError: name 'x' is not defined
```

#### Many Exceptions

You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

**Example:**
Print one message if the try block raises a `NameError` and another for other errors:
```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```
**Output:**
```
Variable x is not defined
```

#### Else

You can use the `else` keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the `try` block does not generate any error:
```python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```
**Output:**
```
Hello
Nothing went wrong
```

#### Finally

The `finally` block, if specified, will be executed regardless if the try block raises an error or not.

**Example:**
```python
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```
**Output:**
```
Something went wrong
The 'try except' is finished
```

This can be useful to close objects and clean up resources:

**Example:**
Try to open and write to a file that is not writable:
```python
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
```
**Output:**
```
Something went wrong when writing to the file
```

The program can continue, without leaving the file object open.

#### Raise an exception

As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the `raise` keyword.

**Example:**
Raise an error and stop the program if x is lower than 0:
```python
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
```
**Output:**
```
Exception: Sorry, no numbers below zero
```

The `raise` keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

**Example:**
Raise a TypeError if x is not an integer:
```python
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
```
**Output:**
```
TypeError: Only integers are allowed
```

#### Exceptions & Description 

| Exception Name | Description |
| -------------- | ----------- |
| Exception | Base class for all exceptions |
| StopIteration | Raised when the next() method of an iterator does not point to any object. |
| SystemExit | Raised by the sys.exit() function. |
| StandardError | Base class for all built-in exceptions except StopIteration and SystemExit. |
| ArithmeticError | Base class for all errors that occur for numeric calculation. |
| OverflowError | Raised when a calculation exceeds maximum limit for a numeric type. |
| FloatingPointError | Raised when a floating point calculation fails. |
| ZeroDivisionError | Raised when division or modulo by zero takes place for all numeric types. |
| AssertionError | Raised in case of failure of the Assert statement. |
| AttributeError | Raised in case of failure of attribute reference or assignment. |
| EOFError | Raised when there is no input from either the raw_input() or input() function and the end of file is reached. |
| ImportError | Raised when an import statement fails. |
| KeyboardInterrupt | Raised when the user interrupts program execution, usually by pressing Ctrl+c. |
| LookupError | Base class for all lookup errors. |
| IndexError | Raised when an index is not found in a sequence. |
| KeyError | Raised when the specified key is not found in the dictionary. |
| NameError | Raised when an identifier is not found in the local or global namespace. |
| UnboundLocalError | Raised when trying to access a local variable in a function or method but no value has been assigned to it. |
| EnvironmentError | Base class for all exceptions that occur outside the Python environment. |
| IOError | Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist. |
| IOError | Raised for operating system-related errors.|
| SyntaxError | Raised when there is an error in Python syntax. |
| IndentationError | Raised when indentation is not specified properly. |
| SystemError | Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit. |
| SystemExit | Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit. |
| TypeError | Raised when an operation or function is attempted that is invalid for the specified data type. |
| ValueError | Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified. |
| RuntimeError | Raised when a generated error does not fall into any category. |
| NotImplementedError | Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented. |
