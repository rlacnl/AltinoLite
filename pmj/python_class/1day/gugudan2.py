import random
from datetime import datetime
import time

a = 1

while (a <= 5) :
    print("구구단을 외자!")

    fristNum = random.randint(1, 9)
    nextNum = random.randint(1, 9)

    start_time = datetime.now 

    print(str(fristNum) + " * " + str(nextNum) + " = ?")

    

    user_Num = int(input("답 >> "))
    result = fristNum * nextNum

    if result == user_Num :
        print("정답입니다 !!")
    else :
        print("틀렸습니다 ㅠㅠ")
        a = 100

a+=1