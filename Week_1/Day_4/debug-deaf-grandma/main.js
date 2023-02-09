

function main() {
    let run = true;
    let goodbyes = 0;

    while(run) {
        console.log("We did it, chat!");
        let userInput = prompt("HEY KID!");
        
        if ( userInput == "GOODBYE!" ) {
            goodbyes++;

            if ( goodbyes == 1 ) {
                alert("LEAVING SO SOON?");
            }
            else if ( goodbyes == 2 ) {
                alert("LATER, SKATER!");
                run = false;
            }
        }
        else if ( userInput == "" ) {
            alert("WHAT!?");
        }
        else if ( userInput.toUpperCase() == userInput ) {
            alert('NO, NOT SINCE 1946!')
        }

        else {
            alert("SPEAK UP, KID!");
        }
    }
}

main();