# grade-prediction
An analysis and prediction models for grades based on real data from NYU classes.

# Introduction

The data for this project are grades for the classes Math for Economics I, II, and III, from 2022 to 2023. The grades are the following.

- Participation, out of 5. This is evaluated by the TA.
- Quizzes (average of all quiz grades), out of 20. These are done at home with limited time and no help allowed.
- Homework (HW, average of all HW grades), out of 20. These are done at home with unlimited time and any resources are allowed.
- Midterm (1 or 2 per term), out of 100. These are done in class with limted time and no resources allowed.
- Final exam. This is done during the final exam week with limited time and no resources allowed.

Their final grade is calculated as a weighted average of all the above grade, with a slightly different scheme each time. Then, this final grade is turned into a letter grade (A, A-, B+, B, B-, C+, C, , F) according to thresholds that are slightly different each term.

The goal of this project is to use only the data of participation, quiz, homework, and midterm grades to predict the final grade. The idea is that a student should know or be able to estimate these rgades very well halfway through the semester. There are two aspects to this that we explore.

- Use these grades to predict the final exam point grade. This is a **regression** problem.
- Use the grades to predict the letter grade. This is a **classsification** problem.


|   | Quiz | HW | Participation | Midterm | Predicted final exam grade | CI lower           | CI upper          | PI lower           | PI upper           |
|---|------|----|---------------|---------|----------------------------|--------------------|-------------------|--------------------|--------------------|
| 0 | 18   | 19 | 5             | 95      | 90.85376010712676          | 89.25000785507676  | 92.45751235917676 | 65.03456669485195  | 116.67295351940157 |
| 1 | 8    | 11 | 5             | 60      | 56.06867192832385          | 51.876381412864696 | 60.26096244378301 | 29.96055007054732  | 82.17679378610038  |
| 2 | 19   | 20 | 3             | 50      | 59.553330874188774         | 56.284938492381166 | 62.82172325599638 | 33.57755146459343  | 85.52911028378412  |
| 3 | 17   | 6  | 0             | 85      | 69.87218467322361          | 61.55807280947013  | 78.1862965369771  | 42.794829129199265 | 96.94954021724797  |
| 4 | 12   | 19 | 5             | 65      | 68.49636097987694          | 65.66389987482647  | 71.32882208492741 | 42.571825051800545 | 94.42089690795333  |
