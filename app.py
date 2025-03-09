import streamlit as st
import re
import random
import string

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    count = 0
    suggestions = []
    
    if len(password) >= 8:
        count += 1
    else:
        suggestions.append("Password must be at least 8 characters long")
        
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        count += 1
    else:
        suggestions.append("Password must contain both uppercase and lowercase letters")
    
    if re.search("[0-9]", password):
        count += 1
    else:
        suggestions.append("Password must contain at least one number")
    
    if re.search("[!@#$%^&*()]", password):
        count += 1
    else:
        suggestions.append("Password must contain at least one special character")
    
    if count == 4:
        return "✅ Strong Password"
    elif count == 3:
        return "⚠️ Medium Password - " + ", ".join(suggestions)
    else:
        return "❌ Weak Password - " + ", ".join(suggestions)

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered", initial_sidebar_state="expanded")
st.title("Password Strength Meter")

password = st.text_input("Enter your password here!", type="password", max_chars=15)

if st.button("Check Strength"):
    if password:
        strength = password_strength(password)
        st.write(strength)
    else:
        st.warning("Please enter a password to check.")

if st.button("Generate Password"):
    new_password = generate_password()
    st.markdown(f'🔑 Try this strong password: `{generate_password()}`')
    

st.markdown("""            
            **Note:** This is a simple password strength meter. It checks if your password has at least 8 characters, 
            both uppercase and lowercase letters, at least one number, and at least one special character. 
            The password is generated randomly and is not stored anywhere.
             """)    