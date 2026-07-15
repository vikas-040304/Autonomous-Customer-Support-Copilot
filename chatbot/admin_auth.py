import streamlit as st

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "12345"

def login():

    st.title("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if (
            username == ADMIN_USERNAME
            and
            password == ADMIN_PASSWORD
        ):

            st.session_state.admin = True
            st.success("Login Successful")
            st.rerun()

        else:

            st.error("Invalid Username or Password")