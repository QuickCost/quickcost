from hwx import gui, inspire
from enum import Enum
import requests

# Global Variables
model = inspire.getModel()
model_name = model.name
model_parts = model.parts
number_parts = len(model_parts)
parts_vector = []
parts_map = {}
material_prices = {}
selectedCurrency = "EUR (€)"


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
    CastPart = 7

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
    NA = 16

class Part:
    def __init__(self, name: str, component: Component, volume: float, material: Material, production_cost: float, part_cost: float, reusable: bool):
        self.name = name
        self.component = component
        self.volume = volume
        self.material = material
        self.production_cost = production_cost
        self.part_cost = part_cost
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
            material_prices[m] = 2.493009304
        elif m == Material.Brass:
            material_prices[m] = 4.112723501
        elif m == Material.Carbon_Steel:
            material_prices[m] = 2.275
        elif m == Material.Cast_Iron:
            material_prices[m] = 0.1745926
        elif m == Material.Cobalt:
            material_prices[m] = 26.86775
        elif m == Material.Copper:
            material_prices[m] = 7.7849135
        if m == Material.Gold:
            material_prices[m] = 274604.7422
        elif m == Material.Magnesium:
            material_prices[m] = 2.752880922
        elif m == Material.Nickel:
            material_prices[m] = 21.056035
        elif m == Material.Silver:
            material_prices[m] = 775.8402098
        elif m == Material.Stainless:
            material_prices[m] = 4.0768
        elif m == Material.Steel:
            material_prices[m] = 1.6920995
        elif m == Material.Tin:
            material_prices[m] = 25.75391
        elif m == Material.Titanium:
            material_prices[m] = 6.1425
        elif m == Material.Zamak:
            material_prices[m] = 3.21996157
        elif m == Material.NA:
            material_prices[m] = 0

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
    elif part_component == "CastPart":
        return Component.CastPart

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
    elif part_material == "NA":
        return Material.NA

def get_name_parts():
    name_parts = ()
    for index in range(number_parts):
        part_name = (model_parts[index].name,)
        name_parts += part_name
    return name_parts

def total_cost_part(p: Part) -> float:
    # Calculate the cost of the part
    comp = p.get_component()
    price = 0
    if comp == Component.CastPart or comp == Component.Chiller or comp == Component.Overflow:
        price = round(float(p.volume * material_prices[p.material]), 4)

    elif comp == Component.Core or comp == Component.Sleeve or comp == Component.Filter:
        price = round(float(p.volume * material_prices[p.material] + p.production_cost), 4)
    elif comp == Component.Riser:
        return 0
    else:
        return -1
    if selectedCurrency == "EUR (€)": return price
    elif selectedCurrency == "USD ($)": return price*1.10
    elif selectedCurrency == "GBP (£)": return price*0.86

def get_component():
    if partName.value[:4] == "core": return "Core"
    elif partName.value[:7] == "chiller": return "Chiller"
    elif partName.value[:5] == "riser": return "Riser"
    elif partName.value[:6] == "sleeve": return "Sleeve"
    elif partName.value[:8] == "overflow": return "Overflow"
    elif partName.value[:6] == "filter": return "Filter"
    elif partName.value[:4] == "Part": return "CastPart"
    else: return "-1"

def get_component_aux(name):
    if name[:4] == "core": return "Core"
    elif name[:7] == "chiller": return "Chiller"
    elif name[:5] == "riser": return "Riser"
    elif name[:6] == "sleeve": return "Sleeve"
    elif name[:8] == "overflow": return "Overflow"
    elif name[:6] == "filter": return "Filter"
    elif name[:4] == "Part": return "CastPart"
    else: return "-1"



def estimated_cost_part(p: Part) -> float:
    # Calculate the estimated cost of the part
    return float(p.get_volume() * material_prices[p.get_material()] * 2)


def total_cost_model() -> float:
    # Calculate the total cost of the model
    total_cost = 0
    for i in range(number_parts):
        total_cost += parts_vector[i].part_cost

    return round(total_cost, 4)

# def update_prices(moneda):
#     url = f"https://commodities-api.com/api/latest?access_key=ad3lcz6of4m5b37ka20q0k5tulwdi0hanmc05wxb17mi28ygjf02ea2vpl3k&base={moneda}&symbols=ALU,LCO,XCU,XAU,NI,XAG,TIN"
#
#     try:
#         # Send GET request to the API
#         response = requests.get(url)
#
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             data = response.json()
#             # Process the response data
#             # ...
#             print("API request successful")
#         else:
#             print(f"Request failed with status code: {response.status_code}")
#     except requests.RequestException as e:
#         print("Error occurred during API request:", str(e))



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

def onSelected(event):
    partComponent.text = get_component()
    partVolume.text = get_volume()
    partMaterial.value = get_material()
    materialCost.text = get_material_cost()

partName = gui.ComboBox(
    parent = None,
    name = 'partName',
    values = get_name_parts(),
    command=onSelected,
)

partComponentLabel = gui.Label(
    parent = None,
    name = 'partComponentLabel',
    text = 'Component',
)

partComponent = gui.Label(
    parent = None,
    name = 'partComponent',
    text = get_component(),
)

partVolumeLabel = gui.Label(
    parent = None,
    name = 'partVolumeLabel',
    text = 'Mass',
)

def get_volume():
    volume = -1
    for part in model_parts:
        if part.name == partName.value:
            volume = part.volume
    return round(volume,4)


partVolume = gui.LineEdit(
    parent = None,
    name = 'partVolume',
    text = get_volume(),

)

partMaterialLabel = gui.Label(
    parent = None,
    name = 'partMaterialLabel',
    text = 'Material',
)

def get_material():
    material = "Aluminium"
    for part in model_parts:
        if part.name == partName.value:
            material = part.GetAttribute("c2_materialGroup")
    if material == "Cast-Iron": material = "Cast_Iron"
    elif material == "Carbon-Steel": material = "Carbon-Steel"
    if partName.value[:6] == "sleeve": material = "Steel"
    elif partName.value[:5] == "riser": material = "NA"
    return material

def get_material_aux(name):
    material = "Aluminium"
    for part in model_parts:
        if part.name == name:
            material = part.GetAttribute("c2_materialGroup")
    if material == "Cast-Iron": material = "Cast_Iron"
    elif material == "Carbon-Steel": material = "Carbon-Steel"
    if name[:6] == "sleeve": material = "Steel"
    elif name[:5] == "riser": material = "NA"
    return material

partMaterial = gui.ComboBox(
    parent = None,
    name = 'partMaterial',
    values = ('Aluminium', 'Brass', 'Carbon_Steel', 'Cast_Iron', 'Cobalt', 'Copper', 'Gold', 'Magnesium', 'Nickel', 'Silver', 'Stainless', 'Steel', 'Tin', 'Titanium', 'Zamak', 'NA', ),
    value = get_material(),
)

materialCostLabel = gui.Label(
    parent = None,
    name = 'materialCostLabel',
    text = 'Material cost (€/kg)',
)

def get_material_cost():
    update_material_prices()
    mat = get_material()
    mat1 = get_material_type(mat)
    return material_prices[mat1]



materialCost = gui.LineEdit(
    parent = None,
    name = 'material_Cost',
    text = get_material_cost(),
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


horizontalSpacer_4 = gui.SpacerItem(40, 20, spacing = 'Horizontal')

partCostLabel = gui.Label(
    parent = None,
    name = 'partCostLabel',
    text = 'Part cost',
    font = dict(size = 9, bold = True),
)

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

def onChangeCurrency(event):
    global selectedCurrency
    selectedCurrency = currency.value

currency = gui.ComboBox(
    parent = None,
    name = 'currency',
    values = ('EUR (€)', 'USD ($)', 'GBP (£)', ),
    value = selectedCurrency,
    command = onChangeCurrency,
)

totalCostLabel = gui.Label(
    parent = None,
    name = 'totalCostLabel',
    text = 'Total cost',
    font = dict(size = 10, bold = True),
)

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
    
    for index in range(number_parts):
        part_name = model_parts[index].name
        part_component = get_component_aux(part_name)
        component_type = get_component_type(part_component)
        part_volume = float(model_parts[index].mass)
        part_material = get_material_aux(part_name)
        material_type = get_material_type(part_material)
        material_cost = 0
        part_production_cost = float(productionCost.value)
        part_reusable = isReusable.value

        part_aux = Part(part_name, component_type, part_volume, material_type, part_production_cost, 0, part_reusable)
        part_cost = total_cost_part(part_aux)
        part =  Part(part_name, component_type, part_volume, material_type, part_production_cost, part_cost, part_reusable)
        parts_vector.append(part)
        parts_map[part_name] = (part)

def calculate_costs():
    init_data()
    part = parts_map[partName.value]
    totalPartCost = str(total_cost_part(part))
    partCost.text = str(totalPartCost + " " + selectedCurrency)
    totalCostModel = str(total_cost_model())
    totalCost.text = str(totalCostModel + " " + selectedCurrency)

def onClickCalculateCostsButton(event):
    calculate_costs()
  
calculateCostsButton = gui.PushButton(
    parent = None,
    name = 'calculateCostsButton',
    text = 'Calculate costs',
    command = onClickCalculateCostsButton,
)

def onClickResetValuesButton(event):
    init_data()
    partComponent.text = get_component()
    partVolume.text = get_volume()
    partMaterial.value = get_material()
    materialCost.text = get_material_cost()

resetValuesButton = gui.PushButton(
    parent = None,
    name = 'resetValuesButton',
    text = 'Reset values',
    command = onClickResetValuesButton,
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
        # resetValuesButton,
        # '<->',
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
        resetValuesButton,
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
		text="Quick Cost",
                children=[
                    gui.SpriteAction(
                        name="Calculate Costs",
                        icon="ribbonSleeveStrip-64.png",
                        context=ExtensionContext,
                    )
                ]
            )
        ],
    )

startup()
