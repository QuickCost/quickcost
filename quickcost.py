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
    Carbon_Steel = 3
    Cast_Iron = 4
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
    def __init__(self, name: str, component: Component, volume: float, material: Material, production_cost: float):
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

    def __str__(self):
        return f'Name: {self.name}, Component: {self.component}, Volume: {self.volume}, Material: {self.material}, Production Cost: {self.production_cost}'


"""Variables globales"""
material_prices = {}
parts_vector = []
parts_map = {}

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


def total_cost() -> float:
    """Calcula el coste total de la pieza"""

    total_cost = 0

    for part in parts_vector:
        total_cost += estimated_part_cost(part)

    return total_cost



"""Programa principal"""
material_name = str(input('Introduzca el nombre del material: '))
material_cost = int(input('Introduzca el precio por tonelada del material: '))

select_part = str(input('Introduzca el nombre de la pieza: '))
component_type = str(input('Introduzca el tipo de componente: '))
part_volume = int(input('Introduzca el volumen: '))
part_material = str(input('Introduzca el material: '))

production_cost = int(input('Introduzca el volumen: '))
"""is_reusable = bool(input('Es reusable?: '))"""
part1 = Part(select_part, component_type, part_volume, part_material, production_cost)
"""parts_vector.append(Part(select_part, component_type, part_volume, part_material, production_cost))"""
"""parts_map[select_part] = (Part(select_part, component_type, part_volume, part_material, production_cost))"""
part_cost = part_cost(part1)
print(part_cost)

number_of_units = int(input('Introduzca el numero de unidades: '))
number_of_parts = int(input('Introduzca el numero de partes: '))
currency = Currency(input('Introduzca la moneda: '))
total_cost = total_cost()
print(total_cost)
