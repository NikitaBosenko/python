
import time

divider = "-------------------------------------------------------------"
# quiz questions dictionary
questions = [
("What is the capital of Australia?", ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"], "C"),
("Which element has the chemical symbol 'O'?", ["A. Oxygen", "B. Gold", "C. Iron", "D. Silver"], "A"),
("Which planet is known as the Red Planet?", ["A. Mars","B. Venus","C. Jupiter","D. Saturn"], "A"),
("In what year did World War II end?", ["A. 1943", "B. 1945", "C. 1950", "D. 1939"], "B"),
("What is the largest mammal on land?", ["A. Elephant", "B. Giraffe", "C. Rhinoceros", "D. Hippopotamus"], "A"),
("Which planet is known as the 'Red Planet'?", ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"], "A"),
("What is the square root of 64?", ["A. 6", "B. 7", "C. 8", "D. 9"], "C"),
("Who painted the Mona Lisa?", ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"], "C"),
("Which country is known as the 'Land of the Rising Sun'?", ["A. China", "B. Japan", "C. South Korea", "D. Thailand"], "B"),
("What is the currency of Brazil?", ["A. Peso", "B. Euro", "C. Real", "D. Dollar"], "C"),
("How many continents are there?", ["A. 5", "B. 6", "C. 7", "D. 8"], "C"),
("What is the largest ocean?", ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"], "C"),
("Who is known as the 'Father of Computer Science'?", ["A. Bill Gates", "B. Alan Turing", "C. Steve Jobs", "D. Mark Zuckerberg"], "B"),
("Which planet is known as the 'Morning Star' or 'Evening Star'?", ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],"B"),
("What is the speed of light?", ["A. 299,792 km/s", "B. 150,000 km/s", "C. 500,000 km/s", "D. 1,000,000 km/s"], "A"),
("Who wrote 'Romeo and Juliet'?", ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"], "B"),
("What is the largest planet in our solar system?", ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "C"),
("Who discovered penicillin?", ["A. Marie Curie", "B. Alexander Fleming", "C. Louis Pasteur", "D. Isaac Newton"], "B"),
("Which animal is known as the 'King of the Jungle'?", ["A. Tiger", "B. Elephant", "C. Lion", "D. Gorilla"], "C"),
("What is the chemical symbol for gold?", ["A. Au","B. Ag","C. Fe","D. Hg"],"A"),
]

# function to show and count each question
def quiz():
    time_str = time.time()
    print(question)
    for option in options:
        print(option)

    score = 0
    answer = input("\nEnter your answer A,B,C or D: ").upper()
    time_stp = time.time()
    time_fin = round(time_stp - time_str)
    if answer == correct_letter:
        print(f"> Correct! ({time_fin} sec spent)")
        print(divider)
        score += 1
        return score
    else: 
        print(f"> Wrong! ({time_fin} sec spent)")
        print(divider)
        return 0
    
# count questions and grade mark
total_ques = len(questions)
great = (total_ques/100) * 80
good = (total_ques/100) * 60

# define total time for quiz
time_1question = 10

time_quest = total_ques * time_1question

# print header and instructions
print("\nWelcome to QUIZ")
print(f"You have to answer {total_ques} questions.")
print(f"Total time for the quiz {time_quest} sec.\n")
print(f"Average time for 1 answer {time_1question} sec!")

start = input("Press 'enter' to Start: ")
print(divider)
# define score counter and quiz start time
score = 0
start_time = time.time()

# difine values in questions dictionary and run quiz
for question, options, correct_letter in questions:
    score += quiz()

# define end time and calculate total time spent for quiz
end_time = time.time()
total_time = round(end_time - start_time, 3)

# if spent total time less or equal to the time given for quiz then define grade
if total_time <= time_quest:
    if score >= great:
        mark = "Great Work!"
    elif score >= good: 
        mark = "Good try!"
    else:
        mark = "Poor finishing!"

    print(f"> You've done {mark}")
# if spent time more then print the user lost quiz
else:
    print("\n> You've lost!\n> The time is over!")
 

print(f"Total time taken: {total_time} seconds")  
print(f"Correct answers: {score} from {total_ques}.")
print(divider)