/*
    textCheck(string): Takes a response and generates a flag based on the string read in. There are four cases.
        - If blank (nothing typed in), returns 'blank' flag
        - If "GOODBYE!", returns 'bye' flag
        - If some other response in UPPERCASE, returns 'upper' flag
        - If not uppercase, returns 'lower' flag

    Each flag is used in the switch block
*/

function textCheck(input) {
    if(input === '') {
        return 'blank';
    }

    if(input === 'GOODBYE!') {
        return 'bye'
    }

    if(input === input.toUpperCase()) {
        return 'upper';
    }

    //SPEAK UP
    return 'lower';
}

function deaf_gma(input) {
    let flag = textCheck(input);
    switch(flag) {
        case 'blank':
            let blank_resp = prompt("WHAT?!");
            deaf_gma(blank_resp);
            break;
        case 'bye':
            if(input === "GOODBYE!") {                      //if GOODBYE!
                let bye_resp = prompt("LEAVING SO SOON?");      //Save prompt
                if(bye_resp === "GOODBYE!") {                   //If second GOODBYE!
                    alert("LATER, SKATER!");
                    break;                                  //You're done
                } else {                                    //otherwise
                    deaf_gma(bye_resp);                         //start again
                    break;
                }
            }
        
        case 'lower':
            let lower_resp = prompt("SPEAK UP, KID!");
            deaf_gma(lower_resp);
            break;

        case 'upper':
            let upper_resp = prompt("NO, NOT SINCE 1946!");
            deaf_gma(upper_resp);
            break;
    }
}

function main() {
    let input = prompt("HEY KID!");
    deaf_gma(input);
}

main();