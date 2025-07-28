from enum import Enum

# Define an Enum for dropdown options
class SourceOptions(Enum):
    satellite = "SATELLITE"
    terrestrial = "TERRESTRIAL"
    cable = "CABLE"