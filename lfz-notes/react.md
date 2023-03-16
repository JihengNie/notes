# React Notes
## React Elements
* React is a JavaScript library for creting user interphase
* The Documnet Object Model (DOM) is a model (representation) of the document (HTML) with JavaScript objects. It is arranged in a tree, aka DOM Tree, like structure with showing the relationships of the elements with each other
* A react element is an object that represents a DOM node (or a single point in the DOM Tree)
* In order to mount a React element to the DOM:
  * We need to query the DOM
  * Create a DOM Root, which is like the starting point for when a branch grows from a tree
  * Then we use the react render method with the react element as an arguement

## JSX
* JSX is a JavaScript syntax extension that is used with React to describe what the user interphase should look like
* JSX requires React to be imported because it directly calls React.createElement method
* JSX is essentially used to make writing react code similar in appearence to HTML

## React function components
* A react component is like a puzzle piece. It allows us to split the user interphase into
independent, reusable pieces, and think about each piece in isolation. They are like JS functions
* In order to use a component, we would need to import the component and then call it
