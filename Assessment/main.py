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
    for question in questions:
        print(f"Question: {question['Questions']}, Options: {question['Options']}")
        answer = input("Please type your answer (a, b, c, or d):  ")
        if answer == question['Answer']:
            print("Correct")
            score += 1
            print (f"Your score is {score}")
        else:
            print("Incorrect")
            
    # presenting the user with a message that says topic complete, and gives them a final score for that topic.
    

def main():
    score = 0
    welcome_to_the_quiz()

    play_quiz = input("are you ready? ")
    while play_quiz == "yes":
        filtered_questions = filter_by_topic(questions)
        if filtered_questions:
            print_questions(score, filtered_questions)  # Print the filtered questions
        play_quiz = input("would you like to play again?")


    



   

main()