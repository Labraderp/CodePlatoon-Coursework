const input = document.getElementById('userinput');
const button = document.getElementById('submitbutton');
const guess_area = document.getElementById('guessbox');

let answer = rngen();
console.log(answer);

button.addEventListener('click', e => {
    if (!isNaN(input.value)) {
        validate_answer(input.value);
    } else {
        console.log("Must use integer values only!");
    }
    input.value = "";
})

function validate_answer(input) {
    if(input === '') {
        console.log("Can't use an empty submission!");
        return;
    } else {
        const node = document.createElement("li");
        node.append(input);

        if(input == answer) {
            alert("YOU WIN!");
            return;
        } else if(input > answer) {
            alert("Input is too high!");
            guess_area.appendChild(node);
            console.log(guess_area);
        } else {
            alert("Input is too low!");
            guess_area.appendChild(node);
            console.log(guess_area);
        } 
    }
}

function rngen() {
    number = Math.floor((Math.random() * 100)+1);
    return number;
}