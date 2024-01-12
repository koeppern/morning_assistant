# morning_helper
*Johannes Köppern*, *Nico Borchert*, 2024

## Folder structure
```
morning_assistant/
│
├── app.py
│
├── classes/
│   ├── __init__.py
│   └── personal_data_hub.py  # Definition von PersonalDataHub
│
├── methods/
│   ├── __init__.py
│   └── helper.py
│
├── tests/
│   ├── __init__.py
│   └── test_personal_data_hub.py
│
├── README.md
└── requirements.txt
```

## Linter: pylint
Installieren von Python und Pylint:

Stellen Sie sicher, dass Python auf Ihrem System installiert ist.
Installieren Sie Pylint in Ihrer Python-Umgebung. Sie können dies tun, indem Sie das folgende Kommando in Ihrem Terminal oder Kommandozeilen-Interface ausführen:
bash
Copy code
pip install pylint
Installieren der Python-Erweiterung in VSCode:

Öffnen Sie VSCode.
Gehen Sie zum Extensions-Tab (Symbolleiste auf der linken Seite, das wie ein Quadrat aus zusammengefügten Teilen aussieht).
Suchen Sie nach „Python“ und installieren Sie die Python-Erweiterung von Microsoft.
Konfigurieren des Linters:

Sobald die Python-Erweiterung installiert ist, erkennt VSCode normalerweise automatisch den installierten Linter (z.B. Pylint).
Falls der Linter nicht automatisch erkannt wird, öffnen Sie die Einstellungen (Datei -> Einstellungen -> Einstellungen oder Ctrl + , auf Windows bzw. Cmd + , auf Mac).
Suchen Sie nach „Python Linting“.
Stellen Sie sicher, dass das Linting aktiviert ist, und wählen Sie Pylint (oder einen anderen bevorzugten Linter) aus der Liste der Linter aus.
Anpassen der Linting-Einstellungen:

Sie können weitere Einstellungen wie Linting-Regeln und Verhaltensweisen anpassen, indem Sie die settings.json-Datei von VSCode bearbeiten.
Zum Beispiel können Sie spezifische Pylint-Flags oder -Optionen in den Einstellungen festlegen.
Verwendung des Linters:

Öffnen Sie eine Python-Datei in VSCode.
Der Linter wird im Hintergrund laufen und Probleme im „Probleme“-Tab (im unteren Bereich des Editors) anzeigen.
Sie können auch Probleme direkt im Code sehen, die durch Unterstreichungen oder andere visuelle Hinweise hervorgehoben werden.
Mit diesen Schritten sollten Sie in der Lage sein, einen Linter in VSCode für Ihre Python-Entwicklung zu konfigurieren und zu verwenden. Linters sind ein nützliches Werkzeug, um die Codequalität zu verbessern und häufige Fehler zu vermeiden.

