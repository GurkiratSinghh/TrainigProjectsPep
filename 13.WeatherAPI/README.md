<p align="center">
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/Open--Meteo-4A90D9?style=for-the-badge&logoColor=white" />
</p>

# 🌤️ Rajasthan Weather & Air Quality Monitor

> A full-stack weather monitoring system for **6 Rajasthan cities** — fetches real-time weather & air quality data from **Open-Meteo APIs**, processes with **Polars**, generates intelligent alerts, and visualizes everything in a **Next.js** dashboard stored in **Supabase**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏙️ 6 Cities | Jaipur, Jodhpur, Udaipur, Bikaner, Ajmer, Kota |
| 🌡️ Weather Data | Temperature, humidity, wind, precipitation, UV index |
| 💨 Air Quality | PM2.5, PM10, dust, CO, NO₂, SO₂, ozone, AQI |
| ⚠️ Smart Alerts | Heatwave, dust storm, heavy rain, poor AQI, fog, UV warnings |
| 📊 Daily Aggregates | Min/max temps, total rainfall, avg AQI per day |
| 🌧️ Monsoon Tracking | Compares rainfall against historical normals |
| 📈 7-Day Forecast | Full week forecast with hourly breakdowns |
| 🖥️ Next.js Dashboard | Beautiful responsive frontend with real-time data |

---

## 🏗️ Project Structure

```
WeatherAPI/
├── backend/
│   ├── config.py            # Cities, API URLs, thresholds, weather codes
│   ├── preprocess.py        # Data pipeline: Fetch → Process → Alert → Store
│   ├── requirements.txt
│   ├── Dockerfile
│   └── render.yaml          # Deployment config
├── frontend/                # Next.js (TypeScript)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── next.config.ts
├── database/
│   └── schema.sql           # Supabase table definitions
└── .github/
    └── workflows/           # CI/CD automation
```

---

## 🚀 Quick Start

### Backend (Data Pipeline)

```bash
cd backend

# 1 · Install dependencies
pip install -r requirements.txt

# 2 · Configure environment
#     Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in .env

# 3 · Run the data pipeline
python preprocess.py
```

### Frontend

```bash
cd frontend

# 1 · Install dependencies
npm install

# 2 · Configure environment
#     Set NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY in .env.local

# 3 · Run the dev server
npm run dev
# → http://localhost:3000
```

---

## 🔧 Data Pipeline Flow

```
Open-Meteo Weather API ──┐
                         ├──▶ Polars Processing ──▶ Alert Engine ──▶ Supabase
Open-Meteo AQI API ──────┘        │                     │
                              Hourly Data           ⚠️ Heatwave
                              Daily Aggregates      ⚠️ Dust Storm
                              Forecast Data         ⚠️ Heavy Rain
                                                    ⚠️ Poor AQI
                                                    ⚠️ High UV
```

### Alert Thresholds (Rajasthan-Specific)

| Alert | Threshold |
|---|---|
| 🔥 Heatwave | ≥ 42°C |
| 🔥 Severe Heatwave | ≥ 45°C |
| ❄️ Cold Wave | ≤ 4°C |
| 🌪️ Dust Storm | Dust ≥ 150 µg/m³ + Wind ≥ 40 km/h |
| 🌧️ Heavy Rain | ≥ 50 mm/day |
| 😷 Poor AQI | US AQI ≥ 101 |
| ☀️ High UV | UV Index ≥ 8 |

---

## 🛠️ Tech Stack

- **Python + Polars** — high-performance data processing
- **Open-Meteo API** — free weather & air quality data
- **Supabase (PostgreSQL)** — managed database
- **Next.js + TypeScript** — server-side rendered frontend
- **httpx** — async HTTP client with retry logic
- **GitHub Actions** — scheduled pipeline runs

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
