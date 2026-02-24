import streamlit as st
from prompt_builder import build_prompt 
from model_api import query_model 

# 1. Page Configuration
st.set_page_config(page_title="FitPlan AI", layout="wide")

# 2. Custom Styling (Preserving your exact UI style)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); background-attachment: fixed; }
    section[data-testid="stSidebar"] { background-color: #000000 !important; }
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] p { color: #FFFFFF !important; }
    h1, h2, h3, p, label { color: #2D3436 !important; font-weight: 600; }
    .result-card { 
        background-color: white !important; padding: 25px; border-radius: 15px; 
        border-left: 10px solid #004d57; color: #000000 !important; margin-bottom: 20px;
    }
    .day-card {
        background-color: #ffffff !important; padding: 20px 30px !important; 
        border-radius: 15px; margin-bottom: 20px; border-left: 10px solid #004d57; 
        color: #000000 !important; white-space: pre-line !important;
        line-height: 1.4 !important; box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .day-card p, .day-card ul, .day-card li { margin: 2px 0 !important; text-align: left !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialize Session State for Page Navigation
if 'page' not in st.session_state:
    st.session_state.page = 'input'
if 'workout_plan' not in st.session_state:
    st.session_state.workout_plan = None
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("# 👤 Personalised Fitness Plan")
    st.write("---")
    if st.session_state.page == 'result':
        if st.button("⬅️ New Profile / Back"):
            st.session_state.page = 'input'
            st.rerun()

# --- PAGE 1: INPUT FORM ---
if st.session_state.page == 'input':
    st.title("🏋️ Create Your Fitness Profile")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1: name = st.text_input("Name", value=st.session_state.user_data.get('name', ''))
    with col2: gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with col3: age = st.number_input("Age", min_value=1, value=st.session_state.user_data.get('age', 19))

    col_h, col_w = st.columns(2)
    with col_h: height = st.number_input("Height (cm)", min_value=1.0, value=st.session_state.user_data.get('height', 170.0))
    with col_w: weight = st.number_input("Weight (kg)", min_value=1.0, value=st.session_state.user_data.get('weight', 65.0))

    goal = st.selectbox("Goal", ["Build Muscle", "Weight Loss", "Strength", "Flexibility"])
    level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
    equip = st.multiselect("Equipment", ["Dumbbells", "Kettlebells", "Pull-up Bar", "Resistance Bands", "Yoga Mat", "No Equipment"])

    if st.button("Submit Profile"):
        if not name or height <= 50.0 or weight <= 10.0:
            st.error("Please fill in valid details.")
        else:
            with st.spinner("Analyzing profile and generating routine..."):
                prompt, bmi, bmi_status, status_color = build_prompt(name, gender, age, height, weight, goal, level, equip)
                raw_workout = query_model(prompt)
                
                if "Error" in raw_workout:
                    st.error("API Error. Please check your HF Token.")
                else:
                    st.session_state.workout_plan = raw_workout
                    st.session_state.assessment_data = {
                        "name": name, "bmi": bmi, "status": bmi_status, "color": status_color, "age": age, "gender": gender
                    }
                    st.session_state.user_data = {"name": name, "age": age, "height": height, "weight": weight}
                    st.session_state.page = 'result'
                    st.rerun()

# --- PAGE 2: RESULTS PAGE ---
elif st.session_state.page == 'result':
    data = st.session_state.assessment_data
    st.title("📋 Your Personalized Routine")
    
    st.markdown(f"""
        <div class="result-card">
            <h2>Hello {data['name']}</h2>
            <p>{data['gender']} | {data['age']} Years Old</p>
            <p>BMI: <strong>{data['bmi']:.2f}</strong> | Category: <span style="color:{data['color']}">{data['status']}</span></p>
        </div>
    """, unsafe_allow_html=True)

    

    raw_content = st.session_state.workout_plan
    days = ["Day 1:", "Day 2:", "Day 3:", "Day 4:", "Day 5:"]
    
    for i in range(len(days)):
        start = raw_content.find(days[i])
        if start != -1:
            end = raw_content.find(days[i+1]) if i+1 < len(days) else len(raw_content)
            day_text = raw_content[start:end].strip()
            # Clean empty spaces logic
            clean_text = "\n".join([line for line in day_text.splitlines() if line.strip()])
            st.markdown(f'<div class="day-card">{clean_text}</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.download_button(
        label="📥 Download Full Plan",
        data=st.session_state.workout_plan,
        file_name=f"{data['name']}_Workout_Plan.txt",
        mime="text/plain"
    )