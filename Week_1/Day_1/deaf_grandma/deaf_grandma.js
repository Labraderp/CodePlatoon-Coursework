/*
    textCheck(string): Takes a response and generates a flag based on the string read in. There are four cases.
        - If blank (nothing typed in), returns 'blank' flag
        - If "GOODBYE!", returns 'bye' flag
        - If some other response in UPPERCASE, returns 'upper' flag
        - If not uppercase, returns 'lower' flag

    Each flag is used in the switch block
*/

function textCheck(input) {
    //Checks for no input
    if(input === '') {
        return 'blank';
    }
    //Checks for "GOODBYE!"
    if(input === 'GOODBYE!') {
        return 'bye'
    }
    //Checks for ALL CAPS INPUT that isn't GOODBYE!
    if(input === input.toUpperCase()) {
        return 'upper';
    }
    //Assumes lowercase/not a word final answer
    return 'lower';
}

function deaf_gma(input) {
    let flag = textCheck(input);        //'blank', 'bye', 'upper', 'lower'
    
    switch(flag) {
        //flag === blank
        case 'blank':
            let blank_resp = prompt("WHAT?!");
            deaf_gma(blank_resp);
            break;
        
        //flag === bye
        case 'bye':
            if(input === "GOODBYE!") {                      
                let bye_resp = prompt("LEAVING SO SOON?");
                //If second prompt === "GOODBYE!", posts alert without user input.
                if(bye_resp === "GOODBYE!") {                  
                    alert("LATER, SKATER!");
                    break;                                 
                } else {
                    deaf_gma(bye_resp);
                    break;
                }
            }
        //flag === lower
        case 'lower':
            let lower_resp = prompt("SPEAK UP, KID!");
            deaf_gma(lower_resp);
            break;
        //flag === upper
        case 'upper':
            let upper_resp = prompt("NO, NOT SINCE 1946!");
            deaf_gma(upper_resp);
            break;
    }
}

function lowercase_check(input) {
    console.log(`Lowercase check came back as ${/[a-z]/.test(input)}`);
    return /[a-z]/.test(input);
    
}

function regex_grandma(input) {
    //Check for blank input
    if(input === '') {
        let resp = prompt("WHAT?!");
        return regex_grandma(resp);
    }
    //Check for GOODBYE!
    if(input === 'GOODBYE!') {
        let resp = prompt("LEAVING SO SOON?");
        //Conditionals for potential responses in the nested prompt
        switch(resp) {
            case 'GOODBYE!':                        //Check for GOODBYE!
                return alert("LATER, SKATER!");
            case '':                                //Check for blank
                resp = prompt("WHAT?!");
                return regex_grandma(resp);
            default:
                if(lowercase_check(resp) === true) {
                    resp = prompt("SPEAK UP!");
                    return regex_grandma(resp);
                } else {
                    resp = prompt("NO, NOT SINCE 1946!");
                    return regex_grandma(resp);
                }
        }
    }
    //Check for lowercase characters
    if(lowercase_check(input)) {
        let resp = prompt("SPEAK UP, KID!");
        return regex_grandma(resp);
    }
    //Default to UPPERCASE but not GOODBYE!
    let resp = prompt("NO, NOT SINCE 1946!");
    return regex_grandma(resp);
}

function main() {
    let input = prompt("HEY KID!");
    regex_grandma(input);
}

main();

/**
function main() {
    let input = prompt("HEY KID!");
    deaf_gma(input);
}

main();
**/