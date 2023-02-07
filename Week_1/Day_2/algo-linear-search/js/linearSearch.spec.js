//import linearSearch module from linearSearch.js
var ls = require("./linearSearch"); 

//helper function that compares 2 arrays and returns `true` if the lists are equivalent
const compareArrays = (array1, array2) => {
    array1 = [...new Set(array1)]
    if (array1.length != array2.length){
        return false
    }
    for (let index = 0; index < array1.length; index++) {
        const element = array1[index];
        if (!array2.includes(element) ){
            return false
        }
    }
    return true
}

// tests for linearSearch
console.log(ls.linearSearch(3, [1,2,3]) === 2);
console.log(ls.linearSearch(4, [1,2,3]) === undefined);
console.log(ls.linearSearch(13, [1,2,3]) === undefined);

// tests for linearSearchGlobal
console.log(compareArrays(ls.linearSearchGlobal("a", ["b", "a", "n", "a", "n", "a", "s"]), [1, 3, 5]))
console.log(compareArrays(ls.linearSearchGlobal("s", ["b", "a", "n", "a", "n", "a", "s"]), [6]))
console.log(compareArrays(ls.linearSearchGlobal("n", ["b", "a", "n", "a", "n", "a", "s"]), [2, 4]))

