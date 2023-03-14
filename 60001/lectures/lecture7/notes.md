# Testing, Debugging, Exceptions, and Assertions

## We aim for high quality -- Soup Analogy
You are making soup, but bugs keep falling in from the ceiling. What do you do?
* Check soup for bugs
  * Testing
* Keep lid closed
  * Defensive programming
* Clean kitchen
  * Eliminate source of bugs

## Defensive programming
* Write specificiations for functions
* Modularize programs
* Check conditions on inputs/outputs(assertions)

## Testing/Validation
* Compare input/output pairs to specification
* "How can I break my program?"

## Debugging
* Study events leading up to an error
* "Why is it not working?"
* "How can I fix my program?"

## Set yourself up for easy testing and debugging
* From the start, design code to ease this part
* Break program up into modules that can be tested and debugged individually
* Document constrants on modules
  * What do you expect the input to be?
  * What do you expect the output to be?
* Document assumptions behind the code design

## When are you ready to test?
* Ensure code runs
  * Remove syntax errors
  * Remove static semantic errors
  * Python interperter with usuall find these for you
* Have a set of expected results
  * An input set
  * For each input, the expected output

## Classes of tests
* Unit testing
  * validate each piece of program
  * testing each function seprately
* Regression testing
  * add test for bugs as you find them
  * catch reintroducted errors that you were previously fixed
* Intergration testing
  * Does overall program work?
  * tend to rush to do this

## Testing approaches
* Intuition about natural boundaries to the problem
  * Can you come up with some natural partitions?
* If no natural partitions, might do random testing
  * Probability that code is correct increases with more tests
* Black box testing
  * Explore paths through specification
* Glass box testing
  * Explore paths through code

## Black box testing
* Designed without looking at the code
* Can be done by someone other than the implementer to avoid some implementer biases
* Testing can be reused if implementation changes
* Paths through specification
  * Build test cases in different natural space partitions
  * Also consider boundary conditions (empty lists, sigleton list, large numbers, small numbers)

## Glass box testing
* Use code directly to guide design of test cases
* Called path-compleate if every potential path through code is tested at least once
* What are some drawbacks of this testing?
  * Can go through loops arbitarily many times
  * Missing paths
* Guildlines
  * Branches
    * Exercise all parts of a conditional
  * for loops
    * Loop not entered
    * body of loop executed exactly once
    * body of loop executed more than once
  * While loops
    * same as for loops
    * cases that catch all ways to exit the loop

## Debugging
* Steep learning curve
* Goal is to have a bug free program
* tools
  * Built to IDLE and Anaconda
  * Python Tutor
  * Print statement
  * Use your brain, be systematic in your hunt

## Print statements
* Good way to test hypothesis
* When to print
  * Enter function
  * Parameters
  * function results
* Use bisection method
  * put print halfway in code
  * decide where bug may be depending on values

## Debugging steps
* study program code
  * Don't ask what is wrong
  * ask how did I get the unexpected result
  * is it part of a family?
* Scientific method
  * Study available data
  * Form hypothesis
  * repeatable experiments
  * Pick simplest input to test with

## Error messages
* Trying to access beyond the limits of a list -- Index Error
* Trying to convert an inappropirate type -- TypeError
* Mixing data types without appropriate coercion -- TypeError
* Referencing a non-existent variable -- NameError
* Forgeting to close parenthesis, quotation, etc -- SyntaxError

## Logic Errors
* Think before writing new code
* Draw pictures, take a break
* Explain the code to someone else or rubber ducky

## Exception and Assertions
* What happens when procdure execcution hits an unexpected condition?
* Get an exception ... to what was expected
  * SyntaxError -- Python can't parse program
  * NameError -- Local or global name not found
  * AttributeError -- Attribute reference fails
  * TypeError -- Operand doesn't have correct type
  * ValueError -- Operand type okay, but value illegal
  * IOError -- IO System reports malfunction (eg file not found)

## Dealing with Exceptions
* Python code can provide handlers for exceptions

```python
try:
  a = int(input("Tell me one number:"))
  b = int(input("Tell me another number:"))
  print(a/b)
except:
  print("Bug in user input.")
```
* Exceptions raised by any statement in body of try are handled by the except statement and execution continues with the body of the except statement

## Handle specific exceptions
* Have seprate except clauses to deal with a particular type of exception

```python
try:
  a = int(input("Tell me one number: "))
  b = int(input("Tell me another number: "))
  print("a/b = ", a/b)
  print("a+b = ", a+b)
except ValueError:
  print("Could not convert to a number.")
except ZeroDivisionError:
  print("Can't divide by zero")
except:
  print("Something went very wrong.")
```

## Other exceptions
* else:
  * body of this is executed when execution of associated try body compleates with no exceptions
finally:
  * body of this is always executed after try, else, and except clauses, even if they raised another error or excutate a break, continue, or return
  * useful for clean-up code that should be run no matter what else happened

## What to do with exceptions?
* What to do when encounter an error?
* fail silently:
  * Substitute default values or just continue
  * bad idea! user gets no warning
* return an "error" value
  * What value to choose?
  * Complicates code having to check for a specific value
* stop execution, signal error condition
  * In python: raise an exception
```python
raise Exception("Descriptive String")
```

## Exceptions as control flow
* Don't return specific values when an error occurred and then cehck whether 'Error value' was returned
* Instead, raise an exception when unable to produce a result consistent with function's specification

## Example: Raising an Exception
```python
def get_ratios(L1, L2):
  """ Assumes: L1 and L2 are lists of equal length of numbers
  Returns: a list containing L1[i]/L2[i] """
  ratios = []
  for index in range(len(L1)):
    try:
      ratios.append(L1[index]/L2[index])
    except ZeroDivisionError:
      ratios.append(float('nan')) #nan = not a number
    except:
      raise ValueError('get_ratios called with bad arg')
  return ratios
```

## Example of exceptions
* Assume we are given a class list for a subject: Each entry is a list of two parts
  * A list of first and last name for a student
  * A list of grades on assignments
  ```python
  test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
                [['bruce', 'wayne'], [100.0, 80.0, 74.0]]]
  ```
  * Create a new class list, with name, grades, and an average
  ```python
    [[['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333],
    [['bruce', 'wayne'], [100.0, 80.0, 74.0], 84.666667]]]
  ```

## Example Code
```python
def get_stats(class_list):
  new_stats = []
  for elt in class_list:
  new_stats.append([elt[0], elt[1], avg(elt[1])])
  return new_stats

def avg(grades):
  return sum(grades)/len(grades)
```

## Error if no grade for a student
* If one or more students dont have any grades, get an error
  ```python
  test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
                [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
                [['captain', 'america'], [8.0,10.0,96.0]],
                [['deadpool'], []]]
  ```
* get ZeroDivisionError: float division by zero because the grade list is empty

## Assertions
* want to be sure that assumptions on state of computation are as expected
* Use an assert statement to raise an AssertionError exception if assumptions not met
* An example of good defensive programming

## Example

```python
def avg(grades):
  assert len(grades) != 0, 'no grades data'
  return sum(grades)/len(grades)
```
* Raises an AssertionError if it is given an empty list for grades
* Otherwise runs okay

## Assertions as defensive programming
* Assertions don't allow a programmer to control response to unexpected condition
* Ensure that execution halts whenever an expected condition is not met
* Typically used to check inputs to functions, but can be used anywhere
* can be used to check outputs of a function to avoid propagating bad values
* can make it easier to locate a source of a bug

## Where to use assertions?
* Goal is to spot bugs as soon as introduced and make clear where they happened
* Use as a supplement to testing
* raise exceptions if users supplies bad data input
* use assertions to
  * check types of arguments or values
  * check that invariants on data structires are met
  * check constraints on return values
  * check for violations of constraints on procedure (eg no duplicates in a list)
