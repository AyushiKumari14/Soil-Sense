import streamlit as st
import serial
import time
import random
from datetime import datetime

from weather import get_weather, API_KEY

COM_PORT = "COM5"
BAUD_RATE = 9600
st.set_page_config(
    page_title="Smart Agriculture Dashboard",
    page_icon="🌱",
    layout="wide"
)

st.markdown(
    """
    <style>

    /* Main dashboard */
    .stApp {
        font-size: 29px !important;
    }

    p, li, label, div {
        font-size: 27px !important;
    }

    /* Main headings */
    h1 {
        font-size: 58px !important;
    }

    h2 {
        font-size: 45px !important;
    }

    h3 {
        font-size: 36px !important;
    }

    /* Metric labels */
    [data-testid="stMetricLabel"] {
        font-size: 25px !important;
    }

    /* Metric values */
    [data-testid="stMetricValue"] {
        font-size: 48px !important;
    }

# SIDEBAR
     
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] div {
        font-size: 29px !important;
    }

    /* Sidebar headings */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        font-size: 34px !important;
    }

    /* Sidebar buttons */
    section[data-testid="stSidebar"] button {
        font-size: 27px !important;
    }

    /* Sidebar input text */
    section[data-testid="stSidebar"] input {
        font-size: 27px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

if "arduino" not in st.session_state:
    st.session_state.arduino = None

if "history" not in st.session_state:
    st.session_state.history = []

if "last_moisture" not in st.session_state:
    st.session_state.last_moisture = None

if "last_ph" not in st.session_state:
    st.session_state.last_ph = None

if "last_weather" not in st.session_state:
    st.session_state.last_weather = None

if "weather_city" not in st.session_state:
    st.session_state.weather_city = ""


st.sidebar.header("⚙️ Project Settings")

mode = st.sidebar.radio(
    "Data Mode",
    [
        "Arduino Live Data",
        "Demo Random Data"
    ]
)

st.sidebar.subheader("📍 Location")

city = st.sidebar.text_input(
    "Enter your city",
    value="Kolar"
)

country = st.sidebar.text_input(
    "Country Code",
    value="IN"
)

get_weather_button = st.sidebar.button(
    "🌤️ Get Weather"
)

def connect_arduino():
    try:
        arduino = serial.Serial(COM_PORT, BAUD_RATE, timeout=2)
        time.sleep(2)
        return arduino
    except Exception:
        return None


def read_arduino(arduino):
    try:
        arduino.reset_input_buffer()
        value = arduino.readline().decode("utf-8", errors="ignore").strip()
        if value:
            parts = value.split(",")
            if len(parts) == 2:
                moisture_value = int(parts[0])
                ph_value = float(parts[1])
                return moisture_value, ph_value
    except Exception:
        return None, None
    return None, None
    
# GET WEATHER (delegated to weather.py)
# GET WEATHER
weather = None
forecast = None
weather_error = None

if (
    get_weather_button
    or st.session_state.weather_city != f"{city},{country}"
):

    weather, forecast, weather_error = get_weather(city)

    st.session_state.weather_city = f"{city},{country}"

    if weather_error:
        st.session_state.last_weather = None
    else:
        st.session_state.last_weather = weather

else:

    weather = st.session_state.last_weather


# WEATHER VALUES
temperature = None
humidity = None
weather_description = "Unknown"

if weather and not weather_error:

    try:

        temperature = weather["main"]["temp"]

        humidity = weather["main"]["humidity"]

        weather_description = (
            weather["weather"][0]["description"]
        )

    except (KeyError, TypeError, IndexError):

        temperature = None
        humidity = None
        weather_description = "Unknown"

# MOISTURE DATA

moisture = None
ph = None

if mode == "Arduino Live Data":
    if st.session_state.arduino is None:
        st.session_state.arduino = connect_arduino()

    if st.session_state.arduino is not None:
        moisture, ph = read_arduino(st.session_state.arduino)
        if moisture is not None and ph is not None:
            st.session_state.last_moisture = moisture
            st.session_state.last_ph = ph
    else:
        moisture = st.session_state.last_moisture
        ph = st.session_state.last_ph

elif mode == "Demo Random Data":
    moisture = random.randint(250, 950)
    ph = round(random.uniform(5.0, 8.0), 2)


# SOIL ANALYSIS


soil_status = "Unknown"
moisture_percent = 0

if moisture is not None:
    DRY_VALUE = 1023
    WET_VALUE = 300

    moisture_percent = ((DRY_VALUE - moisture) / (DRY_VALUE - WET_VALUE)) * 100
    moisture_percent = max(0, min(100, moisture_percent))

    if moisture > 750:
        soil_status = "VERY DRY"
    elif moisture > 600:
        soil_status = "DRY"
    elif moisture > 400:
        soil_status = "MODERATE"
    else:
        soil_status = "WET"
# PH STATUS
def get_ph_status(ph_value):
    if ph_value is None:
        return "Unknown"
    elif ph_value < 7.0:
        return "ACIDIC"
    elif ph_value > 7.0:
        return "BASIC"
    else:
        return "NEUTRAL"

if moisture is not None:
    now = datetime.now().strftime("%H:%M:%S")

    new_reading = {
        "Time": now,
        "Moisture": moisture,
        "Moisture %": round(moisture_percent, 1),
        "pH": round(ph, 2) if ph is not None else None
    }

    if (
        not st.session_state.history
        or st.session_state.history[-1]["Moisture"] != moisture
        or mode == "Demo Random Data"
    ):
        st.session_state.history.append(new_reading)

if len(st.session_state.history) > 30:
    st.session_state.history = st.session_state.history[-30:]

# LOCATION DISPLAY
st.subheader("📍 Selected Location")
st.write(f"**{city}, {country}**")



# LIVE MONITORING

st.subheader("📊 Live Monitoring")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🌱 Soil Moisture", moisture if moisture is not None else "Waiting...")

with col2:
    st.metric("💧 Soil Status", soil_status)

with col3:
    st.metric("🌡️ Temperature", f"{temperature:.1f} °C" if temperature is not None else "N/A")

with col4:
    st.metric("💨 Humidity", f"{humidity}%" if humidity is not None else "N/A")

with col5:
    st.metric("🧪 Soil pH", f"{ph:.2f}" if ph is not None else "N/A")
    if ph is not None:
        st.caption(f"{get_ph_status(ph)}")
        
# SOIL MOISTURE LEVEL


st.subheader("🌱 Soil Moisture Level")

if moisture is not None:
    st.progress(int(moisture_percent))
    st.write(f"Current moisture: **{moisture_percent:.1f}%**")
else:
    st.warning("No moisture reading available.")



st.subheader("📈 Moisture History")

if st.session_state.history:
    chart_data = {
        item["Time"]: item["Moisture %"]
        for item in st.session_state.history
    }
    st.line_chart(chart_data)
    st.write(f"Number of readings: **{len(st.session_state.history)}**")
else:
    st.info("No readings collected yet.")



st.subheader("🌤️ Weather Information")

if weather_error:

    st.warning(weather_error)

elif weather:

    st.success("Weather API Connected ✅")

    st.write(
        f"**Condition:** "
        f"{weather_description.title()}"
    )

    st.write(
        f"🌡️ Temperature: **{temperature:.1f} °C**"
    )

    st.write(
        f"💨 Humidity: **{humidity}%**"
    )

else:

    st.info(
        "Enter your city and click 'Get Weather'."
    )


st.subheader("🤖 Agriculture Analysis")

if moisture is None:
    st.info("Waiting for soil moisture data.")
else:
    if soil_status == "VERY DRY":
        st.error("🚨 Soil is very dry. Irrigation is strongly recommended.")
    elif soil_status == "DRY":
        st.warning("💧 Soil is dry. Irrigation may be required.")
    elif soil_status == "MODERATE":
        st.success("🌱 Soil moisture is in a moderate range. Continue monitoring.")
    elif soil_status == "WET":
        st.info("💦 Soil is wet. Avoid unnecessary irrigation.")


# CROP RECOMMENDATION
st.subheader("🌾 Crop / Plant Recommendations")

recommendations = []

if moisture is not None:

    if moisture > 750:
        recommendations.extend([
            {"crop": "🌵 Cactus / Succulent", "category": "Drought-tolerant",
             "reason": "Can tolerate relatively dry conditions."},
            {"crop": "🌿 Millet", "category": "Cereal",
             "reason": "Relatively suitable for lower-water conditions."},
            {"crop": "🌾 Sorghum", "category": "Cereal",
             "reason": "Generally more drought tolerant than many crops."}
        ])

    elif 600 < moisture <= 750:
        recommendations.extend([
            {"crop": "🌽 Maize", "category": "Cereal",
             "reason": "Can grow well when adequate water is provided."},
            {"crop": "🌻 Sunflower", "category": "Oilseed",
             "reason": "Suitable for moderately dry soil conditions."},
            {"crop": "🥜 Groundnut", "category": "Legume",
             "reason": "Can perform well in well-drained soil."}
        ])

    elif 400 < moisture <= 600:
        recommendations.extend([
            {"crop": "🍅 Tomato", "category": "Vegetable",
             "reason": "Suitable when soil moisture is maintained consistently."},
            {"crop": "🌶️ Chilli", "category": "Vegetable",
             "reason": "Can grow well with controlled irrigation."},
            {"crop": "🥔 Potato", "category": "Tuber",
             "reason": "Needs consistent moisture and good drainage."},
            {"crop": "🍓 Strawberry", "category": "Fruit",
             "reason": "Prefers consistent moisture and suitable temperatures."}
        ])

    elif moisture <= 400:
        recommendations.extend([
            {"crop": "🍚 Rice", "category": "Cereal",
             "reason": "Can tolerate much wetter growing conditions than many crops."},
            {"crop": "🌿 Water-tolerant plants", "category": "Other",
             "reason": "Consider plants suited to wet conditions."}
        ])



filtered_recommendations = []

for crop in recommendations:
    suitable = True
    crop_name = crop["crop"]

    if temperature is not None:
        if ("Tomato" in crop_name or "Chilli" in crop_name) and not (18 <= temperature <= 32):
            suitable = False
        if "Potato" in crop_name and not (15 <= temperature <= 27):
            suitable = False
        if "Strawberry" in crop_name and not (10 <= temperature <= 26):
            suitable = False
        if "Rice" in crop_name and not (20 <= temperature <= 35):
            suitable = False
        if "Maize" in crop_name and not (18 <= temperature <= 35):
            suitable = False

    if suitable:
        filtered_recommendations.append(crop)


# DISPLAY RECOMMENDATIONS

if filtered_recommendations:
    for crop in filtered_recommendations:
        st.success(
            f"**{crop['crop']}** ({crop['category']})\n\n"
            f"{crop['reason']}"
        )
else:
    st.info(
        "No strong crop match was found for the current conditions."
    )


st.subheader("🌱 Plant Growing Recommendation")

if moisture is not None:
    if moisture > 750:
        st.warning("💧 Increase irrigation carefully. The soil is currently dry.")
    elif 600 < moisture <= 750:
        st.info("🌱 Monitor moisture regularly. Moderate irrigation may be required.")
    elif 400 < moisture <= 600:
        st.success("✅ Soil moisture is suitable for many common crops. Maintain consistent watering.")
    elif moisture <= 400:
        st.warning("💦 Soil is very wet. Avoid additional irrigation and check drainage.")

if temperature is not None:
    if temperature > 35:
        st.warning("🌡️ High temperature detected. Provide adequate water and protect sensitive plants.")
    elif temperature < 15:
        st.info("❄️ Temperature is low. Choose crops suitable for cooler conditions.")


# SYSTEM STATUS
st.subheader("🔌 System Status")

if mode == "Demo Random Data":
    st.info("🎲 Demo Mode — Random moisture data")
else:
    if st.session_state.arduino is not None:
        st.success(f"Arduino Connected — {COM_PORT} ✅")
    else:
        st.error(f"Arduino Not Connected — {COM_PORT} ❌")

if weather and "error" not in weather:
    st.success("Weather API Connected ✅")
else:
    st.warning("Weather API Not Connected")




st.divider()

st.caption(
    "Crop recommendations are simplified educational "
    "rules for this project and should not replace "
    "professional agricultural advice."
)
