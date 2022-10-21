from random import randint
from itertools import cycle

from model_bakery.recipe import Recipe

from dragon.models import Dragon, Location, Rider


dragon_names = [
    "Balerion",
    "Vhagar",
    "Meraxes",
    "Quicksilver",
    "Dreamfyre",
    "Vermithor",
    "Silverwing",
    "Meleys",
    "Caraxes",
    "Seasmoke",
    "Syrax",
    "Sunfyre",
    "Tessarion",
    "Vermax",
    "Arrax",
    "Moondancer",
    "Tyraxes",
]

dragon = Recipe(
    Dragon,
    name=cycle(dragon_names),
    power=lambda: randint(1, 100)
)

location_names = [
    "Dragonstone",
    "King's Landing",
]

location = Recipe(
    Location,
    name=cycle(location_names),
)

rider_names = [
    "Aegon",
    "Viserys I",
    "Rhaenyra",
    "Daemon",
    "Jon Snow",
    "Daenerys",
]

rider = Recipe(
    Rider,
    name=cycle(rider_names),
    power=lambda: randint(1, 100)
)
