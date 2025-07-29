from enum import Enum

# Define an Enum for dropdown options
class SourceOptions(Enum):
    satellite = "SATELLITE"
    terrestrial = "TERRESTRIAL"
    cable = "CABLE"

class SourceMappings:
    SOURCE_MAPPING = {
        SourceOptions.satellite: ["TYPE_DVB_S", "TYPE_DVB_S2"],
        SourceOptions.terrestrial: ["TYPE_DVB_T2"],
        SourceOptions.cable: ["TYPE_DVB_C"]
    }