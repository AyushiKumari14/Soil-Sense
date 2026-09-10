# Soil-Sense
# 🌱 SoilSense — AI-Based Soil Detection, Crop Recommendation & Smart Growing Guide

**SoilSense** is a smart agriculture project that combines **Arduino-based soil monitoring, Python, data analysis, weather information, and crop recommendation** to help users understand soil conditions and choose suitable crops or plants.

The system collects soil parameters such as **soil moisture and soil pH**, processes the collected information, and presents the results through an interactive **Python Streamlit dashboard**. Based on soil conditions and weather information, SoilSense provides suitable crop recommendations and a smart growing guide.

---

## 🎯 Project Objective

The main objective of SoilSense is to develop a **low-cost and intelligent soil monitoring system** that can assist users in making better crop-growing decisions.

The project aims to:

* 💧 Monitor soil moisture
* 🧪 Measure and analyze soil pH
* 🔌 Collect sensor data using Arduino
* 🐍 Process sensor data using Python
* 🌦️ Integrate weather information
* 🌾 Recommend suitable crops/plants
* 📊 Display soil analysis through a dashboard
* 📖 Provide a smart growing guide
* 💡 Help users understand basic soil conditions
* 💰 Provide an affordable prototype for smart agriculture

---

# 🔄 System Workflow

```text
                🌱 SOIL
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
   💧 Moisture Sensor    🧪 pH Sensor
          │                 │
          └────────┬────────┘
                   ▼
              🔌 ARDUINO
                   │
                   ▼
            Sensor Readings
                   │
                   ▼
              🐍 PYTHON
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
   Soil Analysis      🌦️ Weather Data
          │                 │
          └────────┬────────┘
                   ▼
          🌾 Crop Recommendation
                   │
                   ▼
          📖 Growing Guide
                   │
                   ▼
          💻 STREAMLIT DASHBOARD
```

---

# 🛠️ Technologies Used

## 💻 Software

* **Python**
* **C/C++**
* **Streamlit**
* **Pandas**
* **Requests**
* **Arduino IDE**

## 🔌 Hardware

* Arduino board
* 💧 Soil Moisture Sensor
* 🧪 Soil pH Sensor / PAT Sensor
* Breadboard
* Jumper wires
* USB cable

## 🌦️ API

* **Open-Meteo Weather API**
* Open-Meteo Geocoding API

---

# ✨ Main Features

## 1. 💧 Soil Moisture Monitoring

The soil moisture sensor measures the amount of moisture present in the soil.

The sensor provides an electrical reading that is processed by the Arduino.

```text
Soil
 ↓
Moisture Sensor
 ↓
Arduino
 ↓
Moisture Reading
 ↓
Python
 ↓
Dashboard
```

The moisture value can be used to classify the soil condition, for example:

* Dry
* Moderately Moist
* Wet

---

## 2. 🧪 Soil pH Measurement

Soil pH is an important parameter for determining plant suitability.

The pH scale ranges from **0 to 14**.

```text
0              7              14
│──────────────│──────────────│
Acidic       Neutral       Alkaline
```

SoilSense uses the pH sensor to obtain soil pH information and use it as part of the crop recommendation process.

Different plants require different soil pH ranges. Therefore, pH information can help identify plants that are more suitable for the tested soil.

---

## 3. 🌦️ Weather Information

SoilSense integrates weather information using the **Open-Meteo API**.

The user can enter a location, after which the system can obtain relevant weather information.

Weather conditions can influence:

* Plant growth
* Water requirements
* Suitable crops
* Growing conditions
* Irrigation decisions

Combining soil information with weather information makes the recommendation system more useful.

---

# 🌾 Crop Recommendation

SoilSense analyzes available soil parameters and matches them with plant requirements.

The basic concept is:

```text
       Soil Data
           │
           ▼
   ┌───────────────┐
   │ Soil Analysis │
   └───────┬───────┘
           │
      ┌────┴────┐
      ▼         ▼
  Moisture      pH
      │         │
      └────┬────┘
           ▼
   Plant Requirement
        Matching
           │
           ▼
    🌾 Crop Recommendation
```

The recommendation can consider:

* Soil moisture
* Soil pH
* Weather conditions
* Plant requirements

---

# 📖 Smart Growing Guide

After recommending a crop or plant, SoilSense can provide useful growing information.

The guide can include:

| Parameter          | Information                |
| ------------------ | -------------------------- |
| 🌱 Plant           | Recommended crop/plant     |
| 🧪 Soil pH         | Suitable pH range          |
| 💧 Water           | Water requirement          |
| ☀️ Sunlight        | Required sunlight          |
| 🌡️ Temperature    | Suitable temperature       |
| 🌾 Soil            | Suitable soil type         |
| 🗓️ Growing Period | Approximate growth period  |
| 💡 Care            | Basic growing instructions |

This allows the project to go beyond simply detecting soil conditions and provides practical information for growing the recommended plant.

---

# 💻 Streamlit Dashboard

The project uses **Streamlit** to create an interactive web dashboard.

The dashboard can display:

```text
╔══════════════════════════════════════════╗
║              🌱 SOIL SENSE               ║
║    Smart Soil Monitoring & Analysis      ║
╠══════════════════════════════════════════╣
║                                          ║
║  💧 Moisture          🧪 Soil pH          ║
║                                          ║
║  🌦️ Weather           📍 Location         ║
║                                          ║
║  📊 Soil Analysis                        ║
║                                          ║
║  🌾 Recommended Crops                     ║
║                                          ║
║  📖 Smart Growing Guide                   ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

# 🔌 Hardware Connection

### 💧 Soil Moisture Sensor

A typical analog moisture sensor connection:

```text
Moisture Sensor       Arduino
──────────────────────────────
VCC       ───────────► 5V
GND       ───────────► GND
AO        ───────────► A0
```

### 🧪 pH Sensor

The exact pH sensor wiring depends on the **specific sensor/module being used**.

Typical modules provide:

```text
VCC
GND
Analog Output
```

The analog output can be connected to an Arduino analog input.

> **Note:** Always check the pin labels and operating voltage of the specific pH/PAT sensor before connecting it.

---

# 📂 Project Structure

```text
SoilSense/
│
├── Arduino/
│   ├── soil_moisture.ino
│   └── soil_ph.ino
│
├── Python/
│   ├── app.py
│   ├── weather.py
│   └── recommendation.py
│
├── data/
│   └── soil_data.csv
│
├── images/
│   └── dashboard.png
│
├── requirements.txt
│
└── README.md
```

For a simple prototype, the project can also be maintained with fewer files:

```text
SoilSense/
│
├── soil_sense.ino
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SoilSense.git
```

Then:

```bash
cd SoilSense
```

---

## 2. Install Python Libraries

```bash
pip install streamlit pandas requests
```

Or use:

```bash
pip install -r requirements.txt
```

---

## 3. Connect the Sensors

Connect the:

* Soil moisture sensor
* pH/PAT sensor
* Arduino

according to the sensor pin configuration.

---

## 4. Upload Arduino Code

Open the Arduino `.ino` file in **Arduino IDE**.

Select:

```text
Tools → Board
Tools → Port
```

Then upload the program to the Arduino.

---

## 5. Run the Python Dashboard

```bash
streamlit run app.py
```

The SoilSense dashboard will then open in the browser.

---

# 📊 Data Processing

The system follows this basic data-processing pipeline:

```text
Sensor Data
     ↓
Arduino
     ↓
Serial Communication
     ↓
Python
     ↓
Data Processing
     ↓
Soil Analysis
     ↓
Weather Integration
     ↓
Crop Recommendation
     ↓
Growing Guide
```

---

# 🧠 Recommendation Logic

The initial recommendation system can use rule-based logic.

For example:

```text
IF soil moisture is suitable
AND soil pH matches crop requirement
AND weather conditions are suitable
        ↓
Recommend Crop
```

This approach makes the prototype easy to understand and test.

In the future, the rule-based system can be replaced or enhanced with a **Machine Learning model** trained on a larger soil and crop dataset.

---

# 🚀 Future Scope

SoilSense can be further developed with:

* 🤖 Machine Learning-based crop prediction
* 📱 Mobile application
* ☁️ Cloud-based soil-data storage
* 📈 Historical soil monitoring
* 🌡️ Temperature sensor
* 💧 Automatic irrigation
* 🌧️ Rainfall prediction
* ☀️ Light intensity monitoring
* 🚨 Irrigation alerts
* 🗺️ Location-based crop recommendations
* 📊 Advanced soil analytics
* 🔄 Real-time sensor monitoring
* 🌱 More crop and plant datasets

---

# 💡 Project Highlights

### Hardware + Software Integration

SoilSense demonstrates the integration of:

```text
Arduino
   +
Sensors
   +
C/C++
   +
Python
   +
Data Analysis
   +
Weather API
   +
Streamlit
   +
Agriculture
```

This makes the project relevant to **IoT, Data Science, Python, and Smart Agriculture**.

---

# 🎓 Project Domain

**Project Name:** SoilSense

**Domain:** Smart Agriculture / IoT / Data Science

**Project Type:** Hardware + Software

**Programming Languages:**

* Python
* C/C++

**Hardware Platform:** Arduino

**Interface:** Streamlit Web Dashboard

---

# 🌱 Project Vision

> **"From Soil Data to Smarter Growing Decisions."**

SoilSense aims to make basic soil monitoring and crop selection more accessible by combining affordable sensors with software-based analysis, weather information, and intelligent recommendations.

---

# 🤝 Contribution

Contributions and suggestions are welcome.

To contribute:

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Create a pull request.

---

# 📜 Disclaimer

SoilSense is an **educational and prototype project**. Sensor readings and recommendations may vary depending on sensor calibration, soil conditions, environmental conditions, and available data. The system is not intended to replace professional laboratory soil testing or expert agricultural advice.

---

## ⭐ Made for Learning & Innovation

**SoilSense — Smart Soil Monitoring for Smarter Agriculture 🌱**
