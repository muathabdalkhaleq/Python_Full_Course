# Python quiz game

questions = ("1. What is the capital of France?",
             "2. Which planet is known as the Red Planet?",
             "3. Who wrote 'Romeo and Juliet'?",
             "4. What is the largest ocean on Earth?",
             "5. How many days are in a leap year?")

options = (("A. London", "B. Paris", "C. Rome", "D. Berlin"),
           ("A. Earth", "B. Venus", "C. Mars", "D. Jupiter"),
           ("A. Shakespeare", "B. Dickens", "C. Orwell", "D. Twain"),
           ("A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"),
           ("A. 364", "B. 365", "C. 366", "D. 367"))

answers = ("B", "C", "A", "D", "C")
guesses = []
score = 0
quastion_num = 0

for qustion in questions:
    print("----------------------")
    print(qustion)
    for option in options[quastion_num]:
        print(option)
    
    guess = input("Enter (A,B,C,D)").upper()
    guesses.append(guess)
    if guess == answers[quastion_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[quastion_num]}  is the correct answer")
        print()
        print()
    quastion_num+=1
    
print("-------------------------------")
print("            RESULTS            ")
print("-------------------------------")

print("answers :", end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses :", end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")