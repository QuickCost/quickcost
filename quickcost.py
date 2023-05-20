from enum import Enum

# Classes
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
    def __init__(self, name: str, component: Component, volume: float, material: Material, production_cost: float, reusable: bool):
        self.name = name
        self.component = component
        self.volume = volume
        self.material = material
        self.production_cost = production_cost
        self.reusable = reusable

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
    
    def is_reusable(self):
        return self.reusable

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
    
    def set_reusable(self, reusable):
        self.reusable = reusable

    def __str__(self):
        return f'Name: {self.name}, Component: {self.component}, Volume: {self.volume}, Material: {self.material}, Production Cost: {self.production_cost}, Reusable: {self.reusable}'


# Global Variables
material_prices = {}
parts_vector = []
parts_map = {}


# Functions
def update_material_prices():
    # Update the material_prices dictionary with the current prices of materials

    for m in Material:
        # Interaction with the API
        if m == Material.Aluminium:
            material_prices[m] = 1
        elif m == Material.Brass:
            material_prices[m] = 1
        elif m == Material.Carbon_Steel:
            material_prices[m] = 1
        elif m == Material.Cast_Iron:
            material_prices[m] = 1
        elif m == Material.Cobalt:
            material_prices[m] = 1
        elif m == Material.Copper:
            material_prices[m] = 1
        if m == Material.Gold:
            material_prices[m] = 1
        elif m == Material.Magnesium:
            material_prices[m] = 1
        elif m == Material.Nickel:
            material_prices[m] = 1
        elif m == Material.Silver:
            material_prices[m] = 1
        elif m == Material.Stainless:
            material_prices[m] = 1
        elif m == Material.Steel:
            material_prices[m] = 1
        elif m == Material.Tin:
            material_prices[m] = 1
        elif m == Material.Titanium:
            material_prices[m] = 1
        elif m == Material.Zamak:
            material_prices[m] = 1

def get_component_type(part_component: str) -> Component:
    if part_component == "Core":
        return Component.Core
    elif part_component == "Chiller":
        return Component.Chiller
    elif part_component == "Riser":
        return Component.Riser
    elif part_component == "Sleeve":
        return Component.Sleeve
    elif part_component == "Overflow":
        return Component.Overflow
    elif part_component == "Filter":
        return Component.Filter

def get_material_type(part_material: str) -> Material:
    if part_material == "Aluminium":
        return Material.Aluminium
    elif part_material == "Brass":
        return Material.Brass
    elif part_material == "Carbon_Steel":
        return Material.Carbon_Steel
    elif part_material == "Cast_Iron":
        return Material.Cast_Iron
    elif part_material == "Cobalt":
        return Material.Cobalt
    elif part_material == "Copper":
        return Material.Copper
    elif part_material == "Gold":
        return Material.Gold
    elif part_material == "Magnesium":
        return Material.Magnesium
    elif part_material == "Nickel":
        return Material.Nickel
    elif part_material == "Silver":
        return Material.Silver
    elif part_material == "Stainless":
        return Material.Stainless
    elif part_material == "Steel":
        return Material.Steel
    elif part_material == "Tin":
        return Material.Tin
    elif part_material == "Titanium":
        return Material.Titanium
    elif part_material == "Zamak":
        return Material.Zamak

def total_cost_part(p: Part) -> float:
    # Calculate the cost of the part
    comp = p.get_component()
    if comp == Component.Chiller or comp == Component.Riser or comp == Component.Overflow:
        return float(p.get_volume() * material_prices[p.get_material()])

    elif comp == Component.Core or comp == Component.Sleeve or comp == Component.Filter:
        return float(p.get_volume() * material_prices[p.get_material()] + p.get_production_cost())

    else:
        return -1

def estimated_cost_part(p: Part) -> float:
    # Calculate the estimated cost of the part
    return float(p.get_volume() * material_prices[p.get_material()] * 2)

def total_cost_model() -> float:
    # Calculate the total cost of the model
    total_cost = 0

    for part in parts_vector:
        total_cost += total_cost_part(part)

    return total_cost


# Main Program
update_material_prices()

model_name = str(input('Enter the name of the model: '))
currency = str(input('Enter the currency: '))
number_parts = int(input('Enter the total number of parts: '))

for index in range(number_parts):
    print('Part', index + 1, ':')

    part_name = str(input('Enter the name of the part: '))
    part_component = str(input('Enter the type of component: '))
    component_type = get_component_type(part_component)
    part_volume = int(input('Enter the volume: '))
    part_material = str(input('Enter the name of the material: '))
    material_type = get_material_type(part_material)
    material_cost = int(input('Optional: Enter the price per ton of the material: '))
    part_production_cost = int(input('Enter the production cost: '))
    part_reusable = bool(input('Is it reusable?: '))
    
    part = Part(part_name, component_type, part_volume, material_type, part_production_cost, part_reusable)
    parts_vector.append(part)
    parts_map[part_name] = (part)

    part_cost = total_cost_part(part)

    print('The cost of the part', part.get_name(), 'is:', part_cost, currency)
    print('-' * 50)

total_cost = total_cost_model()
print('The total cost of the model', model_name, 'is:', total_cost, currency)
print('-' * 100)
