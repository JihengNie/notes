# Lecture 2 - Branching, Iteration

## Strings
* sequences of characters, spaces, digits
* we define strings by enclosing them in quotation marks or single quotes

### Operations on strings
* Concatenate strings
``` python
  name = "ana"
  greet = "Hello There" + name
```
* star operatior for strings
  * Python will interpert this as repeat the string 3 times

### Comparison operators on int, float, strings
Let i and j be variable names
Comparison below evaluate to a Boolean
* i > j
* i >= j
* i < j
* i <= j
* i == j equality test -> True if i is the same as j
* i != j inequality test -> True if i not the same as j

### Logic operators on Bools
Let a and b be variabel names with Boolean Values

* not a     -> True if a is False and False if a is True
* a and b   -> True if both are True
* a or b    -> True if either or both are True

## Indentation
* Indentation matters in python!

## Control Flow - while loop
``` python
while condition:
  expression
  expression
  ...
```
* *condtion* evaluates to a Boolean
* if the *condtion* is True, do all the steps inside the while code block
* check *condtion* again
* repeat until *condtion* is False

## Control Flow - for loop
``` python
for variable in range(some_num):
  expression
  expression
  ...
```
* each time through the loop, *variable* takes a value
* first time, *variable* starts at the smallest value
* next time, *variable* gets the prev value +1
* etc.

## range(start, stop, step)
* defalut values are
  * start = 0
  * step = 1
* loop until value is stop - 1
``` python
mysum = 0
for i in range(7, 10):
  mysum += i
print(mysum)


mysum = 0
for i in range(5, 11, 2):
  mysum += i
print(mysum)

```
## break statement
* immediately exits whatever loop it is in
* skips remaining expressions in code block
* exits only innermost loop!

``` python
while condition_1:
  while condition_2:
    expression_a
    break
    expression_b
  expression_c
```

### What will happen in this program?

``` python
mysum = 0
for i in range(5, 11, 2):
  mysum += i
  if mysum == 5:
    mysum += 1
print(mysum)
```

| Steps |      mysum    |   i   |   mysum after    |
|-------|:-------------:|:-----:|:----------------:|
| 0     |       0       |   5   |     5 + 1        |
| 1     |       6       |   7   |     6 + 7        |
| 2     |       13      |   9   |     13 + 9       |
| 3     |       22      |   11  |     done         |

Final mysum = 22

## for vs while loops
### for loops
* know number of iterations
* can end early via *break*
* uses a counter
* can rewrite a for loop using a while loop

### while loops
* unbounded number of iterations
* can end early via break
* can use a counter but must initialize before loop and increment it inside loop
* may NOT be able to rewrite a while loop using a for loop
