exports.creditCheck = function(str) {
    let str_arr = (str.split('')).reverse();        //read string in reverse, easier
    num_arr = (str_arr.map((num) => parseInt(num) * 2)); //double all -- WRONG, NEED TO DO OVER

    for (num in num_arr) {
        if (num % 2 === 1){
            if(num_arr[num] >= 10) {
                num_arr[num] -= 9;
            }
        }
    }
    console.log(num_arr)
    const sum = num_arr.reduce((acc, tot) => acc + tot, 0);
    console.log(sum)
    if(sum % 10 == 0) {
        return 'The number is valid!'
    } else {
        return 'The number is invalid!'
    }
}
