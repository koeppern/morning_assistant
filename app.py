"""
app.py
2024-01-10, JK
Purpose: Generate dailiy briefing and provide it in the way specified in the foloowing.
Start with dummy data from HardcodedPersonalDataHub clas.
"""
from classes.personal_data_hub import HardcodedPersonalDataHub as DataHub
from classes.data_extractor import DataExtractor
from dotenv import load_dotenv, find_dotenv
import os
import yaml


# -------------------------------------------------------
## Parameters
# -------------------------------------------------------
control_parameters = {
    "print_data_hub": True,
}


# -------------------------------------------------------
## Functions
# -------------------------------------------------------
def load_yaml_file(path):
    with open(path, "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)


def propare_environment():
    load_dotenv(find_dotenv(".env_morning_assistant"))

    BASE_DIR = os.getenv("BASE_DIR")

    RESOURCES_FILE_NAME = os.getenv("RESOURCES_FILE_NAME")

    os.chdir(BASE_DIR)

    resources_file_name = os.path.join(BASE_DIR, RESOURCES_FILE_NAME)

    resources = load_yaml_file(resources_file_name)

    return resources


# -------------------------------------------------------
## App
# -------------------------------------------------------
# Load environmaent and configuration variables ------------------------------------------------------------------
resources = propare_environment()

# load yml file config_file_path


# Object data_hub, update data ------------------------------------------------------------------
data_hub = DataHub()

data_hub.update_data()

if control_parameters["print_data_hub"]:
    data_hub.print_data()

# Create summary ------------------------------------------------------------------
extractor = DataExtractor(data_hub)
