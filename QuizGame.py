questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "prompt": "Which language is primarily used for Android apps?",
        "options": ["A. Swift", "B. Kotlin", "C. Python", "D. Ruby"],
        "answer": "B"
    },
    {
        "prompt": "What does RAM stand for?",
        "options": ["A. Random Access Memory", "B. Read Access Module", "C. Run All Memory", "D. Rapid Access Mode"],
        "answer": "A"
    }
]
def run_quiz(question_list):
    score = 0
    for q in question_list:
        print("\n" + q["prompt"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your choice (A, B, C, or D): ").strip().upper()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    print(f"\n--- Quiz Finished! ---")
    print(f"Your final score: {score}/{len(question_list)}")
while True:
    run_quiz(questions)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break