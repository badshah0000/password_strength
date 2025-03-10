import streamlit as st

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase check
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Number check
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Special character check
    special_chars = "!@#$%^&*()-+?_=,<>/"
    if any(char in special_chars for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Strength feedback
    if strength == 5:
        return "Strong", "Your password is strong!", "green"
    elif strength >= 3:
        return "Medium", "Your password is medium. " + " ".join(feedback), "orange"
    else:
        return "Weak", "Your password is weak. " + " ".join(feedback), "red"

def main():
    # Set page title and icon
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

    # Title with Streamlit
    st.title("🔒 Password Strength Meter")

    # Add a description
    st.write("Enter your password below to check its strength.")

    # Input field for password
    password = st.text_input("", type="password", placeholder="Enter your password here...")

    # Add some space
    st.write("")

    # Check password strength when input is provided
    if password:
        strength, feedback, color = check_password_strength(password)

        # Display strength with colored text
        if color == "green":
            st.success(f"Password Strength: {strength}")
        elif color == "orange":
            st.warning(f"Password Strength: {strength}")
        else:
            st.error(f"Password Strength: {strength}")

        # Display feedback
        st.info(feedback)

        # Add a progress bar for visual representation
        if strength == "Strong":
            st.progress(100)
        elif strength == "Medium":
            st.progress(60)
        else:
            st.progress(30)

    # Add a footer
    st.write("---")
    st.write("Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main()