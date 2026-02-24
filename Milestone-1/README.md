# 🏋️ Personalized Fitness Plan Generator - Milestone 1

---

## 🎯 Objective

The primary objective of this milestone was to develop a professional, user-friendly frontend for a Fitness Profile Form.

This form captures essential health and fitness details from users to serve as a foundation for generating personalized workout plans.

### Key Focus Areas:

- **UI/UX Design:** High-contrast professional theme with a black sidebar and orange-yellow gradient background.
- **Data Collection:** Required fields for personal and fitness-related information.
- **Health Metrics:** Real-time BMI (Body Mass Index) calculation and classification.
- **Validation:** Ensuring data integrity through strong input validation.

---

## 📐 BMI Formula & Logic
BMI = Weight (kg) / [Height (m)]^2

### 🔹 Unit Conversion

Height is captured in centimeters (cm) and converted to meters (m):

### 🔹 BMI Formula

### 🔹 Classification

Calculated BMI values are rounded to two decimal places and classified as:

- **Underweight:** BMI < 18.5  
- **Normal:** 18.5 ≤ BMI < 25.0  
- **Overweight:** 25.0 ≤ BMI < 30.0  
- **Obese:** BMI ≥ 30.0  

---

## 🛠 Steps Performed

### I. Form Creation & Layout Development
- Created a dedicated black sidebar for branding.
- Used `st.columns` to organize personal and physical information.
- Implemented `st.selectbox` for fitness goals and levels.
- Used `st.multiselect` for equipment selection.

### II. Input Validation
- Ensured "Full Name" field is not empty.
- Prevented zero or negative values for height and weight.
- Displayed professional error messages using `st.error`.

### III. BMI Logic Implementation
- Integrated BMI formula into the **Generate** trigger.
- Designed a custom assessment card using HTML/CSS injection.

### IV. Deployment Setup
- Configured `requirements.txt` and `streamlit_app.py`.
- Successfully deployed the application to Hugging Face Spaces.

🔗 **Live Project Link:**  
https://huggingface.co/spaces/Amrutha04/AI-Fitness-Plan-Generator
