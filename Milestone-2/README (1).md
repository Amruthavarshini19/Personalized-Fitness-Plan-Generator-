# 🏋️ FitPlan AI: Professional Fitness Plan Generator (Milestone 2)

---

## 🎯 Objective of the Milestone

The objective of this milestone was to transition from a local, low-parameter model to a high-performance Large Language Model (LLM) hosted via API.

This upgrade enables the generation of high-quality, personalized **5-day fitness routines** based on key user biometrics such as Age, Gender, BMI, and Fitness Goals.

### Key Technical Goals
- Implement multi-page navigation using **Streamlit Session State**
- Prevent response truncation via **Token Optimization**
- Improve output quality using a **Hosted LLM API**

---

## 🤖 Model Used

- **Model:** `mistralai/Mistral-7B-Instruct-v0.2`  
- **Provider:** Hugging Face  
- **Access Method:** Hugging Face Inference API  

This shift removed heavy local model loading and enabled faster deployment with lower RAM usage.

---

## ✍️ Prompt Design Explanation

The prompt is designed using a **Structured Instruction Template** inside `prompt_builder.py`.

### 🔹 Context Framing
The AI is instructed to behave as a:

**Certified Professional Fitness Trainer**

This improves realism and domain accuracy.

---

### 🔹 Dynamic User Data Injection
The prompt safely injects:
- Age  
- Gender  
- BMI  
- Fitness Level  

This ensures personalization for each user.

---

### 🔹 Constraint-Based Output Design
Strict instructions enforce:
- A structured **5-day workout split**
- Mandatory formatting using `Day X:` markers
- Logical constraints (e.g., **Day 3 = Rest Day**)

This enables:
- Easy parsing
- Structured UI rendering

---

### 🔹 Token Efficiency Controls
To prevent truncation:
- Reduced conversational filler
- Minimized vertical spacing
- Optimized instruction compactness

Final safe configuration:
- `max_tokens = 1500`
- `temperature = 0.7`

This guarantees **complete 5-day outputs**.

---

## 🛠️ Steps Performed

### 1️⃣ Model Loading via API
- Integrated `huggingface_hub.InferenceClient`
- Removed local model dependencies
- Reduced memory usage significantly
- Faster Hugging Face Space startup

---

### 2️⃣ Modular Prompt Builder
Created a reusable `build_prompt()` function that:
- Calculates BMI
- Determines BMI category
- Injects structured instructions dynamically

---

### 3️⃣ Inference Optimization
Extensive testing performed to:
- Avoid response cut-offs
- Maintain generation quality
- Ensure Day 5 is always produced

Final parameters:
- `max_tokens: 1500`
- `temperature: 0.7`

---

### 4️⃣ Streamlit UI Enhancement
Implemented **Session State Navigation**:

**Page 1 → User Input Form**  
- Personal details  
- Fitness level  
- Goals  

**Page 2 → AI Generated Plan**  
- Structured 5-day workout  
- Clean display layout  

This creates a **multi-page app feel** inside Streamlit.

---


---

## 🚀 Deployment

### 🌐 Hugging Face Space
🔗 **Live App:**  
https://huggingface.co/spaces/Amrutha04/Fit_Plan_Module_2

---

## ✅ Milestone Outcome

✔ Migrated from local model → Hosted LLM  
✔ Improved scalability and performance  
✔ Achieved structured, high-quality AI outputs  
✔ Implemented multi-page Streamlit navigation  
✔ Production-ready AI fitness generator

---

> 🚀 This milestone marks the transition from a prototype AI app to a scalable, deployment-ready intelligent fitness planning system.
