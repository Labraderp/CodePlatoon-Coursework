const arrayToSearchThrough = [];
for (let i = 1; i <= 1000; i++) {
    arrayToSearchThrough.push(i);
}

exports.linearSearch = function(valueToFind, arrayToSearchThrough) {
    let index = 0;
    while(index < arrayToSearchThrough.length) {
        if(arrayToSearchThrough[index] === valueToFind) {
            return index;
        }
        index++
    }
    return undefined
};

exports.linearSearchGlobal = function(valueToFind, arrayToSearchThrough) {
    let result = [];
    let index = 0;

    while(index < arrayToSearchThrough.length){
        if(arrayToSearchThrough[index] === valueToFind) {
            result.push(index);
        }
        index++;
    }
    return result;
};