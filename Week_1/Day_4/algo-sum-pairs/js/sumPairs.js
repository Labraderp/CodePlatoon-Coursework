exports.sum_pairs = function(num_arr, desired_num) {
    sol_arr = [];

    for (let i  = 0; i < num_arr.length-1; i++) {
        for (let j = i+1; j < num_arr.length; j++) {
            if(num_arr[i] + num_arr[j] === desired_num) {
                sol_arr.push([num_arr[i], num_arr[j]]);
            }
        }
    }
    //       i 
    // 1 2 3 4 5
    //         j 
    if (sol_arr.length === 0) {
        return 'unable to find pairs'
    } else {
        return sol_arr;
    }
};
