from django.shortcuts import render
import requests
import json
import pprint
import random

pp = pprint.PrettyPrinter(indent=2, depth=2)

def pokemon_picker(val):
    endpoint = f"https://pokeapi.co/api/v2/pokemon/{val}"
    response = requests.get(endpoint)
    return json.loads(response.content)

def index(request):
    return render(request, 'form.html')

def pick(request):
    pokemon_name = request.POST.get('pokemon_name')
#Getting JSON data
    pokemon_data = pokemon_picker(pokemon_name)
#Pull sprites
    img_url = pokemon_data['sprites']['front_default']
    data = {
        'pokemon_name' : pokemon_name,
        'img' : img_url
    }
    return render(request, 'pokemon.html', data)

def randomize(request):
        data = {'pokemons' : []}

        count = 0
        while count < 6:
            id = random.randint(1, 1008)
        
            pokemon_data = pokemon_picker(id)  
            img_url = pokemon_data['sprites']['front_default']
            pokemon_name = pokemon_data['species']['name']
            
            data['pokemons'].append(
                 {
                'pokemon_name' : pokemon_name,
                'img' : img_url
                }
                )

            count += 1

        pp.pprint(data)
        return render(request, 'pokemon.html', data)
