import random
mydict={1:'ROCK',2:'PAPER',3:'SCISSORS'}
ans='Y'
print('YOU CAN CHOOSE :')
print("1. ROCK","2. PAPER","3. SCISSORS",sep="\n")
while ans=='y' or ans=='Y':
    user_choice=int(input("ENTER YOUR CHOICE :"))
    print(f'YOU CHOSE {mydict.get(user_choice)}')
    print('ITS COMPUTERS TURN NOW')
    comp_choice=random.randint(1,3)
    print(f'COMPUTER CHOSE {mydict.get(comp_choice)}')
    print(f'ITS {mydict.get(user_choice)} VS {mydict.get(comp_choice)} ')
    if user_choice==comp_choice:
        print("ITS A DRAW IN THIS TURN")
        continue
    elif (user_choice==1 and comp_choice==2) or (user_choice==2 and comp_choice==1):
        print(f'PAPER WINS')
        res=2
    elif (user_choice==2 and comp_choice==3) or (user_choice==3 and comp_choice==2):
        print(f"SCISSORS WIN")
        res=3
    else:
        print(f'ROCK WINS')
        res=1
    if user_choice==res:
        print("USER WON")
    else :
        print("COMPUTER WON")
    ans=input("DO YOU WANT TO PLAY AGAIN??")
    if ans=='n' or ans=='N':
        print("THANKS FOR PLAYING")
        break




