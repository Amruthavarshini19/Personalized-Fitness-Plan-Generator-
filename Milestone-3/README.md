# 🔐 FitPlan AI – Milestone 3: Authentication & Security System

## 🎯 Milestone Objective
The objective of this milestone was to implement a **secure authentication system** for the FitPlan AI application.  
This milestone introduces **user registration, login authentication, session handling, and secure database management** to ensure that user information remains protected and accessible only to authorized users.

---

## 🔐 Authentication System

### 🔑 Sign In Process
- Users authenticate using **email and password**
- Successful login generates a **JWT authentication token**
- The token is used to maintain secure access during the session

### 📝 Sign Up Process
- Multi-step **OTP-based verification system**
- User provides email and password
- A **6-digit OTP** is sent to the user’s email
- The account is activated only after OTP verification

### 🔄 Session Management
- Maintains **secure user state** throughout the application
- Prevents unauthorized access to protected features
- Tracks authenticated user sessions safely

---

## 🗄️ Database Architecture

### 📂 SQLite Database
- Database file: `users.db`
- Stores registered user information securely

### 🧱 Database Schema
Includes fields such as:
- User ID
- Email
- Password Hash
- Verification Status

### 🔒 Security Features
- **Password hashing using Werkzeug**
- **Unique email constraints** to prevent duplicate accounts
- Proper validation checks during registration

### ⚙️ Database Operations
Functions implemented include:
- User registration
- OTP verification
- Duplicate email detection
- Secure user authentication

---

## 🔒 Security Implementation

### 🔑 JWT Authentication
- Generates secure **JSON Web Tokens (JWT)** after successful login
- Tokens are verified for protected application actions
- Ensures authenticated access to application features

### 🔢 OTP Verification System
- Secure **6-digit OTP generation**
- OTP delivered through **email verification**
- Prevents unauthorized account creation

### 🔐 Password Security
- Implemented **PBKDF2 password hashing**
- Automatic **salt generation**
- Protects stored passwords from brute-force attacks

---

## 🛠️ Technical Details

### 📦 Dependencies
Key libraries used:

- Flask / Backend framework  
- Werkzeug for password hashing  
- PyJWT for authentication tokens  
- SQLite for database storage  
- Email libraries for OTP delivery  

### 📁 File Structure
Authentication-related files include:

- `auth.py` – Authentication logic  
- `database.py` – Database operations  
- `otp_utils.py` – OTP generation and verification  
- `jwt_handler.py` – JWT token creation and validation  

*(File names may vary depending on the project structure.)*

### 🔄 Session Management
- Tracks authentication state securely
- Stores user data during active sessions
- Prevents unauthorized access to protected pages

---

## 🚀 Getting Started

### ⚙️ Installation Steps

1. Clone the repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python app.py
```

---

### ▶️ Usage Instructions

**Sign Up**
- Enter email and password
- Verify your account using the OTP sent to your email

**Sign In**
- Login using registered credentials
- Authentication token is generated for secure session access

---

## 🛡️ Security Features Implemented

- Email OTP verification
- Secure password hashing
- JWT-based authentication
- Protected user sessions
- Duplicate account prevention

---

## ✅ Milestone Outcome

This milestone successfully introduced a **complete authentication and security layer** for the FitPlan AI system.  
It enables safe **user registration, login authentication, OTP verification, session management, and database security**, ensuring that sensitive user data remains protected.
