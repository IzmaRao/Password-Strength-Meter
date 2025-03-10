import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "success", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "warning", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", "error", feedback

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

# Custom CSS for Elegant Design
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Poppins', sans-serif;
        }
        .stApp {
            background: linear-gradient(135deg, #1f1c2c, #928dab);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        }
        .stTextInput > div > div > input {
            background-color: #2e2e2e;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton button {
            background-color: #6a11cb;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #2575fc;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Meter")
st.markdown("### Check the security of your password & improve it!")

password = st.text_input("Enter your password", type="password")
if password:
    result, status, feedback = check_password_strength(password)
    st.toast(result, icon="✅" if status == "success" else "⚠️")
    
    if status == "error":
        for msg in feedback:
            st.warning(msg)
    else:
        for msg in feedback:
            st.info(msg)
    
    st.divider()

st.subheader("🔑 Need a strong password?")
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.code(strong_password, language='plaintext')