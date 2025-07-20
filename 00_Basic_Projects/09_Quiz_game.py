#Quiz game using python

questions = ["What is the capital of India?", 
             "Which language is primarily used for data science?",
             "Who is known as the Father of Computers?",
             "What does CPU stand for?",
             "Which planet is known as the Red Planet?",
             "What is not object?: "]

options = (("a) Mumbai", "b) Delhi", "c) Kolkata", "d) Bengaluru"),
           ("a) Java", "b) C++", "c) Python", "d) HTML"),
           ("a) Alan Turing", "b) Charles Babbage", "c) Dennis Ritchie", "d) Bill Gates"),
           ("a) Central Process Unit", "b) Computer Personal Unit", "c) Central Processing Unit", "d) Control Processing Unit"),
           ("a) Mars", "b) Venus", "c) Saturn", "d) Jupiter"),
           ("a) pen", "b) Pencil", "c) Human", "d) Mobile"))

answers = ["b", "c", "b", "c", "a", "c"]
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter the Answer(a, b, c, d): ").lower() 
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is correct answer!!")
    
    question_num += 1

print("Correct Answers are: ")
for answer in answers:
    print(answer, end=" " )

print()

print("Correct Guesses are: ")
for guess in guesses:
    print(guess, end=" ")

print()

print(f"Your final score is {score}/{question_num}.")




    

        
