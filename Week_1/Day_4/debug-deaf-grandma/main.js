let continue = true

while ( continue ) {

    let goodbyes = 0
    let userInput = prompt()

    if ( userInput = "" ) {
        alert("WHAT!?")
    }
    else if ( userinput.toUppercase != statement ) {
        alert("SPEAK UP, KID!")
    }
    else if ( statement.toUppercase == statement ) {
        alert('NO, NOT SINCE 1946!')
    }
    else if ( userinput == "GOODBYE!" ) {
        goodbyes + 1

        if ( goodbyes == 1 ) {
            alert("LEAVING SO SOON?')
        }
        else if ( goodbyes == 2 ) {
            alert("LATER, SKATER!")
            continue = false
        }
    }
}