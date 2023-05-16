print("Welcome to QuikyQuiz!!!")
# import emoji
count=0
playing=input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay!!!, let's play :) ")
# print("\U0001F600")
print("hi my name is qickoo","\N{grinning face}")

sat=input("Here comes the first question!press Enter key , \U0001F44D " )
Answer=input("1.What country has the highest life expectancy? \n(a)Hong Kong \n(b)Srilanka \n(c)India \n(d)China \nEnter your answer option ")
if Answer.lower() == "a":
    print("correct!!  ,\U0001F917 ")
    count=count+1
else:
    print("incorrect!! ,\U0001F61F ")

sat=input("Here comes the Second question!press Enter key , \U0001F44D " )
Answer=input("2.How many minutes are in a full week? \n(a)11,080 \n(b)12,080 \n(c) 10,080 \n(d)9080 \nEnter your answer option ")
if Answer.lower() == "c":
    print("correct!! ,\U0001F917 ")
    count=count+1
else:
    print("incorrect!! ,\U0001F61F ")

sat=input("Here comes the third question!press Enter key , \U0001F44D " )
Answer=input("3.How many elements are in the periodic table? \n(a)111 \n(b)119 \n(c)108 \n(d)118 \nEnter your answer option ")
if Answer.lower() == "d":
    print("correct!!  ,\U0001F917 ")
    count=count+1
else:
    print("incorrect!! ,\U0001F61F ")

sat=input("Here comes the fourth question!press Enter key , \U0001F44D " )
Answer=input("4.Which planet has the most moons? \n(a)Earth \n(b)Saturn \n(c)Mars \n(d)Jupiter \nEnter your answer option ")
if Answer.lower() == "b":
    print("correct!!  ,\U0001F917 ")
    count=count+1
else:
    print("incorrect!! ,\U0001F61F ")

sat=input("Here comes the fifth question!press Enter key , \U0001F44D " )
Answer=input("5.How many bones do we have in an ear?  \n(a)1 \n(b)4 \n(c)3 \n(d)2 \nEnter your answer option ")
if Answer.lower()== "c":
    print("correct!! ,\U0001F917 ")
    count=count+1 
else:
    print("incorrect!! ,\U0001F61F ")

result=input("\U0001F9D0,Want to know your score?? ")
if result.lower()=="yes":
    if count<2:
        print("you lost !! try again,\U0001F643")
    elif count==5:
        print("\U0001F389,congratulations, you Won!!!!,\U0001F3C6")
    else:
        print("Good score!!! keep it up,\U0001F607 ")
print(f"You scored {count} out of 5")
print("you got"+str((count/5)*100)+"%!!")
