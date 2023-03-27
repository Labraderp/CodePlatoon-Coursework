const resultsContainer = document.getElementById('results');

const names = ['Ben Cohen', 'Jason Statham', 'Adam Cahan', 'Pikaku Picachu'];

function onClickHandler() {
    for (const name of names) {
        const newListItem = document.createElement('li');
        newListItem.innerText = name;

        resultsContainer.append(newListItem);
    }
}