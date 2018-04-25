# Python - Class 1

## What is programming?

It's a series of instructions with a certain logic to be performed by a computer.

Programming is like cooking, you need to follow a recipe, using some ingredients, and finally preparing the saucer on the microwave or the stove.

So in programming is like:

- The kitchen is the computer.
- The recipe is the code.
- The microwave is the compiler which is in charge of creating our program.

## What is a programming language?

Is a set of symbols and letter which form part of a formal language that a computer can interpret.

There are 2 types of programming languages; High level & Low Level.

The more high level a programming language is more like a human language, so, the more low level, more like the computer language.

## What we do we need to program?

The first thing we need to start programming is to understand the basic principle:

- First, analyze the problem.
- Second, resolve it.
- Then we start coding.

## Bases of a programming language

### Basic Data Types

- Strings:
```
>>> name = "Francisco"
```
- Integers:
```
age = 30
```
- Floats:
```
height = 1.82
```
- Bools:
```
have_car = True
```

### Basic Operators

```
sum = 1 + 1
rest = 1 - 1
multiply = 1 * 2
divide = 2 / 1
```

- **=** for asignment.
- **==** for evaluation.

### Logical Operators

The logical `AND` operator `(&&)`` returns the boolean value true if both operands are true and returns false otherwise.

```
if 1 == 1 and 1 != 2:
    pass
```

The logical `OR` operator `(||)`` returns the boolean value true if either or both operands is true and returns false otherwise.

```
if 1 == 1 or 1 == 2:
    pass
```

### Flow Control Structure

#### If else conditionals Syntax

```
work_on_rigs = True

if work_on_rigs:
    name = "Francisco"
else:
    name = "Aaron"
```

#### Functions Syntax

- Function Definition.
``` 
def sum(number1, number2):
    return number1 + number2
```
- Function execution.
```
>>> sum()
```
- Assign the returned value from function to variable.
```
>>> my_sum = sum()
```

### Reserved word by pyhton

- if
- else
- def
- print

### Utility functions

- type()
- input()
