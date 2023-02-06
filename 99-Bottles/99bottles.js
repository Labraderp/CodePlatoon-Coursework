// Write a program that can print the song "99 Bottles of Beer"
function bottles99(){
    for (let i = 99; i >1; i--) {
        let next = i-1
        console.log(`${i} Bottles of beer on the wall, ${i} bottles of beer!\nTake one down, pass it around, ${next} bottles of beer on the wall!`);
    }

    console.log("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.");
    console.log("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.");
}

function bottles_any(num) {
    while(num>1) {
        console.log(`${num} bottles of beer on the wall, ${num} bottles of beer.\nTake one down and pass it around, ${num-1} bottles of beer on the wall.`);
        num -= 1;
    }
    
    console.log(`${num} bottles of beer on the wall, ${num} bottles of beer!\nTake one down and pass it around, ${num-1} bottles of beer on the wall!`);
    console.log('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.');
}

bottles_any(5);