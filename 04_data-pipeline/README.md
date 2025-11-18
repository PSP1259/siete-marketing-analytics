# 04 – Data Pipeline (GA4 → Python)

In diesem Teil des Projekts baue ich eine kleine, aber saubere Datenpipeline auf Basis der **GA4 Data API**.

Ziel:

- ausgewählte GA4-Events (z. B. `view_item`, `add_to_cart`, `begin_checkout`, `purchase`) automatisiert abfragen
- die Daten lokal als CSV ablegen
- sie später für Funnel-Analysen und Dashboards verwenden

Wichtig:

- Die Pipeline arbeitet nur mit **aggregierten Eventdaten**, keine personenbezogenen Informationen.
- Service-Account-Key und echte Konfiguration bleiben **lokal** und landen nicht in diesem Repository.

Geplante Bausteine:

1. `requirements.txt`  
   – Python-Abhängigkeiten (GA4 API Client, pandas, YAML)

2. `config_example.yaml`  
   – Template für die lokale Konfiguration (Property-ID, Zeiträume, Eventliste, Output-Ordner)

3. `extract_ga4_events.py`  
   – Skript, das:
     - Config lädt
     - GA4 Data API abfragt
     - die Resultate als CSV speichert

Später kommen hier noch:

- ein Notebook für Funnel-Analysen
- eventuell eine Erweiterung Richtung BigQuery oder Looker Studio

