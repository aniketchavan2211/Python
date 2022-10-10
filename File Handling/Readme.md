### File handling

File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

#### Basics

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

`r` - Read - Default value. Opens a file for reading, error if the file does not exist

`a` - Append - Opens a file for appending, creates the file if it does not exist

`w` - Write - Opens a file for writing, creates the file if it does not exist

`x` - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

`t` - Text - Default value. Text mode

`b` - Binary - Binary mode (e.g. images)

**Syntax**:

To open a file for reading it is enough to specify the name of the file:

```py
f = open("demofile.txt")
```
The code above is the same as:

```py
f = open("demofile.txt", "rt")
```

Because `r` for read, and `t` for text are the default values, you do not need to specify them.

***`Note`: Make sure the file exists, or else you will get an error.***

#### Modes & Description

| Modes | Description |
| ----- | ----------- |
| `r` | Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode. |
| `rb` | Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode. |
| `r+` | Opens a file for both reading and writing. The file pointer placed at the beginning of the file. |
| `rb+` | Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file. |
| `w` | Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. |
| `wb` | Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. |
| `w+` | Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing. |
| `wb+` | Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing. |
| `a` | Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing. |
| `ab` | Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing. |
| `a+` | Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing. |
| `ab+` | Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing. |

####  Open a File

To open the file, use the built-in open() function.

The `open()` function returns a file object, which has a `read()`` method for reading the content of the file:

**Example:**
```py
f = open("file.txt", "r")
print(f.read())
```
**Output:**
```
Hello! Welcome to file.txt
This file is for testing purposes.
Good Luck!
```

If the file is located in a different location, you will have to specify the file path, like this:

**Example:**
Open a file on a different location:
```py
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
```
**Output:**
```
Welcome to this text file!
This file is located in a folder named "myfiles", on the D drive.
Good Luck!
```

#### Read Only Parts of the File

By default the `read()` method returns the whole text, but you can also specify how many characters you want to return:

**Example:**

Return the 5 first characters of the file:

```py
f = open("demofile.txt", "r")
print(f.read(5))
```
**Output:**
```
Hello
```


#### Read Lines

You can return one line by using the `readline()` method:

**Example:**

Read one line of the file:
```py
f = open("demofile.txt", "r")
print(f.readline())
```
**Output:**
```
Hello! Welcome to file.txt
```

By calling `readline()`` two times, you can read the two first lines:

**Example:**

Read two lines of the file:
```py
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
```
**Output:**
```
Hello! Welcome to file.txt
This file is for testing purposes.
```

By looping through the lines of the file, you can read the whole file, line by line:

**Example:**

Loop through the file line by line:
```py
f = open("demofile.txt", "r")
for x in f:
  print(x)
```
**Output:**
```
Hello! Welcome to file.txt
This file is for testing purposes.
Good Luck!
```

#### Close Files

It is a good practice to always close the file when you are done with it.

**Example:**

Close the file when you are finish with it:
```py
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```

***`Note`: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.***


#### Write to an Existing File

To write to an existing file, you must add a parameter to the `open()`` function:

`a` - Append - will append to the end of the file

`w` - Write - will overwrite any existing content

**Example:**

Open the file `demofile2.txt` and append content to the file:
```py
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
```
**Output**:
```
Hello! Welcome to demofile2.txt
This file is for testing purposes.
Good Luck!Now the file has more content!
```

**Example:**

Open the file `demofile3.txt` and overwrite the content:
```py
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
```
**Output**:
```
Woops! I have deleted the content!
```

***`Note`: the `w` method will overwrite the entire file.***

#### Create a New File

To create a new file in Python, use the `open()`` method, with one of the following parameters:

`x` - Create - will create a file, returns an error if the file exist

`a` - Append - will create a file if the specified file does not exist

`w` - Write - will create a file if the specified file does not exist

**Example:**
Create a file called `myfile.txt`:
```py
f = open("myfile.txt", "x")
```

Result: a new empty file is created!

**Example:**
Create a new file if it does not exist:
```py
f = open("myfile.txt", "w")
```

#### Delete a File

To delete a file, you must import the OS module, and run its `os.remove()`` function:

**Example:**

Remove the file `demofile.txt`:
```py
import os
os.remove("demofile.txt")
```
#### Check if File exist

To avoid getting an error, you might want to check if the file exists before you try to delete it:

**Example:**

Check if file exists, then delete it:
```py
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

#### Create a folder

The `os` module has serveral methods that helps you create, remove, and change directories.

```py
os.mkdir("newdir")
```

#### Delete Folder

To delete an entire folder, use the `os.rmdir()` method:

**Example:**

Remove the folder `myfolder`:
```py
import os
os.rmdir("myfolder")
```
***`Note`: You can only remove empty folders.***

#### Change a directory

**Syntax**:
```py
import os
# os.chdir("path")
os.chdir("/home")
```

Check more methods

***Reference:***

[File Methods](https://www.tutorialspoint.com/python/file_methods.htm)

[OS Module Methods](https://www.tutorialspoint.com/python/os_file_methods.htm)
