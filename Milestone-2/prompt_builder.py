def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "#3498db"
    elif bmi < 25:
        return "Normal Weight", "#2ecc71"
    elif bmi < 30:
        return "Overweight", "#f1c40f"
    else:
        return "Obese", "#e74c3c"

def build_prompt(name, gender, age, height, weight, goal, fitness_level, equipment):
    bmi = calculate_bmi(weight, height)
    bmi_status, status_color = bmi_category(bmi)
    equipment_list = ", ".join(equipment) if equipment else "No Equipment"

    prompt = f"""You are a professional trainer. Create a 5-day plan for {name}.
User Profile:
- Age: {age} years old
- Gender: {gender}
- BMI: {bmi:.2f} ({bmi_status})
- Goal: {goal}
- Level: {fitness_level}
- Equipment: {equipment_list}

Requirements:
1. Label days strictly as Day 1, Day 2, Day 3, Day 4, and Day 5.
2. Adjust exercise selection and intensity based on the user's age and BMI.
3. For each exercise, provide: Name, Sets, Reps, and Rest.
4. Be concise and eliminate extra blank lines.
5. Day 3 must be Rest.
6. Only output the workout routine."""

    return prompt, bmi, bmi_status, status_color