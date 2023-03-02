const dog_img = document.querySelector("#dog");
const squ_img = document.querySelector("#squidward");
const walt_img = document.querySelector("#walter");
const squ_img2 = document.querySelector("#squidward2");
const squ_img3 = document.querySelector("#squidward3");
const squ_img4 = document.querySelector("#squidward4");
const inverter = document.querySelector("#invert-button");

inverter.addEventListener('click', e => {
    holder = document.getElementsByClassName('imageholder');
    console.log(holder);

    for (let i = holder.length - 1; i >= 0; i--) {
        replaceImages(holder[i]);
    }
});

function replaceImages(e) {
    const alt_text = document.createTextNode(e.alt);
    const parentDiv = e.parentNode;
    console.log(e);
    parentDiv.replaceChild(alt_text, e);
}