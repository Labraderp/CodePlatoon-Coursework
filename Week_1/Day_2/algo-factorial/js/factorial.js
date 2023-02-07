exports.factorial = function(num) {
    if(num === 1) {
        return num;
    } else {
        return num * exports.factorial(num-1);
    }
};