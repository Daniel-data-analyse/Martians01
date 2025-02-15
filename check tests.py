# Правильные ответы для каждого вопроса
correct_answers = [
    "б", "б", "а", "а", "в", "а", "б", "а", "в", "б",
    "б", "а", "а", "в", "б", "а", "а", "в", "б", "в",
    "б", "в", "в", "г", "в", "б", "б", "а", "б", "в",
    "б", "в", "б", "г", "б", "г", "в", "а", "д", "а",
    "г", "д", "а", "б", "в", "б", "г", "б", "д", "б",
    "г", "б", "в", "в", "а", "б", "в", "д", "г", "д"
]

correct_answers_count = 0
total_questions = 60  
for i in range(total_questions):
    user_answer = input(f"Enter the answer for question {i+1}: ").strip().lower()  
    
    if user_answer == correct_answers[i]:
        correct_answers_count += 1 

print(f"You got {correct_answers_count} correct answers out of {total_questions}.")
