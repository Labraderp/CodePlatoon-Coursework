const padArray = require("./padArray")
const pad = padArray.pad

// Curious? Check out the source code for shallow-equal: https://github.com/moroshko/shallow-equal/blob/master/src/arrays.js
// It's friendly! And - Check out its npmjs package page: https://www.npmjs.com/package/shallow-equal
const shallowEqualArrays = require('shallow-equal/arrays')

// JS Tip: `null` vs `undefined` in JS: https://stackoverflow.com/questions/5076944/what-is-the-difference-between-null-and-undefined-in-javascript
console.log(shallowEqualArrays(pad([1,2,3], 5), [1,2,3, null, null]))
console.log(shallowEqualArrays(pad([1,2,3], 5, 'apple'), [1,2,3, 'apple', 'apple']))
console.log(shallowEqualArrays(pad([1,2,3], 3), [1,2,3]))

// Challenge - what edge case do we NOT have tests for? Add a test for it, and any other tests you think will increase our test coverage
// for the possible valid inputs our program might receive.
