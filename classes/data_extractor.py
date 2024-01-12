"""
data_extractor.py
2024-01-12, JK
Thie DataExtractor class creates summaries using GPT-4 based on the
user's personal data probided in the PersonalDataHub data_hub object.
"""


class DataExtractor:
    def __init__(self, data_hub):
        self.data_hub = data_hub
