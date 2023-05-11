precios_productos = {}

def actualizar_precios(pp: dict) -> dict:
    """Actualiza el diccionario de precios con los valores del diccionario m."""
    """precios_productos.update(m)"""
    return pp

class Part:
    def __init__(self, name, volume, material, production_cost, is_reusable):
        self.name = name
        self.volume = volume
        self.material = material
        self.production_cost = production_cost
        self.is_reusable = is_reusable

    def get_name(self):
        return self.name

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

def coste_parte(p: Part) -> float:
"""Calcula el màxim de dos enters."""

    return float(p.get_volume() * precios_productos[p.get_material()] + p.get_production_cost())



def coste_parte(p: Part) -> float:
"""Calcula el màxim de dos enters."""

    return p.get_volume() * p.get_material_cost() + p.get_production_cost()


select_part = str(input('Introduzca el nombre de la pieza: '))
part_volume = int(input('Introduzca el volumen: '))
part_material = str(input('Introduzca el material: '))
material_cost = int(input('Introduzca el precio por tonelada del material: '))
production_cost = int(input('Introduzca el volumen: '))
is_reusable = bool(input('Es reusable?: '))
part_cost

number_of_units
number_of_parts
currency
total cost