# Program Name: Assignment2.py (use the name the program is saved as)
# Course: IT3883/Section 114
# Student Name: Brendon Antoine 
# Assignment Number: Assingment 2
# Due Date: 9/19/ 2025
# Purpose: This program takes the input of six students and their scores, calculates the average score for each student, and then outputs the students' names along with their average scores in descending order.
# List Specific resources used to complete the assignment. I have used the VSCode auto-formatting and auto-completion tools to help me with the indentation of my code.


output = []

with open("Assignment2input.txt", "r") as f:
    for line in f:
        parts = line.split()
        name = parts[0]
        scores = [int(x) for x in parts[1:]]
        average = sum(scores) / len(scores)
        output.append((name, average))

results_sorted = sorted(output, key=lambda x: x[1], reverse=True)

for name, avg in results_sorted:
    print(f"{name}: {avg:.2f}")
