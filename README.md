# Project-Architecture


## 1. Core Tools and Languages

| Category | Component | Version / Details | Purpose |
|----------|-----------|--------------------|----------|
| Programming Language | Python | 3.12 | Main language for data pipeline and dashboard |
| IDE | Visual Studio Code | — | Development, debugging, documentation |
| Version Control | Git | CLI & GitHub Desktop | Code management, repository synchronization |
| Environment | Python Virtual Environment | .venv | Isolated dependency environment |
| Terminal | PowerShell | — | Execution of scripts and Git commands |

---

## 2. Python Libraries and Dependencies

| Group | Library | Purpose | Dependency for |
|--------|----------|----------|-----------------|
| Data Processing | pandas | Data manipulation, merging, CSV export | Merge script, QA script, dashboard |
| Configuration | PyYAML | Reading configuration files | GA4 export script |
| GA4 API Access | google-analytics-data | Querying GA4 Data API | Export script |
| Authentication | google-auth, google-auth-oauthlib | Service account authentication | GA4 API calls |
| Dashboard UI | streamlit | Building the interactive dashboard | Dashboard layer |
| Visualization | plotly | Generating interactive charts | Dashboard |

---

## 3. Web, Tracking, Cloud and Hosting

| Category | System / Service | Role | Dependency / Integration |
|-----------|------------------|--------|----------------------------|
| CMS | WordPress.org | Website and admin base | Hostpoint hosting |
| E-Commerce | WooCommerce | Store system and product catalog | Generates e-commerce events for GA4 |
| Tracking Integration | GTM4WP Plugin | DataLayer injection | WooCommerce |
| Tag Manager | Google Tag Manager (GTM) | Client-side tracking logic | Integrated via GTM4WP |
| Analytics Backend | Google Analytics 4 (GA4) | Stores all events | Source for Python data pipeline |
| API Backend | GA4 Data API | Programmatic access to event data | Python export script |
| Cloud IAM | Google Cloud (Service Account) | API authentication | Required for GA4 API |
| Hosting | Hostpoint | Domain and WordPress hosting | Runs siete.ch |

---

## 4. System Architecture and Processing Logic

| Component | Role in Dataflow | Depends on |
|-----------|-------------------|-------------|
| GA4 Event Export Script (`extract_ga4_events.py`) | Extracts event-level data from GA4 API | google-analytics-data, google-auth, PyYAML |
| QA Script (`event_coverage_check.py`) | Ensures presence and completeness of event CSVs | pandas |
| Master CSV Layer (`ga4_funnel_daily.csv`) | Clean, aggregated funnel data | Merge script |
| Funnel Analysis (`funnel_analysis.py`) | Computes KPI metrics | Raw CSV files |
| Streamlit Dashboard (`07_dashboard/app.py`) | Visualizes Data and time series | Master CSV layer, pandas, plotly |

---

## 7. OSI Layer Mapping (always a pleasure)

| OSI Layer | Definition | Projektkomponenten |
|----------|------------|--------------------|
| Layer 7 – Application | Benutzernahe Software, APIs, Datenverarbeitung | WordPress, WooCommerce, GA4, GA4 Data API, Google Tag Manager, Python Scripts (extract_ga4_events.py, merge_funnel_daily.py, funnel_analysis.py), Streamlit Dashboard |
| Layer 6 – Presentation | Datenformatierung und Darstellung | HTML/CSS/JS (Astra Theme), DataLayer JSON, GA4 API JSON Responses, Streamlit UI Rendering |
| Layer 5 – Session | Sitzungssteuerung und Identitätskontext | GA4 Session Logic, Client ID Cookies, Session ID Cookies, Google Cloud Service Account Authentication |
| Layer 4 – Transport | Zuverlässige Ende-zu-Ende Datenübertragung | HTTPS, TLS, TCP, Streamlit Local Server (Port 8501) |
| Layer 3 – Network | Routing, IP-Adressen, DNS | DNS bei Hostpoint (siete.ch), Internet Routing, Google Cloud Endpoints |
| Layer 2 – Data Link | Lokale Übertragung innerhalb eines Netzwerks | WLAN/LAN Verbindung des lokalen Systems, Ethernet Frames bei Hostpoint Servern |
| Layer 1 – Physical | Physikalische Signalübertragung | Glasfaser/DSL, lokale PC-Hardware, Hostpoint Serverhardware |

---

## 8. Execution

Project directory: `cd siete-marketing-analytics`

Activate the virtual environment: `.venv\Scripts\activate`

GA4 event export: `python 04_data-pipeline/extract_ga4_events.py`

Run QA checks: `python 06_qa-and-monitoring/event_coverage_check.py`

Start dashboard: `streamlit run 07_dashboard/app.py`





