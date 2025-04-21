import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Ultimate Unit Converter", page_icon="🔁", layout="centered")

# --- Title and Theme ---
st.markdown("<h1 style='text-align: center;'>🔁 Ultimate Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("#### 🌟 Convert between common units easily with a clean interface!")

# --- Theme Toggle ---
dark_mode = st.toggle("🌙 Dark Mode", value=False)
if dark_mode:
    st.markdown(
        """<style>
            body { background-color: #111; color: white; }
            .stSelectbox, .stNumberInput { background-color: #222 !important; }
        </style>""",
        unsafe_allow_html=True
    )

# --- Conversion Data ---
units_data = {
    "Length": {
        "Kilometer": 1000,
        "Meter": 1,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 1e-6,
        "Nanometer": 1e-9,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852,
    },
    "Mass": {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Ton": 1000,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K",
    },
    "Time": {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
    }
}

# --- Conversion History ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- UI Layout ---
category = st.selectbox("📁 Select Category", list(units_data.keys()))
value = st.number_input("🔢 Enter Value", value=1.0, step=0.1)

unit_from = st.selectbox("🔽 From Unit", list(units_data[category].keys()))
unit_to = st.selectbox("🔼 To Unit", list(units_data[category].keys()))

# --- Converter Logic ---
def convert_units(val, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == to_unit:
            return val
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (val * 9/5) + 32
            elif to_unit == "Kelvin":
                return val + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (val - 32) * 5/9
            elif to_unit == "Kelvin":
                return (val - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return val - 273.15
            elif to_unit == "Fahrenheit":
                return (val - 273.15) * 9/5 + 32
    else:
        base_val = val * units_data[category][from_unit]
        converted = base_val / units_data[category][to_unit]
        return converted

# --- Button ---
if st.button("🔁 Convert"):
    result = convert_units(value, unit_from, unit_to, category)
    st.success(f"✅ {value} {unit_from} = {result:.6f} {unit_to}")

    # Save to history
    st.session_state.history.append(
        f"{value} {unit_from} ➡️ {result:.6f} {unit_to} ({category})"
    )

# --- History ---
if st.session_state.history:
    st.markdown("### 🕘 Conversion History")
    for item in st.session_state.history[::-1]:
        st.markdown(f"- {item}")
