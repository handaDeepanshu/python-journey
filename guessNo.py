import random
rNo = random.randint(1,10)
attempts = 0
while True:
    userNo = int(input("Enter No: "))
    attempts += 1
    if rNo == userNo:
        print(f"Correct! You did it in {attempts} attempt(s)")
        break
    elif rNo > userNo:
        print("Small")
    else:
        print("Large")