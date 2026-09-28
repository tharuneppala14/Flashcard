import random

flashcards = [
    {
        "question": "What is the full form of CPU?",
        "answer": "Central Processing Unit"
    },
    {
        "question": "What is the full form of RAM?",
        "answer": "Random Access Memory"
    },
    {
        "question": "Which language is used to create web pages?",
        "answer": "HTML"
    },
    {
        "question": "What is the extension of a Python file?",
        "answer": ".py"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "answer": "#"
    }
]

random.shuffle(flashcards)

score = 0

print("===== Flashcard Quiz =====")

for card in flashcards:
    print("\nQuestion:", card["question"])

    user_answer = input("Your Answer: ")

    if user_answer.lower() == card["answer"].lower():
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", card["answer"])

print("\n===== Result =====")
print("Total Questions:", len(flashcards))
print("Correct Answers:", score)
print("Wrong Answers:", len(flashcards) - score)

print("Your Score:", score, "/", len(flashcards))
