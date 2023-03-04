const get_button = document.getElementById('getbtn');
const base_url = 'https://pokeapi.co/api/v2/';
const test_url = 'https://pokeapi.co/api/v2/pokemon/727/';

get_button.addEventListener('click', a => {
    // 1: Get original pokemon
    org_pkmn_url = pokemon_search();
    // 2: Display its sprite
    show_pokemon(org_pkmn_url);
    // 3: Get types of original pokemon
    let type_list = get_types(org_pkmn_url);
    // 4: Create dictionary of pokemon with shared types
    get_similar(type_list);
    // 5: Randomly pick five of those pokemon
    // 6: Display pokemon sprites
    // for(pkmn in pkmn_dict) {
    //     get_pokemon(pkmn);
    //     show_pokemon(pkmn);
    // }
});

// ================= AXIOS- FUNCTIONS ================= //
function show_pokemon(pokemon_url) {
    axios.get(pokemon_url)
    .then(function (pokemon) {
        image = pokemon.data.sprites.front_default;
        tag = document.createElement('img');
        tag.src = image;
        document.body.appendChild(tag);;
    })
    .catch(function (error) {
        console.log(error);
    })
    .finally(function () {
    });
}

function get_types(pokemon_url) {
    let new_arr = [];

    axios.get(pokemon_url)
    .then(function (pokemon) {
        type_list = pokemon.data.types;
        if(type_list.length == 1) {
            new_arr.push(type_list[0].type.url);
        } else {
            new_arr.push(type_list[0].type.url);
            new_arr.push(type_list[1].type.url);
        }
    })
    .catch(function (error) {
        console.log(error);
    })
    .finally(function () {
    });
    return new_arr;
}

// ================= HELPER FUNCTIONS ================= //
function rng(num) {
    rng_num = Math.floor((Math.random() * num) + 1);
    return rng_num;
}

function pokemon_search() {
    rng_num = rng(1007);
    returned_url = base_url + 'pokemon/' + rng_num + '/';
    return returned_url;
}

function get_similar(type_list) {
    console.log(type_list);
//     console.log(type_list);
    
//     axios.get(type_list)
//     .then(function (type) {
//         console.log(type);
//     })
//     .catch(function (error) {
//         console.log(error);
//     })
//     .finally(function () {
//     });
}