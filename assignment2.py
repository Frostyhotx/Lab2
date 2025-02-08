# Program Name: Assignment2.py
# Course: Adv Application Development Section W02
# Student Name: Foster North
# Assignment Number: Lab2
# Due Date: 2/07/2025
# Purpose: This program finds and lists the averages of students based on input from the input.txt file.

def calculate_averages(filename):
    with open(filename, 'r') as file:
        student_scores = file.readlines()

    # creates a list to store the students scores and average them
    averages = []
    for score in student_scores:
        parts = score.split()
        name = parts[0]
        scores = list(map(int, parts[1:]))  # Convert scores to integers
        average = sum(scores) / len(scores)  # Calculate average
        averages.append((name, average))

    # sorts the scores from the highest down
    averages.sort(key=lambda x: x[1], reverse=True)
    
    # prints the results from the line above
    for name, average in averages:
        print(f"{name} {average:.2f}")

# calls the text file for the input given in the assignment instructions
calculate_averages('input.txt')
