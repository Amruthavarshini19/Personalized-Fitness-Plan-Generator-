import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Fitness Profile Generator", layout="wide")

# 2. Custom Styling (Maintaining your specific color/layout requirements)
st.markdown("""
    <style>
    /* Gradient Background for the entire App */
    .stApp {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        background-attachment: fixed;
    }

    /* Sidebar Background - Black */
    section[data-testid="stSidebar"] {
        background-color: #000000 !important;
    }
    
    /* Sidebar Text Color - White */
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] p {
        color: #FFFFFF !important;
    }

    /* Main Content Text Colors - Professional Dark Grey */
    h1, h2, h3, p, label {
        color: #2D3436 !important;
        font-weight: 600;
    }

    /* Input Elements Styling */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 8px !important;
    }

    /* BUTTON STYLING - White text on dark teal as requested */
    .stButton > button {
        background-color: #004d57 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        width: 100% !important;
        border: none !important;
    }
    
    .stButton > button:hover {
        background-color: #000000 !important;
        color: white !important;
    }

    /* Professional BMI Result Card */
    .result-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin-top: 25px;
        border-left: 10px solid #004d57;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("# 👤 Personalised Fitness Plan Generator")
    st.write("---")
    st.write("Your professional fitness profile manager.")

# --- MAIN CONTENT ---
st.title("🏋️ Create Your Fitness Profile")

# SECTION 1: PERSONAL INFORMATION (Updated with Age and Gender)
st.markdown("### 1️⃣ Personal Information")
col_name, col_gender, col_age = st.columns([2, 1, 1])

with col_name:
    name = st.text_input("Full Name *", placeholder="e.g. John Doe")
with col_gender:
    gender = st.selectbox("Gender *", ["Male", "Female", "Other", "Prefer not to say"])
with col_age:
    age = st.number_input("Age *", min_value=1, max_value=120, value=25)

col_h, col_w = st.columns(2)
with col_h:
    height_cm = st.number_input("Height in centimeters *", min_value=0.0, step=0.1, format="%.1f")
with col_w:
    weight_kg = st.number_input("Weight in kilograms *", min_value=0.0, step=0.1, format="%.1f")

st.write("---")

# SECTION 2: FITNESS DETAILS
st.markdown("### 2️⃣ Fitness Details")
col_goal, col_level = st.columns(2)

with col_goal:
    goal = st.selectbox(
        "Fitness Goal",
        ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
    )

with col_level:
    level = st.selectbox(
        "Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

equipment = st.multiselect(
    "Available Equipment (Multiple selection allowed)",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "Kettlebells", "Pull-up Bar", "No Equipment"],
    default=["No Equipment"]
)

st.write("---")

# SECTION 3: FUNCTIONAL REQUIREMENTS & BMI CALCULATION
if st.button("Generate Workout Plan ✨"):
    # 5. Input Validation
    if not name:
        st.error("Validation Error: Please enter your Full Name.")
    elif height_cm <= 0 or weight_kg <= 0:
        st.error("Validation Error: Height and Weight must be positive numerical values.")
    else:
        # Convert height from cm to meters
        height_m = height_cm / 100
        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)
        # Round BMI to two decimal places
        bmi_rounded = round(bmi, 2)

        # Classify BMI into standard health categories
        if bmi_rounded < 18.5:
            category = "Underweight"
            color = "#3498db" # Blue
        elif 18.5 <= bmi_rounded < 25:
            category = "Normal"
            color = "#2ecc71" # Green
        elif 25 <= bmi_rounded < 30:
            category = "Overweight"
            color = "#f1c40f" # Yellow
        else:
            category = "Obese"
            color = "#e74c3c" # Red

        # 4. Display the user's name along with calculated BMI and category
        st.markdown(f"""
            <div class="result-card">
                <h2 style="color: #004d57; margin-top:0;">Assessment for {name}</h2>
                <p style="font-size: 1.1rem; color: #555;">{gender} | {age} Years Old</p>
                <hr>
                <p style="font-size: 1.2rem;">Your calculated BMI is: <strong>{bmi_rounded}</strong></p>
                <p style="font-size: 1.2rem;">Health Classification: <span style="color: {color}; font-weight: bold;">{category}</span></p>
            </div>
        """, unsafe_allow_html=True)
        
        st.success(f"Professional profile generated for {name}.")