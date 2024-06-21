import folium

from django.http import HttpResponseNotFound, HttpRequest
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
from django.utils.timezone import localtime

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.filter(appeared_at__lt=localtime(), disappeared_at__gt=localtime())

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.img.url)
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.img.url),
            'title_ru': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = {'pokemon_id': pokemon.id,
                                 'img_url': request.build_absolute_uri(pokemon.img.url),
                                 'title_ru': pokemon.title_ru,
                                 'title_jp': pokemon.title_jp,
                                 'title_en': pokemon.title_en,
                                 'description': pokemon.description}
            if pokemon.previous_evolution:
                requested_pokemon['previous_evolution'] = {"title_ru": pokemon.previous_evolution.title_ru,
                                                           "pokemon_id": pokemon.previous_evolution.id,
                                                           "img_url": request.build_absolute_uri(
                                                               pokemon.previous_evolution.img.url)}
            if pokemon.next_evolutions.first():
                requested_pokemon['next_evolution'] = {"title_ru": pokemon.next_evolutions.first().title_ru,
                                                       "pokemon_id": pokemon.next_evolutions.first().id,
                                                       "img_url": request.build_absolute_uri(
                                                           pokemon.next_evolutions.first().img.url)}
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    requested_pokemon_entities = PokemonEntity.objects.filter(pokemon_id=requested_pokemon['pokemon_id'],
                                                              appeared_at__lt=localtime(), disappeared_at__gt=localtime())
    for pokemon_entity in requested_pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(requested_pokemon['img_url'])
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': requested_pokemon,
    })
