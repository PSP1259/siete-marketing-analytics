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

## 5. OSI Layer Mapping (always a pleasure)

| OSI Layer | Definition | Project Components |
|----------|------------|---------------------|
| Layer 7 – Application | User-facing software, APIs, data processing | WordPress, WooCommerce, GA4, GA4 Data API, Google Tag Manager, Python scripts (extract_ga4_events.py, merge_funnel_daily.py, funnel_analysis.py), Streamlit Dashboard |
| Layer 6 – Presentation | Data formatting, UI rendering, serialization | HTML/CSS/JS (Astra Theme), DataLayer JSON, GA4 API JSON responses, Streamlit UI rendering |
| Layer 5 – Session | Session control, identity context, state handling | GA4 session logic, Client ID cookies, Session ID cookies, Google Cloud Service Account authentication |
| Layer 4 – Transport | End-to-end reliable data transfer | HTTPS, TLS, TCP, Streamlit local server (port 8501) |
| Layer 3 – Network | Routing, addressing, DNS resolution | Hostpoint DNS (siete.ch), Internet routing, Google Cloud API endpoints |
| Layer 2 – Data Link | Local network frame-level transmission | Local WLAN/LAN, Ethernet frames on Hostpoint servers |
| Layer 1 – Physical | Physical signal transmission | Fiber/DSL infrastructure, local PC hardware, Hostpoint server hardware |

---

## 6. Execution

Project directory: `cd siete-marketing-analytics`

Activate the virtual environment: `.venv\Scripts\activate`

GA4 event export: `python 04_data-pipeline/extract_ga4_events.py`

Run QA checks: `python 06_qa-and-monitoring/event_coverage_check.py`

Start dashboard: `streamlit run 07_dashboard/app.py`





