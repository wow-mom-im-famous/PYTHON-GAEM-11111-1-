import random
print("PYTHON NUMBER GUESSING GAME!!!11!1!1111")
print("\n")
print("Please select your level : \n")
print("Level 1 : Easy >:)) \n")
print("Level 2 : Medium -_- \n")
print("Level 3 : Harddd :0  \n")
i=int(input("Select ur level : "))
sucess=0
while True:
    if i==1:
        break
    elif i==2:
        break
    elif i==3:
        break
    else:
        print("Sybau u gooner 🥀 \n")
        print("Try again >:(")
        i=int(input("Select ur level : "))
if i==1:
    print("Guess a number from 1 to 10 gng D: ")
    num=random.randrange(1,10,1)
    for i in range(0,5):
        guess = int(input("Give me ur guess G : "))
        if guess==num:
                    print("Yayyyy u got itttt :D :D, it was ",num," !!!1111111!!!11!!1")
                    sucess=1
                    break
        else:
            print("Oh hell nah u gooner 🥀")
            if guess>num:
                print("It is lower gng 😭🙏 \n")
            else:
                print("It is higher gng 😭🙏\n")
    if sucess==0:
        print("Aw hell nah u fatass chud the number was : ",num)
elif i==2:
    print("Guess a number from 1 to 100 gng D: ")
    num=random.randrange(1,100,1)
    for i in range(0,10):
        guess = int(input("Give me ur guess G : "))
        if guess==num:
                    print("Yayyyy u got itttt :D :D, it was ",num," !!!1111111!!!11!!1")
                    sucess=1
                    break
        else:
            print("Oh hell nah u gooner 🥀")
            if guess>num:
                print("It is lower gng 😭🙏 \n")
            else:
                print("It is higher gng 😭🙏 \n")
    if sucess==0:
        print("Aw hell nah u fatass chud the number was : ",num)
elif i==3:
    print("Guess a number from 1 to 1000 gng D: ")
    num=random.randrange(1,1000,1)
    for i in range(0,15):
        guess = int(input("Give me ur guess G : "))
        if guess==num:
                    print("Yayyyy u got itttt :D :D, it was ",num," !!!1111111!!!11!!1")
                    sucess=1
                    break
        else:
            print("Oh hell nah u gooner 🥀")
            if guess>num:
                print("It is lower gng 😭🙏 \n")
            else:
                print("It is higher gng 😭🙏 \n")
    if sucess==0:
        print("Aw hell nah u fatass chud the number was : ",num)
