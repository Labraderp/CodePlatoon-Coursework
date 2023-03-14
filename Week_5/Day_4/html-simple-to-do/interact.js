const add_item = document.getElementById('add_button');
const remove_item = document.getElementById('remove_button');
const delete_item = document.getElementsByClassName('delete_button');
const input_field = document.getElementById('input_field');

let text = "testing list";
let serial = 1;``

add_item.addEventListener('click', a => {
    console.log('Hello world!');
    text = input_field.value;
    create_item(text);
});

function create_item(text) {
    let node = document.createElement('li');
    node.id = text + '_list_item_' + serial;
    serial++;
    
    let delete_button = document.createElement('button');
    delete_button.appendChild(document.createTextNode('delete'));
    delete_button.class = 'delete_button';

    let complete_button = document.createElement('button');
    complete_button.appendChild(document.createTextNode('complete'));
    complete_button.class = 'complete_button';
    
    node.appendChild(document.createTextNode(text));
    node.appendChild(delete_button);
    node.appendChild(complete_button);
    
    delete_button.addEventListener('click', a => {
        let list = document.getElementById('list_holder');
        item = document.getElementById(node.id);
        list.removeChild(item);
    });

    complete_button.addEventListener('click', a => {
        item = document.getElementById(node.id);
        item.class = 'completed';
        console.log(item.class);
    });

    document.querySelector('ol').appendChild(node);
    // document.body.appendChild(tag);
}