def quiz_game(): 
    questions = [
        {
            "question" : "what is the full form of cpu?",
            "options" : ["a) control proccesing unit", "b) central processing unit", "c) central personal unit","d) central process unit"],
            "answer" : "b"
        },
        {
            "question" : "Which planet is known as the Red Planet?",
            "options" : ["a) earth", "b) jupiter", "c) mars", "d) venus"],
            "answer" : "c"
        },
        {
            "question" : "Who painted the famous artwork Mona Lisa?",
            "options" : ["a) vincent van gogh", "b) pablo picasso", "c) leonardo da vinci", "d) michelangelo"],
            "answer" : "c"
        },
        {
            "question" : "What is the capital city of Japan?",
            "options" : ["a) beijing", "b) washington dc", "c) delhi", "d) tokyo"],
            "answer" : "d"
        }, 
        {
            "question" : "Who was the first person to step on the Moon?",
            "options" : [ "a) neil armstrong", "b) yuri gagrin", "c) buzz aldrin","d) michael collins"],
            "answer" : "a"
        },
        {
            "question" : "Which is the largest ocean on Earth?",
            "options" : [ "a) indian ocean", "b) pacific ocean", "c) atlantic ocean", "d) arctic ocean"],
            "answer" : "b"
        },
        {
            "question" : "What gas do humans exhale when they breathe out?",
            "options" : [ "a) oxygen", "b) helium", "c) hydrogen", "d) carbon dioxide"],
            "answer" : "d"
        },
        {
            "question" : "What is the smallest prime number?",
            "options" : [ "a) 2", "b) 0", "c) 3", "d) 1"],
            "answer" : "a"
        },
        {
            "question" : "In which sport is the term hat-trick commonly used?",
            "options" : [ "a) football", "b) cricket", "c) hockey","d) tennis"],
            "answer" : "b"
        },
        {
            "question" : "Which animal is known as the Ship of the Desert?",
            "options" : [ "a) horse", "b) goat", "c) donkey", "d) camel"],
            "answer" : "d"
        },
    ]
    score = 0
    for q in questions:
        print(q["question"])
        for options in q["options"]:
            print(options)
        ans = input("enter your answer:").strip().lower()

        if ans == q["answer"]:
            print("correct✅\n")
            score += 1
        else:
             print(f"wrong❌ The correct answer was:{q["answer"]}\n")
    print(f"\nyour final score is {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Your score: {percentage:.2f}%")
    if score == len(questions):
        print("🌟 Excellent! You got everything right!")
    elif score>= len(questions)*0.7:
        print("👍 Good job! Keep practicing to become even better.")
    else:
        print("📘 Needs Improvement. Dont worry, keep learning and youll improve!")
while True:
    quiz_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Bye 👋")
        break


