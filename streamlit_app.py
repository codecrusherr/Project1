import numpy as np
import requests
import streamlit as st
from datetime import date, time
import pandas as pd
import nltk
import time as tm


# Download NLTK stopwords dataset
nltk.download('stopwords')

# Set up your Streamlit page
st.set_page_config(
    page_title="Web Dev - Streamlit",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/library/api-reference',
        'Report a bug': "https://docs.streamlit.io/library/api-reference",
        'About': "# This is Project 1 - Learning Streamlit for COP 4813 - Jose Suarez"
    }
)

st.title("Learning Streamlit")
st.header("Web Dev - Jose Suarez")

st.subheader("Personal Info")

first_name = st.text_input('First Name')
last_name = st.text_input('Last Name')
major = st.selectbox('What is your major',
                     ["", "Computer Science", "Information Technology", "CyberSecurity", "Data Science"])
campus = st.radio('Which campus are you at?',
                  ["MMC", "BBC", "EC"])
data_started = st.date_input("Start Date at FIU")
today = date.today().year

if first_name and last_name and major and campus and data_started:
    st.write("Hi,", first_name, "! You have been at FIU", campus, "for", str(today - data_started.year),
             "years studying",
             major, ".")
campuses_map = st.checkbox("See all the FIU campuses on the map")
if campuses_map:
    st.write("User selected the field")
    map_data = pd.DataFrame(
        np.array([
            [25.759005, -80.373825],
            [25.770459, -80.368130],
            [25.910728, -80.138982],
            [25.992332, -80.339832],
            [25.763418, -80.190564],
            [25.790110, -80.131561],
            [24.950351, -80.452974],
            [38.895549, -77.011910],
            [25.772754, -80.134411],
            [25.781113, -80.132460]]),
        columns=['lat', 'lon'])
    st.map(map_data)

st.subheader("Streamlit Features")

basic_plots = st.checkbox("Basic Plots")
if basic_plots:
    chart_data = pd.DataFrame(
        np.random.rand(20, 3),
        columns=["A", "B", "C"])
    st.line_chart(chart_data)

sliders = st.checkbox("Sliders")
if sliders:
    st.info("Integer slider for age")
    age = st.slider("How old are you?", 0, 130, 21)
    st.write("I'm", str(age), "years old!")

    st.info("Time slider for appointment")
    appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30), time(12, 45))
    )
    st.write("You're scheduled for:",
             appointment[0].strftime("%H:%M"),
             "to", appointment[1].strftime("%H:%M"))
    st.info("Float slider for a range")
    values = st.slider("Select a range of values",
                       0.0, 100.0, (25.0, 75.0))
    st.write("Value:", str(values))

audio = st.checkbox("Audio")
if audio:
    st.write("Waves and Birds")
    st.audio("https://bigsoundbank.com/UPLOAD/mp3/0267.mp3", format="media/mp3", start_time=0)

boxes = st.checkbox("Message boxes")
if boxes:
    st.success("This is a success box.")
    st.warning("This is a warning box")
    st.error("This is an error box")
    st.info("This is an info box")

balloons = st.checkbox("Surprise!")
if balloons:
    st.balloons()

progress_bar = st.checkbox("Progress Bar")
if progress_bar:
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i+1)
        tm.sleep(0.1)
