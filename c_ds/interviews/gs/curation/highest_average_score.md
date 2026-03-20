Task 2: Highest Average Score

You are given a list of student score records. Each record contains a student_id (string) and a score (integer). A student can appear multiple times.
Compute the average score per student (mean of all that student’s scores), and return the maximum average across all students.
Input: list of pairs [(student_id, score), ...]
Output: the highest average (as a floating-point value or as an exact rational; specify your choice during the interview)
Example Input: [("a", 80), ("b", 90), ("a", 100)]
avg(a) = (80 + 100) / 2 = 90
avg(b) = 90 Output: 90
Notes / Clarifications to ask:
Should ties return just the value, or also the student id(s)?
How should rounding be handled if the average is not an integer?
