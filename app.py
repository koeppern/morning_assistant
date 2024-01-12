"""
app.py
2024-01-10, JK
Purpose: Generate dailiy briefing and provide it in the way specified in the foloowing.
Start with dummy data from HardcodedPersonalDataHub clas.
"""
from classes.personal_data_hub import HardcodedPersonalDataHub as DataHub
from classes.data_extractor import DataExtractor


# -------------------------------------------------------
## Parameters
# -------------------------------------------------------
control_parameters = {
    "print_data_hub": True,
}

# -------------------------------------------------------
## Functions
# -------------------------------------------------------

# -------------------------------------------------------
## App
# -------------------------------------------------------
# Object data_hub, update data ------------------------------------------------------------------
data_hub = DataHub()

data_hub.update_data()

if control_parameters["print_data_hub"]:
    data_hub.print_data()

# Extract summary ------------------------------------------------------------------
extractor = DataExtractor(data_hub)
