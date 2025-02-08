# Program Name: Assignment2.py
# Course: IT3883/Section XXX
# Student Name: John Doe
# Assignment Number: Lab#
# Due Date: xx/xx/20XX
# Purpose: This program calculates the average score for a list of students based on their provided scores and displays the results in descending order of average.
# List Specific resources used to complete the assignment: Python Standard Library

def calculate_averages(filename):
    with open(filename, 'r') as file:
        student_scores = file.readlines()

    # Creating a list to store the name and average score
    averages = []
    for score in student_scores:
        parts = score.split()
        name = parts[0]
        scores = list(map(int, parts[1:]))  # Convert scores to integers
        average = sum(scores) / len(scores)  # Calculate average
        averages.append((name, average))

    # Sort the list by the average score in descending order
    averages.sort(key=lambda x: x[1], reverse=True)
    
    # Print the results
    for name, average in averages:
        print(f"{name} {average:.2f}")

# Calling the function with the provided file name
calculate_averages('input.txt')
