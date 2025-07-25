"""
Script to create the webapp with Streamlit.
"""

# Imports

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from src.streamlit_utils import predict_final, predict_letter

# Build app

st.write("## Hello!")
st.write(
    "Please write down your average grade for each assignment, and we will predict your final exam grade and final letter grade."
)

quiz = st.text_input("Quiz average, out of **20**.")
hw = st.text_input("Homework average, out of **20**.")
participation = st.text_input("Participation, out of **5**.")
midterm = st.text_input("Midterm average, out of **100**.")

grades = [float(quiz), float(hw), float(participation), float(midterm)]


if st.button("Show me my final exam grade!"):
    grade = predict_final(grades)
    st.write(f"**Predicted final exam grade: :primary[{grade[0]:.1f}]**")
    st.write(
        f"**Confidence interval: :primary[[{grade[1][0]:.1f}, {grade[1][1]:.1f}]]**"
    )
    st.write(
        f"**Prediction interval: :primary[[{grade[2][0]:.1f}, {grade[2][1]:.1f}]]**"
    )

if st.button("Show me my letter grade!"):
    grade_prediction, dic_proba = predict_letter(grades)

    # Reorder the dictionary and turn to percentage

    ordered_dic = {
        key: dic_proba[key] for key in ["A", "A-", "B+", "B", "B-", "C+", "C", "D", "F"]
    }
    ordered_dic_percent = {key: [f"{value:.1%}"] for key, value in ordered_dic.items()}

    # Display the results
    st.write(f"**Most likely letter grade: :primary[{grade_prediction}]**")
    st.write("**Probability of each grade:**")
    df = pd.DataFrame(ordered_dic_percent, index=["**Probability**"])
    st.table(df)

    # Add pie chart
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie(list(ordered_dic.values()), labels=list(ordered_dic.keys()))
    st.pyplot(fig, use_container_width=False)
