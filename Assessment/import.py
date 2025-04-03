import random  # Import the random module
from questions import questions

def filter_by_topic(questions):
    print("What topic would you like to play: Who | What | Where")
    player_choice = input("Type in a topic: ")
    print(f"You chose: {player_choice}")
    filtered_questions = []
    
    for question in questions:
        if question["Topic"].lower() == player_choice.lower():  # Case insensitive comparison
            filtered_questions.append(question)
    
    if not filtered_questions:
        print("No questions found for that topic.")
    
    return filtered_questions

def welcome_to_the_quiz():
    print("Welcome to the Quiz!!")

def print_questions(score, questions):
    question_number = 0  
    for question in questions:
        print(f"Question: {question['Questions']}, Options: {question['Options']}")
        answer = input("Please type your answer (a, b, c, or d):  ")
        if answer == question['Answer']:
            print("Correct")
            score += 1
            question_number += 1    
            print(f"Your score is {score}/{question_number} out of {len(questions)} questions")
        else:
            question_number += 1
            print("Incorrect")
            print(f"Your score is {score}/{question_number} out of {len(questions)} questions")

    # Presenting the user with a message that says topic complete, and gives them a final score for that topic.
    print(f"Topic complete! Your final score for this topic is {score}/{len(questions)}.")

def main():
    score = 0
    welcome_to_the_quiz()

    play_quiz = input("Are you ready? (yes/no): ").strip().lower()
    while play_quiz == "yes":
        filtered_questions = filter_by_topic(questions)
        if filtered_questions:
            # Ask the user how many questions they want to answer
            num_questions = int(input(f"How many questions would you like to answer (max {len(filtered_questions)}): "))
            num_questions = min(num_questions, len(filtered_questions))  # Ensure we don't exceed available questions
            
            # Randomly select questions
            selected_questions = random.sample(filtered_questions, num_questions)
            
            print_questions(score, selected_questions)  # Print the selected questions
        play_quiz = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_quiz == "no":
        print("Thanks for playing!")
main()