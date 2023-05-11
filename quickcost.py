from enum import Enum

"""Clases"""
class Currency(Enum):
    EUR = 1
    USD = 2
    GBP = 3

class Component(Enum):
    Core = 1
    Chiller = 2
    Riser = 3
    Sleeve = 4
    Overflow = 5
    Filter = 6

class Material(Enum):
    Aluminium = 1
    Brass = 2
    Carbon-Steel = 3
    Cast-Iron = 4
    Cobalt = 5
    Copper = 6
    Gold = 7
    Magnesium = 8
    Nickel = 9
    Silver = 10
    Stainless = 11
    Steel = 12
    Tin = 13
    Titanium = 14
    Zamak = 15

class Part:
    def __init__(self, name, component, volume, material, production_cost):
        self.name = name
        self.component = component
        self.volume = volume
        self.material = material
        self.production_cost = production_cost

    def get_name(self):
        return self.name
    
    def get_component(self):
        return self.component

    def get_volume(self):
        return self.volume

    def get_material(self):
        return self.material

    def get_production_cost(self):
        return self.production_cost

    def get_is_reusable(self):
        return self.is_reusable

    def set_name(self, name):
        self.name = name

    def set_component(self, component):
        self.component = component

    def set_volume(self, volume):
        self.volume = volume

    def set_material(self, material):
        self.material = material

    def set_production_cost(self, production_cost):
        self.production_cost = production_cost

    def set_is_reusable(self, is_reusable):
        self.is_reusable = is_reusable

    def __str__(self):
        return self.name + ' ' + str(self.volume) + ' ' + self.material + ' ' + str(self.material_cost) + ' ' + str(self.production_cost) + ' ' + str(self.is_reusable)


"""Variables globales"""
material_prices = {}
parts = []

"""Funciones"""
"""
def update_prices():
    ""Actualiza el diccionario de precios con los valores del diccionario m.""

    for m in Material:
        ""AQUÍ LA INTERACCIÓ AMB LA API""
"""

def part_cost(p: Part) -> float:
    """Calcula el màxim de dos enters."""
    comp = p.get_component()
    if comp == 'Chiller' or comp == 'Riser' or comp == 'Overflow':
        return float(p.get_volume() * material_prices[p.get_material()])

    elif comp == 'Core' or comp == 'Sleeve' or comp == 'Filter':
        return float(p.get_volume() * material_prices[p.get_material()] + p.get_production_cost)

    else:
        return -1


def estimated_part_cost(p: Part) -> float:
    """Calcula el màxim de dos enters."""

    return p.get_volume() * material_prices[p.get_material()] * 2


material_name = str(input('Introduzca el nombre del material: '))
material_cost = int(input('Introduzca el precio por tonelada del material: '))

select_part = str(input('Introduzca el nombre de la pieza: '))
part_volume = int(input('Introduzca el volumen: '))
part_material = str(input('Introduzca el material: '))

production_cost = int(input('Introduzca el volumen: '))
is_reusable = bool(input('Es reusable?: '))
part_cost

number_of_units
number_of_parts
currency

def total_cost() -> float:
    """Calcula el coste total de la pieza"""

    total_cost = 0

    for part in parts:
        total_cost += estimated_part_cost(part)

    return total_cost




part1 = Part('part1', 10, 'aluminium', 100, True)