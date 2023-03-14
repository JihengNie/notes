# JavaScript Syntaxs
## Conditional Statements
```js
const name = 'Jiheng Nie'

if (name === 'Jiheng Nie') {
  console.log('Name is Jiheng Nie')
} else if (name === 'Peter Parker') {
  console.log('Name is spiderman')
} else {
  console.log('Name is not Jiheng Nie or Peter Parker')
}
```
* Condtionals are checking a condition.
* if condition is true, then the code in the code block, which is the code sourrouned by the curly braces {}, will execute.


## For loops
```js
const grades = [80, 95, 100, 50]

for (let i = 0; i < grades.length; i++) {
  console.log(grades[i])
}

// Syntax
for (initialization; condition; final expression) {

}
```
* This is a for loop with a initialization, condition, and final expression
* The initialization is evaluated at the beginning, before the loop starts
* The condition is evaluated at the beginning of each iteration. This is checked before the code in the loop is ran
* The final expression is ran at the end of each iteration and before the next condition evaluation

## While loop
```js
const grades = [80, 95, 100, 50]
let i = 0
while (i < grades.length) {
  console.log(grades[i])
  i++
}

// Syntax
while (condition) {

}

```

* The while loop checks the condition at the beginning of each loop
  * If the condition is true, we run the code, else, we exit the loop

## Data Structures
### Objects
```js
// Objects

const object = {
  age: 25,
  name: 'Jiheng Nie'
}

// Syntax

const object = {
  property: value
}

// Notes
object.age // 25
object['age'] // 25
```

### Arrays
```js
const array = [80, 95, 100, 50]
// Notes
array[0] //80
array[3] // 50
array[10] // undefined
```

# JavaScript Forms
```js
event.preventDefault()
// This method prevents the default behavior of the event.
// With JS forms, the default behavior of form submission is to refresh the page
```
We should use the name attribute for all of the forms we create

# JavaScript Primitives
```js
const string = 'string' // String is a series of letters and symbols
const number = 12 // These are integers and real numbers
const boolean = True // These are True or False
undefined // This is JS's way of letting us know something is defined or does not exist
null // Similar to undefined, but it is a way for us to store something
//that does not exist or intentiopnal left empty
const object = {
  name: 'Jiheng',
  age: 25
} // Everything in JS are objects, that is strings, arrays, and objects
```
