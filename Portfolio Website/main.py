import streamlit as st

st.title("Portfolio")
st.write("**Hi, my name is Kobina. I do computer Science and this is my portfolio website. I have used streamlit to develop this website.**")
st.divider()
st.header("Projects")
st.caption("**I used pyinstaller to convert my python projects from .py to .exe files.**")

def calc_app():
    st.subheader("Calculator App")
    st.caption("**This is my first ever project. It is a very simple calculator.**")
    with open("projects/calculator-app.exe", "rb") as file:
        btn = st.download_button(
            label="Click to Download Calculator App",
            data=file,
            file_name="calculator-app.exe",
            mime="application/octet-stream"
    )

def notes_app():
    st.subheader("Notes App")
    st.caption("**This is a notes app where you can save files with text.**")
    with open("projects/notes-app.exe", "rb") as file:
        btn = st.download_button(
            label="Click to Download Notes App",
            data=file,
            file_name="notes-app.exe",
            mime="application/octet-stream"
        )

calc_app()
notes_app()