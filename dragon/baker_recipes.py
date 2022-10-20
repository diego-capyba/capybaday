from itertools import cycle

from model_bakery import baker
from model_bakery.recipe import Recipe

from dragon.models import Dragon


dragon_names = [
    'Balerion',
    'Vhagar',
    'Meraxes',
    'Quicksilver',
    'Dreamfyre',
    'Vermithor',
    'Silverwing',
    'Meleys',
    'Caraxes',
    'Seasmoke',
    'Syrax',
    'Sunfyre',
    'Tessarion',
    'Vermax',
    'Arrax',
    'Moondancer',
    'Tyraxes',
]

dragon = Recipe(
    Dragon,
    name=cycle(dragon_names),
)
