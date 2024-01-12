# personal_data_hub.py
# 2024-01-10, JK
# The class PersonalDataHub is a singleton class that is used to store and retrieve personal data.
# Data are the user's name, private calendar, work calendar and so on.


# PersonalDataHub ------------------------------------------------------------------
# @Nico, bitte lösche diesen Kommentar, wenn du ihn gelesen hast.
# Ich wollte das Arbeiten mit einer Baxsisklasse in Python ausprobieren, auch wenn ich, Deinem Rat folgend, nicht mit der Archtiektur in voller Schönheit imersten Schritt beginnen will.
# Bei den anderen Klassen werde ich anders verfahren.
class PersonalDataHub:
    def __init__(
        self,
        user_name: str,
        personal_calendar_today: str,
        professional_calendar_today: str,
        notes_previous_days: str,
        date_for_summary: str,
    ):
        self.user_name = user_name
        self.personal_calendar_today = personal_calendar_today
        self.professional_calendar_today = professional_calendar_today
        self.notes_previous_days = notes_previous_days
        self.date_for_summary = date_for_summary


# HardcodedPersonalDataHub ------------------------------------------------------------------
class HardcodedPersonalDataHub(PersonalDataHub):
    def __init__(self):
        user_name = "Max"
        personal_calendar_today = "Persönlicher Kalender Einträge"
        professional_calendar_today = "Beruflicher Kalender Einträge"
        notes_previous_days = "Notizen der vergangenen Tage"
        date_for_summary = "2024-01-10"

        super().__init__(
            user_name,
            personal_calendar_today,
            professional_calendar_today,
            notes_previous_days,
        )
