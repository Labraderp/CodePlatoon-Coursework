var arm = require("./armstrongNumbers");
var shallowEqualArrays = require('shallow-equal/arrays');

function createArrayOfNum(maxValue) {
  return Array.apply(null, {length: maxValue}).map(Number.call, Number)
}

console.log(shallowEqualArrays(arm.findArmstrongNumbers([0]),[0]));
console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(8)), [0, 1, 2, 3, 4, 5, 6, 7]));
console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(99)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]));
console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(999)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]));
