# 04 – Data Pipeline (GA4 → Python)

Dieses Verzeichnis enthält das Skript, das Events aus GA4 über die GA4 Data API exportiert.

## Dateien

- `extract_ga4_events.py` – ruft die GA4 Data API auf und exportiert Events als CSV.
- `config_example.yaml` – Beispielkonfiguration (ohne echte IDs/Keys).
- `config.yaml` – lokale Konfiguration mit echter Property-ID und Key-Pfad (nicht ins Repo committen).
- `data/` – Output-Ordner für CSV-Exporte (im `.gitignore`).

In diesem Teil des Projekts baue ich eine kleine, aber saubere Datenpipeline auf Basis der **GA4 Data API**.

Ziel:

- ausgewählte GA4-Events (z. B. `view_item`, `add_to_cart`, `begin_checkout`, `purchase`) automatisiert abfragen
- die Daten lokal als CSV ablegen
- sie später für Funnel-Analysen und Dashboards verwenden

Später kommen hier noch:

- ein Notebook für Funnel-Analysen
- eventuell eine Erweiterung Richtung BigQuery oder Looker Studio

## Setup und Ausführung

Die Pipeline wird lokal ausgeführt und nutzt eine Python Umgebung mit Service Account.

### 1. Virtuelle Umgebung erstellen und Pakete installieren

```bash
python -m venv .venv
# Windows Aktivierung
.venv\Scripts\activate

pip install -r 04_data-pipeline/requirements.txt


