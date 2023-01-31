# Decomposition, Abstraction, Functions

## How do we write code?
* So far...
  * covered language mechanisms
  * know how to write different files for each computation
  * each file is some piece of code
  * each code is a sequence of instructions
* problems with this approach
  * easy for small-scale problems
  * messy for larger problems
  * hard to keep track of details
  * how do you know the right info is supplied to the right part of the code?

## Good programming
* More code not necessarily a good thing
* measure good programmers by the amount of functionality
* introduce functions
* mechanism to achieve decomposition and abstraction

## Example - prokector
* A projector is a black box
* don't know how it works
* know the interface: input/output
* connect any electronic to it that can communicate with that input
* black box somehow converts image from input source to a wall, magnifying it
* Abstraction idea: Do not need to know how projector works to use it

* projecting large image for olympics decomposed inot seprate tasks for seprate projectors
* each projector takes input an dproduces separate outputs
* all projectors work together to produce larger image
* Decomposition idea: Different devices work together to achieve an end goal

## Create structure with decomposition
* in projector example, deprate devices
* in programming, divide code into modules
  * are self-contained
  * used to break up code
  * intended to be reusable
  * keep code orginized
  * keep code coherent
* achieve decompositon with functions, later with classes

## supress details with abstraction
* in projector example, instructions for how to use it are sufficient, no need to know how to build one
* in programming, think of a piece of code as a black box
  * cannot see details
  * do not need/want to see details
  * hide tedious coding details
* achieve abstraction with function specifications or docstrings

## Functions
* Write resueable pieces/chuncks of code, called functions
* functions are not run in a program until they are called or invoked in a program
* function characteristics:
  * has a name
  * has parameters (0 or more)
  * has a docstring (optional but recommended)
  * has a body
  * returns something

```python
def is_even(i):
  """
  input: i, a positive int
  returns true if i is even, otherwise false
  """
  print("inside is_even")
  return i % 2 ==0

is_even(3)
```

## variable scope
* Global scope is the main programming scope
* formal parameter gets bound to the value of actual parameter when function is called
* new scope/frame/environment created when enter a function
* scope is mapping of names to objects

## Warning if no return statement
* Python returns the value None if no return given
* represents the absence of a value

## Return vs Print
### Return
* return only has meaning inside a function
* only one return exectued inside a function
* code inside function but after return statement not executed
* has a value associated with it, given to function caller
### print
* print can be used outside functions
* can execute many print statements inside a function
* code inside function can be executed after a print statement
* has a value associated with it, outputted to the console

## Functions as arguments
* Arguments can take on any type, even functions

## Scope example
* Inside a function, can access a variable defined outside
* Inside a function, cannot modify a variable defined
* outside -- can use global variables, but frowned upoon

## Decomposition and abstraction
* Powerful together
* code can be used many times but only has to be debudded once!
