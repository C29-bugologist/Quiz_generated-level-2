import random

# Sample question bank (expand with more topics and questions!)
question_bank = {
    "science": [
        {"text": "What is the capital of France?", "choices": ["London", "Paris", "Berlin"], "answer": 1},
        {"text": "What is the formula for water?", "choices": ["H2O", "CO2", "NH3"], "answer": 0},
        {"text": "What is the largest planet in our solar system?", "choices": ["Earth", "Jupiter", "Mars"], "answer": 1},
    ],
    "history": [
        {"text": "Who painted the Mona Lisa?", "choices": ["Leonardo da Vinci", "Michelangelo", "Vincent van Gogh"], "answer": 0},
        {"text": "What year did World War II begin?", "choices": ["1914", "1939", "1945"], "answer": 1},
        {"text": "What is the capital of ancient Rome?", "choices": ["Athens", "Rome", "Sparta"], "answer": 1},
    ],
    "geography": [
        {"text": "What is the highest mountain in the world?", "choices": ["Mount Everest", "K2", "Kangchenjunga"], "answer": 0},
        {"text": "What continent is the Amazon rainforest located in?", "choices": ["South America", "Africa", "Asia"], "answer": 0},
        {"text": "What is the largest ocean on Earth?", "choices": ["Pacific", "Atlantic", "Indian"], "answer": 0},
    ],
}
while True:
    print("\nQuiz Generator (Multiple Topics)")
    print("Available topics:\n")
    for topic in question_bank:
        print(topic)
    print("1. Generate Quiz")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1' :
        topic = input("Enter the topic for the quiz: ")

        if topic not in question_bank:
            print(f"Topic '{topic}' not found. Please choose from available topics.")
            continue

        num_questions = int(input("Enter the number of questions: "))
        filtered_questions = question_bank[topic]
        random_question = random.sample(filtered_questions, num_questions)

        score = 0

        for question in random_question:
            print(question["text"])
            for i,choice in enumerate(question["choices"]):
                print(i+1 ,choice )
            user_answer = int(input("Enter your answer (number): ")) - 1
            if user_answer == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The answer is {question['choices'][question['answer']]}")
        print(f"\nYou scored {score} out of {num_questions} questions.")

    elif choice == '2':
        break
    else:
        print("Invalid choice!")

print("Exiting Quiz Generator...")









# while True:
#     print("\nQuiz Generator (Multiple Topics)")
#     print("Available topics:\n")
#     for topic in question_bank:
#         print(topic)
#     print("1. Generate Quiz")
#     print("2. Exit")
#     choice = input("Enter your choice: ")

#     if choice == '1':
#         topic = input("Enter the topic for the quiz: ")

#         if topic not in question_bank:
#             print(f"Topic '{topic}' not found. Please choose from available topics.")
#             continue

#         num_questions = int(input("Enter the number of questions: "))
#         # Filter questions for the chosen topic
#         filtered_questions = question_bank[topic]

#         # Randomly select questions without duplicates
#         questions = random.sample(filtered_questions, num_questions)

#         # Present the quiz
#         score = 0
#         for question in questions:
#             print(question["text"])
#             for i, choice in enumerate(question["choices"]):
#                 print(f"{i+1}. {choice}")
#             user_answer = int(input("Enter your answer (number): ")) - 1
#             if user_answer == question["answer"]:
#                 print("Correct!")
#                 score += 1
#             else:
#                 print(f"Incorrect. The answer is {question['choices'][question['answer']]}")
#         print(f"\nYou scored {score} out of {num_questions} questions.")

#     elif choice == '2':
#         break
#     else:
#         print("Invalid choice!")

# print("Exiting Quiz Generator...")