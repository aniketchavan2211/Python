### Loops 

A loop statement allows us to execute a statement or group of statements multiple times.

#### While loops

A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.

**Syntax**:
```python
while expression:
   statement(s)
```

**Example**:
```python
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
```

**Output**:
```
The count is: 0
The count is: 1
The count is: 2
The count is: 3
The count is: 4
The count is: 5
The count is: 6
The count is: 7
The count is: 8
```

##### Infinite loops

A loop becomes infinite loop if a condition never becomes FALSE.

**Example** :
```python
var = 1
while var == 1 :  # This constructs an infinite loop
   num = ("Enter a number  :")
   print ("You entered : ", num)
```
**Output**:
```
You entered : Entered a number  :
You entered : Entered a number  :
You entered : Entered a number  :
You entered : Entered a number  :
...
```

Loops never ends, And crashed the program

##### Using else Statement with While loops

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

The following example illustrates the combination of an else statement with a while statement that prints a number as long as it is less than 5, otherwise else statement gets executed.

```python
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
```
**Output** :
```
0 is less than 5
1 is less than 5
2 is less than 5
3 is less than 5
4 is less than 5
5 is not less than 5
```

##### On-line While

Similar to the if statement syntax, if your while clause consists only of a single statement, it may be placed on the same line as the while header.

**Example** :
```python
flag = 1
while (flag): print 'Given flag is really true!'
```


#### For loops

If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable iterating_var.

**Syntax**:
```python
for iterating_var in sequence:
   statements(s)
```

**Example**:
```
for letter in 'Python':     # First Example
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit

```
**Output**:
```
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n
Current fruit : banana
Current fruit : apple
Current fruit : mango
```

##### Iterating by Sequence Index

An alternative way of iterating through each item is by index offset into the sequence itself.

**Example**:
```Python
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]
```

**Output**:
```
Current fruit : banana
Current fruit : apple
Current fruit : mango
```

##### Using else Statement with For Loop

If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

The following example illustrates the combination of an else statement with a for statement that searches for prime numbers from 10 through 20.

```Python
for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
		break
```

**Output** :
```
10 equals 2 * 5
11 is a prime number
12 equals 2 * 6
13 is a prime number
14 equals 2 * 7
15 equals 3 * 5
16 equals 2 * 8
17 is a prime number
18 equals 2 * 9
19 is a prime number
```


#### Nested Loops

Python programming language allows to use one loop inside another loop. Following section shows few examples to illustrate the concept.


**Syntax for For loops** :
```python
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
```

**Syntax for while loops** :
```python
while expression:
   while expression:
      statement(s)
   statement(s)
```

**Example** :
```python
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1
```
**Output**:
```
2 is prime
3 is prime
5 is prime
7 is prime
11 is prime
13 is prime
17 is prime
19 is prime
23 is prime
29 is prime
31 is prime
37 is prime
41 is prime
43 is prime
47 is prime
53 is prime
59 is prime
61 is prime
67 is prime
71 is prime
73 is prime
79 is prime
83 is prime
89 is prime
97 is prime
```
