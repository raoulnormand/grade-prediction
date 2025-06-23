"""
Functions for cleaning the raw data. All files include
_ Quiz average (out of 20, labeled "Quiz").
_ Homework average (out of 20, labeled "HW").
_ Participation grade (out of 5, labeled "Participation").
_ Midterm grades (1 or 2 for each class, labeled "Midterm" or "Exam").
_ Final exam grade (labeled "Final")
_ Letter grade (A, A-, B+, B, B-, C+, C, D, F, labeled "Letter grade").

"""

import os

import pandas as pd


def clean_df(grades_df):
    """
    Creates average of quizzes, HW, and exams (if necessary).
    """

    cols = ["Email", "Quiz", "HW", "Participation", "Final", "Letter grade"]
    cleaned_df = grades_df[cols].copy()

    # Fina exam columns, labeled "Midterm" or "Exam". Files also include the number of missed exams so these columns are excluded.
    exam_cols = [
        col
        for col in grades_df.columns
        if ("Midterm" in col or "Exam" in col) and "missed" not in col
    ]
    cleaned_df["Exams"] = grades_df[exam_cols].mean(axis=1)

    return cleaned_df


# Clean all files.


def main():
    """
    Combine all files, and delete duplicate emails, then delete email for anonymity.
    """
    file_names = os.listdir("data/raw")

    for file_name in file_names:
        grades_df = pd.read_csv("data/raw/" + file_name, index_col=False)
        cleaned_df = clean_df(grades_df)
        cleaned_df.to_csv("data/cleaned/" + file_name, index=False)

    dfs = [
        pd.read_csv("data/cleaned/" + file_name, index_col=False)
        for file_name in file_names
    ]

    all_grades = pd.concat(dfs, ignore_index=True)
    all_grades.drop_duplicates(subset="Email", inplace=True)
    all_grades.drop("Email", axis=1, inplace=True)
    all_grades.to_csv("data/final/all_grades.csv", index=False)


if __name__ == "__main__":
    main()
