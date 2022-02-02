import random
from time import time as t

try:
    correct = 0
    times = int(input('How many questions you want:'))
    how_num = int(input('How the numbers can go?:'))
    answer_list = []
    start = t()
    for i in range(int(times)):
        x = random.randint(1, how_num)
        y = random.randint(1, how_num)
        math_q = x * y
        user_an = input(f"How much is: {x} times {y}:  ")
        answer_list.append(f"How much is: {x} times {y}: your:{user_an} ")
        if (int(user_an) == math_q):
            correct += 1
        end = t()
except ValueError as err:
    print(f'{err} is Bad Value')

else:
    wrong = times - correct
    porcent_correct = (correct*100)/int(times)
    print(
        f'You aswered {correct} correct and make {wrong} mistakesin {round(end-start,1)} seconds ({round((end-start)/times,1)}seconds/question')
    print(f'You porcent was {porcent_correct}%')
    for a in answer_list:
        print(a)

finally:
    print('Thanks for playing')
