import random
wrong = 0
right = 0
y = random.randrange(100)
while right<1:
    x = int(input('guess num: '))
    while x!= y:
        if x>y:
                wrong += 1
                print("guess wrong,","It's too much,","worng :",wrong)
                break
        else :
                wrong += 1
                print("guess wrong,","It's less than num,","worng :",wrong)
                break
    if x==y:
        right += 1
        print("You are Correct!!,","wrong :",wrong)
