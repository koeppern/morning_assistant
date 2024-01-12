# personal_data_hub.py
# 2024-01-10, JK
# The class PersonalDataHub is a singleton class that is used to store and retrieve personal data.
# Data are the user's name, private calendar, work calendar and so on.


# PersonalDataHub ------------------------------------------------------------------
# @Nico, bitte lösche diesen Kommentar, wenn du ihn gelesen hast.
# Ich wollte das Arbeiten mit einer Baxsisklasse in Python ausprobieren, auch wenn ich, Deinem Rat folgend, nicht mit der Archtiektur in voller Schönheit imersten Schritt beginnen will.
# Bei den anderen Klassen werde ich anders verfahren.
class PersonalDataHub:
    def __init__(self):
        self.user_name = None
        self.personal_calendar_today = None
        self.professional_calendar_today = None
        self.notes_previous_days = None
        self.date_for_summary = None

    def update_data(self):
        return False

    def print_data(self):
        print("user_name: ", self.user_name)
        print("personal_calendar_today: ", self.personal_calendar_today)
        print("professional_calendar_today: ", self.professional_calendar_today)
        print("notes_previous_days: ", self.notes_previous_days)
        print("date_for_summary: ", self.date_for_summary)


# HardcodedPersonalDataHub ------------------------------------------------------------------
class HardcodedPersonalDataHub(PersonalDataHub):
    def update_data(self):
        self.user_name = "Max"
        self.personal_calendar_today = "Persönlicher Kalender Einträge"
        self.professional_calendar_today = "Beruflicher Kalender Einträge"
        self.notes_previous_days = "Notizen der vergangenen Tage"
        self.date_for_summary = "2024-01-10"
