# Lecture 1 - What is Computation?

## What does a computer do?
* Fundamentally:
  * They performs calculations. A billion calculations per seconds!
  * They remember results. 100s of gigabytes of storge
* What kind of calculations?
  * Built-in to the langulage. These are low types of calculations such as addition, subtraction, multiplication, and so on
  * Ones that we define as programmers using the low level calculations
* Computers only know what we tell them

## Type of knowledge
* Declaritive knowledge - These are statement of facts.
* Imperative knowledge - These are a recipe or "how-to"

  ### Numerical example of types of knowledge
  Declaritive knowledge: Square root of a number x is y such that y*y = x
  Imperative knowledge: Recipe for deducing square root of a number x
  1. Start with a guess g
  2. If g*g is close enough to x, stop and say g is the answer
  3. Otherwise, make a new guess by averaging g and x/g
  4. Using the new guess, repeat provess until close enough

## What is a recipe?
1. Sequence of simple steps
2. Flow of control process that specifies when each step is exected
3. A means of determining when to stop

## Computers are machines
* fixed program computer - They are great for one task
  * Calculators
* Stored program computer - These are machines that stores and excutes instructions. They are modern day computers

## Basic machine architecture

* Memory - This is where data and sequences of instructions is stored
* Arithemetic logic unit - This is where the primitive operations are preformed
* Control unit - This is a program counter. Depending on the instruction, we are able to increase this counter (i.e. move onto the next step) or reset it back to 0 (or restarting the steps)
* Input - Taking in a set of commands
* Output - Returing a result after the sequences of instructions are compleated

## Stored program computer

* Sequence of instructions stored inside computer
  * Build from predfeinded set of primitive instructions
    1. Arithmetic and logic
    2. Simple tests - Equals, not equals
    3. Moving data - storing or moving data
  * Special program (interperter) excutes each instruction in order
    * Use tests to change flow of control through sequence
    * Stop when done

## Basic primitives
* Allan Turing showed that you can compute anything using 6 primitives
* Modern programming languages have more convenient set of primitives
* Anything computable in one language is computable in any other programming languages

## Creating recipes
* A programming language provides a set of primitive operations
* Expressions are complex but legal combinations of primitives in a programming language
* Expressions adn computations have values and meaning in a programming language

## Aspects of languages
* Primitive constructs
  * English: Words
  * Programming language: Numbers, strings, simple, operators
* Static semantics is which syntactically valid strings have meaning
  * English: "I are hungry" - Syntactically valid, but static semantic errpr
  * Programming language: 3 + "hi" - Static semantic error
* Semantics is the meaning associated with a syntactically correct string of symbols with no static semantic errors

## WHere things go wrong
* Syntactic errors
* Static semantic errors
  * Some languages check for these before running a program
  * Can cause unpredictable behavior
* No semantic errrors byt different meaning than what programmer intended
  * Program crashes, stops running
  * Program runs forever
  * Program gives an answer but different than expected

## Python programs
* A program is a sequence of definitions and commands
  * definitions evaulated
  * Commands executed by Python interpreter in a shell
* Commands (statements) instruct interpreter to do something

## Objects
* Programs manipulate data objects
* Objects have a type that defines the kinds of things programs can do to them
* Everything is an object in Python. They are
  * Scalar (Can not be subdivived)
    * Int - Integers
    * Float - Real numbers
    * Bool - True/False
    * NoneType - Special and has one value, None
  * Non-scalar (Have internal structures that can be accessed)

## Expressions
* Combine objects and operators to from expressions
* An expression has a valu, which has a type
* Syntas for simple expression
  ```
  <object> <operator> <object>
  ```

## Operators on Int and floats
i + j - Sum
i - j - Difference
i * j - Product
i / j - division
i % j - Remainder
i ** j - i to the power of j

## Binding variables and values
* Equal sign is an assignment of a value to a variable name
* Value stored in a computer memory
* An assignment binds name to value
* Retrieve value associated with a name or variable by involking the name
* We give names to values of expressions so we can reuse names instead of values. Easier to change code later

## Changeing bindings
* Can re-bind variable names using new assignment statements
* Previous valuye may still stored in memory but lost the handle for it
* Value for variables does not change until you tell the computer to do the calculaton again
