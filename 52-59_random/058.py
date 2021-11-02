import random

score = 0
for question in range(5):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2

    uanswer = int(input(f"{num1} + {num2} = "))
    
    if uanswer == correct_answer:
        score += 1

print(f"You got {score} out of 5 correct")