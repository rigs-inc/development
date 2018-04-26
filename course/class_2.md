# Python - Class 2

## Data Types

- List
- Dictionary

## Flow Control Structure

- Loops

## What is a List?

A list is a data structure that allows storing different data types; integers, floats, strings, even functions. They can contain as many variables as we needed.

How to create and add data to a list:

- Define a new list with pre-defined data:
```
>>> my_super = ["fruit", "vegetables", "cleaning products", ...]
```
- Define a empty list and add data after:
```
>>> my_super = []
>>> my_super.append("fruit")
>>> my_super.append("vegetables")
>>> my_super.append("cleaning products")
```

How to work with a list data:

- Accessing by its element index
```
>>> my_super[0] ---> "fruit"
>>> my_super[1] ---> "vegetables"
>>> my_super[2] ---> "cleaning products"
```
- Iterating over a very simple manner
```
for product in my_super:
  print product
```

## What is a Dictionary?

Like the list, dictionaries are data structures that allow storing different data types, with the difference that to each element a key can be assigned.

How to create and assign data:
```
>>> phonebook = {}
>>> phonebook["John"] = 938477566
>>> phonebook["Jack"] = 938377264
>>> phonebook["Jill"] = 947662781
>>> print phonebook["Jill"]
947662781
```

## What is a Loop?

A loop in programming is a flow control structure that allows to execute a line or block of code many times as needed

There are 2 types of Loops

- Determined
  - Is repeated a determined number of times
```
# This will print from 0 to 100

for number in range(0, 100):
  print number
```
- Undetermined
  - They repeat a line or a block of code for an unknown number of times until the program is executed

```
# a list is created & data is added while the program is executed
>>> my_super = []
>>> my_super.append("fruit")
>>> my_super.append("vegetables")
>>> my_super.append("cleaning products")
...
>>> my_super.append(...)

for product in my_super:
  print product
```
