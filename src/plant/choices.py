from enum import Enum


class PlantType(Enum):
    flower = "Flower"
    shrub = "Shrub"
    tree = "Tree"


class PlantClass(Enum):
    common = "Common"
    rare = "Rare"
    epic = "Epic"
