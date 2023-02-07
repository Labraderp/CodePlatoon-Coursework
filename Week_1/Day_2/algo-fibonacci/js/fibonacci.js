const fibonacci = (num) => {
    let fib_arr = [0, 1];

    if(num === 0 || num === 1) {
        return fib_arr[num];
    } else {
        let counter = 2;
        while(counter <= num) {
            let last_index = fib_arr.length-1;
            fib_arr.push(fib_arr[last_index]+fib_arr[last_index-1]);
            counter++;
        }
        return fib_arr[fib_arr.length-1];
    }
}

module.exports = {fibonacci}
