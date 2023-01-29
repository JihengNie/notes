# Lecture 3 - String Manipulation, Guess and Check, Approximations, Bisection

## Strings

* They are a sequence of case sensitive characters
* Can compare strings with ==, >, < etc.
* len() is a function used to retrieve the length of the string in the parentheses

```python
s = "abc"
len(s) -> evaluates to 3
```

* square brackets used to perform indexing into a string to get the value at a certain index/position

```python
s = "abc"
s[0] -> "a"
s[1] -> "b"
s[2] -> "c"
s[3] -> error, trying to index out of bounds
s[-1] -> "c"
s[-2] -> "b"
s[-3] -> "a"
```

* last element is always at index -1
* can slice strings using [start : stop : step]
* if gived two numbers, [start : stop], step = 1 by default
* you can also omit numbers and just leave colons

```python
s = "abcdefgh"
s[3:6] -> "def" #same as s[3:6:1]
s[3:6:2] -> "df"
s[::] -> "abcdefgh" #same as s[0: len(s): 1]
s[::-1] -> "hgfedbca" #same as s[-1: -1(len(s) + 1) : -1]
s[4:1:-2] -> "ec"
```

* strings are "immutable" - cannot be modified
```python
s = "hello"
s[0] = "y" # Will give an error
s = "y" + s[1:len(s)] # is allowed, s bound to a new object
```
## for loops recap
* for loops have a loop variable that iterates over a set of values
```python
for var in range(4): #var iterates over values 0,1,2,3
  <expressions>

for var in range(4,6): #var iterates over values 4,5
  <expressions>
```
* range is a way to iterate over numbers, but a for loop variable can iterate over any set of values, not just numbers!

## Strings and loops
* these two code snippets do the same thing
* bottom one is more "pythonic"
```python
s = "abcdefgh"
for index in range(len(s)):
  if s[index] == 'i' or s[index] == 'u':
    print("There is an i or u")

```

```python
for char in s:
  if char == 'i' or char == 'u':
    print("There is an i or u")

```

## Code example: Robot cheerleaders
```python
an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiam level (1-10): "))

for char in word:
  if char in an_letters:
    print("Give me an " + char + "! " + char)
  else:
    print( "Give me a " + char + "! " + char)
print("What does that spell?")
for i in range times:
  print(word, "!!!")
```
# Finding cube root of a number
## Guess and check
* The process below is also called exhaustive enumeration
* Given a problem...
* The process works if you are able:
  * to guess a value for a solution
  * to check if the solution is correct
* Keep guessing until find solution or guessed all values

Initial try
```python
cube = 8
for guess in range(cube+1):
  if guess ** 3 == cube:
    print("Cube root of", cube, "is", guess)
```

Adding in negative cubes and if a number is not a perfect cube

```python
cube = 8
for guess in range(abs(cube)+1):
  if guess ** 3 >= abs(cube):
    break

if guess ** 3 != abs(cube):
  print(cube, 'is not a perfect cube')

else:
  if cube < 0:
    guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))
```

## Approximate solution
* good enough solution
* start with a guess and increment by some small value
* keep guessing if | guess <sup>3</sup> - cube| >= epsilon for some small epsilon
* decreasing incrememnt size -> slower program
* increasing epsilon -> less accurate answer

```python
cube = 27
epsilon = .01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
  guess += increment
  num_guesses += 1
print("num_guesses =", num_guesses)

if abs(guess ** 3 - cube) >= epsilon:
  print("Failed on cube root of ", cube)
else:
  print(guess, "is close to the cube root of", cube)
```
## Bisection search
* half interval each iteration
* new guess is halfway in between
```python
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess ** 3 - cube) >= epsilon:
  if guess ** 3 < cube:
    low = guess
  else:
    high = guess
  guess = (high + low) / 2.0
  num_guesses += 1
print("num_guesses =", num_guesses)
print(guess, "is close to the cube root of", cube)
```

## Bisection search convergence
* search space
  * first guess: N/2
  * second guess: N/4
  * kth guess: N/2<sup>k</sup>
* guess converges on the order of log<sub>2</sub>N steps
* bisection search works when value of function varies monotonically with input
* code as shown only works for positive cubes > 1
* Challenges:
  * Modify to work with negative cubes!
  * Modify to work with x < 1

## For x < 1
* if x < 1, search space is 0 to x, but cube root is greater than x and less than 1
* modify the code to choose the search space depending on value of x
