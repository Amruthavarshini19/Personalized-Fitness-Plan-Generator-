🏋️ Personalised Fitness Plan Generator - Milestone 1

🎯 Objective The primary objective of this milestone was to develop a professional, user-friendly frontend for a Fitness Profile Form. This form is designed to capture essential health and fitness details from users to serve as a foundation for generating personalized workout plans. Key focus areas included:

  UI/UX Design: Implementing a high-contrast, professional theme with a black sidebar and an orange-yellow gradient background.
  Data Collection: Establishing required fields for personal and fitness-related information.
  Health Metrics: Integrating real-time BMI (Body Mass Index) calculation and classification.
  Validation: Ensuring data integrity through robust input validation.

📐 BMI Formula & Logic

Unit Conversion Height is captured in centimeters (cm) and converted to meters (m) for the calculation:
Height(m) = Height(cm)/100

The Formula The Body Mass Index is calculated using the weight in kilograms and the square of the height in meters:
BMI = Weight(kg)/[Height(m)]^2

Classification Calculated BMI values are rounded to two decimal places and classified into the following health categories:
Underweight: BMI < 18.5
Normal: 18.5 ≤ BMI < 25.0
Overweight: 25.0 ≤ BMI < 30.0
Obese: BMI ≥ 30.0

🛠️ Steps Performed

I. Form Creation & Layout
Sidebar Development: Created a dedicated black sidebar for the application title and branding.
Input Grid: Utilized st.columns to create an organized grid for Personal Information (Name, Gender, Age) and Physical Stats (Height, Weight).
Selection Components: Implemented st.selectbox for Fitness Goals and Levels, and st.multiselect for equipment to allow for complex user profiles.

II. Input Validation
Requirement Checks: Implemented logic to ensure the "Full Name" field is not left empty.
Numerical Bounds: Added validation to prevent calculations if height or weight are entered as zero or negative values.
Professional Feedback: Integrated st.error messages to guide users in correcting invalid inputs.

III. BMI Logic Implementation
Dynamic Calculation: Integrated the BMI formula directly into the "Generate" trigger.
  Result Presentation: Designed a custom "Assessment Card" using HTML/CSS injection to display the user's specific health classification in a professional, readable format.

IV. Deployment
Environment Setup: Configured requirements.txt and streamlit_app.py.
Hugging Face Spaces: Successfully deployed the application to Hugging Face Spaces for public accessibility.
Project Hugging Face Link: https://huggingface.co/spaces/Amrutha04/AI-Fitness-Plan-Generator
