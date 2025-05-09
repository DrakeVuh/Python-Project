class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt + " ")
        if user_answer.lower() == question.answer.lower():
            score += 1
    return score

def main():
    print("Python Quiz Game")
    print("Answer the following questions to test your Python knowledge.")

    questions = [
        Question("What is the capital of France?", "Paris"),
        Question("What is the capital of Germany?", "Berlin"),
        Question("What is the capital of Italy?", "Rome"),
        Question("What is the capital of Spain?", "Madrid"),
        Question("What is the capital of Portugal?", "Lisbon"),
        Question("What is the capital of Greece?", "Athens"),
        Question("What is the capital of Turkey?", "Ankara"),
        Question("What is the capital of Egypt?", "Cairo"),
    ]

    score = run_quiz(questions)
    print(f"You scored {score} out of {len(questions)}")

if __name__ == "__main__":
    main()
