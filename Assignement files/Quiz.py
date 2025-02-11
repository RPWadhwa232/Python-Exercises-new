import os
import time

# Function to clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Welcome Screen
def welcome_screen():
    clear_screen()
    print("*********************************")
    print("*  Welcome to the Quiz Game!   *")
    print("*  Developed by: RP Wadhwa     *")
    print("*  Year of Release: 2025 *")
    print("*********************************")
    input("\nPress Enter to continue...")
    clear_screen()

# Help Function
def help_menu():
    clear_screen()
    print("******** HELP MENU ********")
    print("1. The quiz consists of 5 multiple-choice questions.")
    print("2. Each question has 4 possible answers.")
    print("3. Select the correct option (A, B, C, or D) to earn points.")
    print("4. You can return to the main menu at any time.")
    print("5. Good luck and have fun!\n")
    input("Press Enter to return to the menu...")
    clear_screen()

# Quiz Questions
def play_quiz():
    clear_screen()
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which programming language is known as the 'mother of all languages'?",
            "options": ["A) Python", "B) C", "C) Java", "D) Assembly"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
            "answer": "D"
        },
        {
            "question": "Which animal is known as the king of the jungle?",
            "options": ["A) Elephant", "B) Lion", "C) Tiger", "D) Giraffe"],
            "answer": "B"
        }
    ]

    score = 0
    for q in questions:
        clear_screen()
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q["answer"]:
            print("\nCorrect! 🎉")
            score += 1
        else:
            print(f"\nIncorrect. The correct answer was {q['answer']}. ❌")

        print(f"Your current score: {score}/{len(questions)}")
        time.sleep(2)  # Pause before next question

    print("\nQuiz Completed!")
    print(f"Final Score: {score}/{len(questions)}")
    input("\nPress Enter to return to the menu...")
    clear_screen()

# Menu System
def main_menu():
    while True:
        print("******** MAIN MENU ********")
        print("1) Help")
        print("2) Play Quiz")
        print("3) Quit")
        
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            help_menu()
        elif choice == "2":
            play_quiz()
        elif choice == "3":
            print("\nThank you for playing! Goodbye! 😊")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

# Run the application
welcome_screen()
main_menu()
