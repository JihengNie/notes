# Tuples, lists, aliasing, mutability, and cloning

## Tuples
* They are an ordered sequence of elements, can mix element types
* Cannot change element values, they are immutable
* Represented with parentheses

```python
te = () # Empty tuple
t = (2, "mit", 3)
t[0] # Evaluates to 2
t[1:2] # slice tuple, evaluates to ("mit",)
t[1:3] # slice tuple, evaluates to ("mit",3)
len(t) # evaluates to 3
```

* Conventiently used to swap variable values
```python
temp = x
x = y
y = temp

(x, y) = (y, x)
```
* used to return more than one value from a function
```python
def qutient_and_remainder(x,y):
  q = x // y # integer division
  r = x % y
  return (q, r)
```

## manipulating tuples
* can iterate over tuples
```python
def get_data(aTuple):
  # aTuple ((ints,strings), (), ())
  nums = ()
  words = ()
  for t in tuples:
    nums = nums + (t[0],)
    if t[1] not in words:
      words = words + (t[1],)
  min_n = min(nums)
  max_n = max(nums)
  unique_words = len(words)
  return (min_n, max_n, unique_words)
```

## Lists
* Ordered sequence of information, accessible by index
* a list is denoted by square brackets, []
* a list contains elements
  * usually homogeneous (ie, all intergers)
  * can contain mixed types (not common)
* list elements can be changed so a list is mutable

## Indces and ordering
```python
a_list = [] # empty list
L = [2, "a", 4, [1,2]]
len(L) # evaluates to 4
L[0] # evaluates to 2
L[2] + 1 # evaluates to 5
l[3] # evaluates to [1, 2], another list!
i = 2
L[i - 1] # evaluates to "a" since L[1] = "a"
```
* Lists are mutable
* Assigning to an element at an index changes the value
```python
L = [2, 1, 3]
L[1] = 5
L # is now [2, 5, 3]
```
* Note: This is the same object!

## Iterating over a list
* Compute the sum of elements of a list
* comman patter, iterate over list elements

```python
total = 0
for i in range(len(L)):
  total += L[i]
print total
```
* List strings, lists can be element wise iterated

```python
total = 0
for i in L:
  total += i
print total
```
* Notice that:
  * list elements are indexed 0 to len(L) - 1
  * range(n) goes from 0 to n - 1

## Operatiions on lists - Add
* add elements to end of a list with L.append(element)
* mutates the list!
* What is the dot?
  * lists are Python objects, everything in Python is an object
  * objects have data
  * objects have methods and functions
  * access this information by object_name.do_something()
* to combine lists together use concatenation, + operator, to give you a new list
* mutate list with L.extend(some_list)

```python
L1 = [2, 1, 3]
L2 = [4, 5, 6]
L3 = L1 + L2 # . L1 and L2, unchanged

L1. extend([0,6]) # mutated L1 to [2, 1, 3, 0, 6]
```

## Operations on lists - Remove
* delement element at a specific index with del(L[index])
* remove element at end of the list with L.pop(), returns the removed element
* remove a specific element with L.remove(element)
  * Looks for the element and removes it
  * if element occurs multiple times, remove first occurrence
  * if element not in list, gives an error

```python
# All of the following operations occurrs in order
L3 = [2, 1, 3, 6, 3, 7, 0]
L.remove(2) # mutates L = [1, 3, 6, 3, 7, 0]
L.remove(3) # mutates L = [1, 6, 3, 7, 0]
del(L[1]) # mutates L = [1, 3, 7, 0]
L.pop() # returns 0 and mutates L = [1, 3, 7]
```
## Convert lists to strings and back
* Convert string to list with list(s), returns a list with every character from s an element in L
* can use s.split(), to split a string on a character parameter, splits on spaces if called without a parameter
* use ''.join(L) to turn a list of characters into a string, can give a character in quoters to add char between every element

```python
s = "I<3 cs" # s is a string
list(s) # returns  ['I','<','3',' ','c','s']
s.split("<") # returns  ['I', '3 cs']

L = ["a", "b", "c"] # L is a list
''.join(L) # returns "abc"
'_'.join(L) # returns "a_b_c"
```
* sort() and sorted()
* reverse()
* and many more!
  https://docs.python.org/3/tutorial/datastructures.html
```python
L = [9, 6, 0, 3]
sorted(L) # returns sorted list, does not mutate L
L.sort() # mutates L = [0,3,6,9]
L.reverse() # mutates L = [9,6,3,0]
```

## lists in memory
* lists are mutable
* behave differently than immutable types
* is an object in memory
* variable names points to object
* any variable pointing to that object is affected
* key phrase to keep in mind when working with lists is side effects

## An analogy
* attributes of a person - Justin Bieber
  * singer, rich
* he is known by many names
* all nicknames point to the same person
  * add new attributes to one nickname
    Justin Bieber - singer - rich - troublemaker
  * ... all his nicknames refer to old attributes AND all new ones
    The Bieb - singer - rich - troublemaker
    JBeebs - singer - rich - troublemaker

## Aliases
* hot is an alias for warm - changing one changes the other!
* append() has a side effect

```python
a = 1
b = a
print(a)
print(b)

warm = ["red", "yellow", "orange"]
hot = warm
hot.append("pink")
print(hot)
print(warm)
```

## Cloning a list
* create a new list and copy every element using chill = cool[:]

```python
cool = ["blue", "green", "grey"]
chill = cool[:]
chill.append("black")
print(chill)
print(cool)
```

## sorting lists
* calling sort() mutates the list, returns nothing
* calling sorted() DOES NOT mutate the list, must assign result to a new variable

```python
warm = ["red", "yellow", "orange"]
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)

cool = ["blue", "green", "grey"]
sortedcool = sorted(cool)
print(cool)
print(sortedcool)
```
## Lists of lists of lists...
* can have nested lists
* side effects still possible after mutation

```python
warm = ["yellow", "orange"]
hot = ["red"]
brightcolors = [warm]
brightcolors.append(hot)
print(brightcolors)

hot.append("pink")
print(hot)
print(brightcolors)
```

## mutation and iteration
* avoid mutating a list as you are iterating over it

```python
# Bad
def remove_dups(L1, L2):
  for e in L1:
    if e in L2:
      L1.remove(e)

# Good
def remove_dups(L1, L2):
  L1_copy = L1[:]
  for e in L1_copy:
    if e in L2:
      L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
```
* L1 is [2, 3, 4], not [3, 4] why?
  * Python uses an internal counter to keep track of index it is in the loop
  * mutating changes the list length but Python doesn't update the counter
  * loop never sees element 2
