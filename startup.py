from hwx import gui, inspire
from enum import Enum


# Global Variables
model = inspire.getModel()
model_name = model.name
model_parts = model.parts
number_parts = len(model_parts)
parts_vector = []
parts_map = {}
material_prices = {}


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


# Functions
def clean_data():
    parts_vector.clear()
    parts_map.clear()

def update_material_prices():
    # Update the material_prices dictionary with the current prices of materials
    for m in Material:
        # Interaction with the API
        ## TODO: set material prices from API
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

def get_name_parts():
    name_parts = ()
    for index in range(number_parts):
        part_name = (model_parts[index].name,)
        name_parts += part_name
    return name_parts

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


# GUI
# Widgets
verticalSpacer = gui.SpacerItem(20, 221, spacing = 'Vertical')

horizontalSpacer_2 = gui.SpacerItem(40, 20, spacing = 'Horizontal')

partLabel = gui.Label(
    parent = None,
    name = 'partLabel',
    text = 'PART',
    font = dict(size = 11, bold = True),
)
partLabel.SetAlignment(gui.hwui.ui.AlignCenter)

partNameLabel = gui.Label(
    parent = None,
    name = 'partNameLabel',
    text = 'Select part',
)

partName = gui.ComboBox(
    parent = None,
    name = 'partName',
    values = get_name_parts(),
)

partComponentLabel = gui.Label(
    parent = None,
    name = 'partComponentLabel',
    text = 'Component',
)

## TODO: set selected value with the component of the part
partComponent = gui.ComboBox(
    parent = None,
    name = 'partComponent',
    values = ('Core', 'Chiller', 'Riser', 'Sleeve', 'Overflow', 'Filter', )
)

partVolumeLabel = gui.Label(
    parent = None,
    name = 'partVolumeLabel',
    text = 'Volume',
)

## TODO: set text with the volume of the part
partVolume = gui.LineEdit(
    parent = None,
    name = 'partVolume',
    text = '0',
)

partMaterialLabel = gui.Label(
    parent = None,
    name = 'partMaterialLabel',
    text = 'Material',
)

## TODO: set selected value with the material of the part
partMaterial = gui.ComboBox(
    parent = None,
    name = 'partMaterial',
    values = ('Aluminium', 'Brass', 'Carbon_Steel', 'Cast_Iron', 'Cobalt', 'Copper', 'Gold', 'Magnesium', 'Nickel', 'Silver', 'Stainless', 'Steel', 'Tin', 'Titanium', 'Zamak', )
)

materialCostLabel = gui.Label(
    parent = None,
    name = 'materialCostLabel',
    text = 'Material cost (€/mt)',
)

## TODO: set text with the cost of the material selected
materialCost = gui.LineEdit(
    parent = None,
    name = 'materialCost',
    text = '0',
)

productionCostLabel = gui.Label(
    parent = None,
    name = 'productionCostLabel',
    text = 'Production cost',
)

productionCost = gui.LineEdit(
    parent = None,
    name = 'productionCost',
    text = '0',
)

isReusableLabel = gui.Label(
    parent = None,
    name = 'isReusableLabel',
    text = 'Is it reusable?',
)

isReusable = gui.CheckBox(
    parent = None,
    name = 'isReusable',
    text = '',
)

def onClickResetValuesButton(event):
  ## TODO: set default values on GUI
  gui.tellUser("Hello World")
  
resetValuesButton = gui.PushButton(
    parent = None,
    name = 'resetValuesButton',
    text = 'Reset values',
    command = onClickResetValuesButton,
)

horizontalSpacer_4 = gui.SpacerItem(40, 20, spacing = 'Horizontal')

partCostLabel = gui.Label(
    parent = None,
    name = 'partCostLabel',
    text = 'Part cost',
    font = dict(size = 9, bold = True),
)

## TODO: add to text the selected currency symbol
partCost = gui.Label(
    parent = None,
    name = 'partCost',
    text = '0',
    font = dict(size = 9, bold = True),
)
partCost.SetAlignment(gui.hwui.ui.AlignRight|gui.hwui.ui.AlignTrailing|gui.hwui.ui.AlignVCenter)

horizontalSpacer = gui.SpacerItem(40, 20, spacing = 'Horizontal')

modelLabel = gui.Label(
    parent = None,
    name = 'modelLabel',
    text = 'MODEL',
    font = dict(size = 11, bold = True),
)
modelLabel.SetAlignment(gui.hwui.ui.AlignCenter)

modelNameLabel = gui.Label(
    parent = None,
    name = 'modelNameLabel',
    text = 'Model name',
)

modelName = gui.Label(
    parent = None,
    name = 'modelName',
    text = model_name,
)

numberPartsLabel = gui.Label(
    parent = None,
    name = 'numberPartsLabel',
    text = 'Number of parts',
)

numberParts = gui.Label(
    parent = None,
    name = 'numberParts',
    text = number_parts,
)

currencyLabel = gui.Label(
    parent = None,
    name = 'currencyLabel',
    text = 'Select currency',
)

currency = gui.ComboBox(
    parent = None,
    name = 'currency',
    values = ('EUR (€)', 'USD ($)', 'GBP (£)', )
)

totalCostLabel = gui.Label(
    parent = None,
    name = 'totalCostLabel',
    text = 'Total cost',
    font = dict(size = 10, bold = True),
)

## TODO: add to text the selected currency symbol
totalCost = gui.Label(
    parent = None,
    name = 'totalCost',
    text = '0',
    font = dict(size = 10, bold = True),
)
totalCost.SetAlignment(gui.hwui.ui.AlignLeading|gui.hwui.ui.AlignLeft|gui.hwui.ui.AlignVCenter)

def init_data():
    clean_data()
    update_material_prices()
    number_parts = 1
    
    for index in range(number_parts):
        part_name = partName.value
        part_component = partComponent.value
        component_type = get_component_type(part_component)
        part_volume = float(partVolume.value)
        part_material = partMaterial.value
        material_type = get_material_type(part_material)
        material_cost = float(materialCost.value)
        part_production_cost = float(productionCost.value)
        part_reusable = isReusable.value
    
        part = Part(part_name, component_type, part_volume, material_type, part_production_cost, part_reusable)
        parts_vector.append(part)
        parts_map[part_name] = (part)

def calculate_costs():
    init_data()
    part = parts_map[partName.value]
    totalPartCost = str(total_cost_part(part))
    partCost.text = totalPartCost
    totalCostModel = str(total_cost_model())
    totalCost.text = totalCostModel

def onClickCalculateCostsButton(event):
    calculate_costs()
  
calculateCostsButton = gui.PushButton(
    parent = None,
    name = 'calculateCostsButton',
    text = 'Calculate costs',
    command = onClickCalculateCostsButton,
)

def onClickGenerateCostReportButton(event):
  ## TODO: generate cost report and download it
  gui.tellUser("Hello World")

generateCostReportButton = gui.PushButton(
    parent = None,
    name = 'generateCostReportButton',
    text = 'Generate cost report',
    command = onClickGenerateCostReportButton,
)

horizontalSpacer_3 = gui.SpacerItem(40, 20, spacing = 'Horizontal')

verticalSpacer_1 = gui.SpacerItem(20, 220, spacing = 'Vertical')

# Layouts
partNameHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        partNameLabel,
        partName,
    )
)

partComponentHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        partComponentLabel,
        partComponent,
    )
)

partVolumeHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        partVolumeLabel,
        partVolume,
    )
)

partMaterialHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        partMaterialLabel,
        partMaterial,
    )
)

materialCostHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        materialCostLabel,
        materialCost,
    )
)

productionCostHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        productionCostLabel,
        productionCost,
    )
)

isReusableHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        isReusableLabel,
        isReusable,
    )
)

resetAndPartCostHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        resetValuesButton,
        '<->',
        partCostLabel,
        partCost,
    )
)

partVerticalLayout = gui.VBoxLayout(
    spacing = 6,
    children = (
        partLabel,
        partNameHorizontalLayout,
        partComponentHorizontalLayout,
        partVolumeHorizontalLayout,
        partMaterialHorizontalLayout,
        materialCostHorizontalLayout,
        productionCostHorizontalLayout,
        isReusableHorizontalLayout,
        resetAndPartCostHorizontalLayout,
    )
)

modelNameHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        modelNameLabel,
        modelName,
    )
)

numberPartsHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        numberPartsLabel,
        numberParts,
    )
)

currencyHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        currencyLabel,
        currency,
    )
)

totalCostHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        totalCostLabel,
        totalCost,
    )
)

costsButtonsHorizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        calculateCostsButton,
        generateCostReportButton,
    )
)

modelVerticalLayout = gui.VBoxLayout(
    spacing = 6,
    children = (
        modelLabel,
        modelNameHorizontalLayout,
        numberPartsHorizontalLayout,
        currencyHorizontalLayout,
        totalCostHorizontalLayout,
        costsButtonsHorizontalLayout,
    )
)

horizontalLayout = gui.HBoxLayout(
    spacing = 6,
    children = (
        '<->',
        partVerticalLayout,
        '<->',
        modelVerticalLayout,
        '<->',
    )
)

verticalLayout = gui.VBoxLayout(
    spacing = 6,
    margin = 9,
    children = (
        '<->',
        horizontalLayout,
        '<->',
    )
)

# Dialog
QuickCost = gui.Dialog(caption = 'QuickCost'
, children = (verticalLayout,)
)


# #############################################################################


class ExtensionContext(inspire.gui.Context):
    def onFirstActivate(self):
        # TODO: Replace this dialog by your dialog
        self.dialog = QuickCost
        self.dialog.OnHide().Connect(self._onDialogHide)

    def onActivate(self):
        calculate_costs()
        self.dialog.show()

    def onDeactivate(self):
        self.dialog.hide()

    def _onDialogHide(self, event):
        self.pop()


# #############################################################################


# class CastingExtentionDialog(inspire.gui.Dialog):
#     def createContents(self):
#         self.SetCaption("Casting Extension")
#         inspire.gui.VBoxLayout(
#             parent=self,
#             children=("PAE ..."),
#         )


# #############################################################################
def startup():
    ribbon = gui.RibbonPage.get("Casting")
    gui.RibbonPageGroup(
        ribbon,
        children=[
            gui.SpriteActionGroup(
                children=[
                    gui.SpriteAction(
                        name="Casting.Extension",
                        icon="ribbonSleeveStrip-64.png",
                        context=ExtensionContext,
                    )
                ]
            )
        ],
    )


startup()
