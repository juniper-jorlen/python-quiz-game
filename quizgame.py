# Python Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "options": {
            "A": "Berlin",
            "B": "Madrid",
            "C": "Paris",
            "D": "Rome"
        },
        "answer": "C"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": {
            "A": "function",
            "B": "define",
            "C": "func",
            "D": "def"
        },
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": {
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Program Utility",
            "D": "Control Processing User"
        },
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Earth",
            "B": "Mars",
            "C": "Venus",
            "D": "Jupiter"
        },
        "answer": "B"
    },
    {
        "question": "What is 5 × 6?",
        "options": {
            "A": "11",
            "B": "25",
            "C": "30",
            "D": "35"
        },
        "answer": "C"
    }
]

score = 0

print("=" * 30)
print("      Python Quiz Game")
print("=" * 30)

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}")
    print(q["question"])

    for key, value in q["options"].items():
        print(f"{key}. {value}")

    user_answer = input("\nYour answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        correct = q["options"][q["answer"]]
        print(f"Wrong! The correct answer was {q['answer']}. {correct}")

print("\n" + "=" * 30)
print(f"You scored {score} out of {len(questions)}.")

percentage = (score / len(questions)) * 100

if percentage == 100:
    print("Perfect score! ")
elif percentage >= 80:
    print("Great job!")
elif percentage >= 60:
    print("Good effort!")
else:
    print("Keep practicing!")

print("=" * 30)