# Recursion, Dictionaries
## Recursion - What is it?
* Recursion is the process of repeating items in a self-similar way
* Algorithmically: A way to design solutions to problems by divide-and-conquer or decrease-and-conquer
  * reduce a problem to simpler versions of the same problem
* Semantically: A programming technique where a function calls itself
  * In programming, goal is to NOT have infinite recursion
    * Must have 1 or more base cases that are easy to solve
    * Must solve the same problem on some other input with the goal of simplifying the larger problem input

## Iterative algorithms so far
* Looping constucts(while and for loops) lead to iterative alogrithms
* Can capture computation in a set of state variables that update on each iteration through loop

## Multiplication - Iterative solution
* "multiply" a * b is equalent ot "add a to itself b times"
* capture state by
  * An iteration number(i) starts at b
  * A current value of computation(result)

```python
def mult_iter(a,b):
  result = 0
  while b > 0:
    result += a
    b -= 1
  return result
```
## Multiplaction - recursive solution
* Recursive step
  * Think how to reduce problem to a simpler/smaller version of the same problem
* Base case
  * Keep reducing problem until reach a simple case that can be solved directly

## Factorial
n! = n * (n-1) * (n-2) * ... * 1
* For what n do we know the factorial?
  n = 1 -> if n == 1, we can return 1
* how to reduce problem? Rewrite in terms of something simpler to reach base case
  n*(n-1)! -> else, return n * factorial(n-1)
```python
def fac(n):
  if n ==1:
    return 1
  else:
    return n * fac(n-1)
```

## Some observations
* Each recursive call to a function creates its own score/ enviroment
* Bindings of variables in a scope are not changed by recursive call
* Flow of control passes back to previous scope once function call returns value

## Iteration vs Recursion
### Iteration
```python
def factorial_iter(n):
  prod = 1
  for i in range(1, n+1):
    prod *= 1
  return prod
```

### Recursion
```python
def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n - 1)
```
* Recursion may be simpler, more intuitive
* Recursion may be efficient from programmer POV
* Recursion may not be efficient from computer POV

## Mathematical Induction
* To prove a statement indexed on integers is true for all values of n:
  * Prove it is true when n is smallest value
  * Then prove that it is true for an arbitary value of n, one can show that it must be true for n + 1
## Relvance to code?
* Same logic applies
```python
def mult(a, b):
  if b == 1:
    return a
  else:
    return a + mult(a, b-1)
```
* Base case, we can show mult must return correct answer
* For recursive case, we can assume that mult correctly returns an answer for problems of size smaller than b, then by the addition step, it must also return a correct answer for the problem of size b
* Thus, by induction, code correctly returns answer

## Tower of Hanoi
* The story:
  * 3 tall spikes
  * Stack of 64 different sized discs - start on one spike
  * Need to move stack to a second spike (at which point universe ends)
  * Can only move one disc at a time, and a larger disc can never cover up a small disc
* Having seen a set of examples of different sized stacks, how would you write a program to print out the right set of moves?
* Thinking recursively!
  * Solve a smaller problem
  * Solve a basic problem
  * Solve a smaller problem

```python
def printMove(fr, to):
  print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
  if n == 1:
    printMove(fr, to)
  else:
    Towers(n-1, fr, spare, to)
    Towers(1, fr, to , spare)
    Towers(n-1, spare, to, fr)
```
## Recursion with multiple base cases
* Fibonacci numbers
  * Leonardo	of	Pisa	(aka	Fibonacci)	modeled	the	following	challenge
    * Newborn	pair	of	rabbits	(one	female,	one	male)	are	put	in	a	pen
    * Rabbits	mate	at	age	of	one	month
    * Rabbits	have	a	one	month	gestaSon	period
    * Assume	rabbits	never	die,	that	female	always	produces	one	new	 pair	(one	male one	female)	every	month	from	its	second	month	on.
    * How many female rabbits are there at the end of one year?

## Fibonacci
* After one month (call it 0) - 1 female
* After second month - still 1 female (now pregnant)
* After third month - two femals, one pregnant, one not
* In general, females(n) = females(n-1) + females(n - 2)
  * Every female alive at month n - 2 will produce one female in month n
  * These can be added those alive in month n-1 to get total alive in month n

* Base cases:
  * Females(0) = 1
  * Females(1) = 1
* Recursive case
  * Females(n) = Females(n-1) + Females(n-2)
```python
def fib(x):
  """
    Assume x is an int >= 0
    Returns Fibonacci of x
  """
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x - 1) + fib(x - 2)
```

## Recursion on Non-Numerics
* How to check if a string of characters is a palindrome ie reads the same forwards and backwards
* First, convert the string to just characters, by stripping out punctuation, and converting upper case to lower case
* Then
  * Base case: a string of length 0 or 1 is a palindrome
  * Recursive case:
    * If the frist character mathces the last character, then it is a palindrome if middle section is a palindrome

```python
def isPalindrome(s):
  def toChars(s):
    s = s.lower()
    ans = ''
    for c in s:
      if c in 'abcdefghijklmnopqrstuvwxyz':
        ans = ans + c
  def isPal(s):
    if len(s) <= 1:
      return True
    else:
      return s[0] == s[-1] and isPal(s[1:-1])
  return isPal(toChars(s))
```

## Divide and Conquer
* an example of divide and conquer algorithm
* Solve a hard problem by breaking it into a set of sub-problems such that:
  * sub-problems are easier to solve than the original
  * Solutions of the sub-problems can be combined to solve the original

## Dictionaries
* A python dictionary stores pairs of data
  * Key
  * Value
## Dictionary lookup
* Similar to indexing into a list
* Looks up the key
* Returns the value associated with the key
* if key isn't found, get an error

## Dictionary operations
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
* add an entry
  * grades['Sylvan'] = 'A'
* test if a key in dictionary
  * 'John' in grades -> returns True
  * 'Daniel' in grades -> returns False
* delete entry
  * del(grades["Ana"])
* get an iterable that acts like a tuple of all keys
  *  grades.keys() -> returns ['Denise','Katy','John','Ana']
* get an iterable that acts like a tuple of all values
  * grades.values() -> returns ['A', 'A', 'A+', 'B']

## Dictionary keys and values
* values
  * any type (immutable and mutable)
  * can be duplicates
  * dictionary values can be lists, even other dictionaries
* keys
  * Must be unique
  * immutable types(int, float, string, typle, bool)
    * Actually need an object that is hashable, but think of as immutable as all immutable types are hashable
    * careful with float type as a key
  * no otder to keys or values

## List vs dictionaries
### List
* Ordered sequence of elements
* Look up elements by an integer index
* Indices have an order index is an integer
### Dictionary
* mathces keys to values
* look up one item by another item
* No order is guaranteed
* key can be any immutable type

### Example 3 functions to analyze song lyrics
1. Create a frequence dictionary mapping str:int
2. Find word that occurs the most and how many times
  * use a list, in case there is more than one word
  * return a tuple (list, int) for words_list, highest_freq
3 find the words that occurs at least x times
  *	let	user	choose	“at	least	X	Smes”,	so	allow	as	parameter
  * return	a	list	of	tuples,	each	tuple	is	a	(list, int) containing	the	list	of	words	ordered	by	their	frequency
  * IDEA:	From	song	dicSonary,	find	most	frequent	word.	Delete	most	common	word.	Repeat.	It	works	because	you	are mutating the	song	dictionary

## Creating a dictionary
```python
def lyrics_to_frequencies(lyrices):
  myDict = {}
  for word in lyrics:
    if word in myDict:
      myDict[word] += 1
      else:
        myDict[word] = 1
  return myDict
```

## Using the dictionary
```python
def most_common_words(freqs):
  values = freqs.values()
  best = max(values)
  words = []
  for k in freqs:
    if freqs[k] == best:
      words.append(k)
  return (words, best)
```
## Leveraging dictionary properties
```python
def words_often(freqs, minTimes):
  result = []
  done = False
  while not done:
    temp = most_common_words(freqs):
    if temp[1] >= minTimes:
      result.append(temp):
      for w in temp[0]:
        del(freqs[w])
    else:
      done = True
  return result

print(words_often(beatles, 5))
```
## Fibonacci with a dictionary
```python
def fib_efficient(n, d):
  if n in d:
    return d[n]
  else:
    ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
    d[n] = ans
    return ans
```
* do a loopup first in case already calculated the value
* modify dictionary as progress through function calls

## Efficiency gains
* Calling	fib(34)	results	in	11,405,773	recursive	calls	to
the	procedure
* Calling	fib_efficient(34)	results	in	65	recursive	calls	to
the	procedure
* Using	dicSonaries	to	capture	intermediate	results	can
be	very	efficient
* But	note	that	this	only	works	for	procedures	without
side	effects	(i.e.,	the	procedure	will	always	produce	the
same	result	for	a	specific	argument	independent	of	any
other	computaSons	between	calls)
