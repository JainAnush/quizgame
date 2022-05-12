def startquiz():
    score=0
    for ques, options in questions.items():
        print(f"QUESTION : {ques}")
        for i in range(4):
            print(i + 1, '.', options[i], sep='')
        selectedoption=input("ENTER YOUR CHOICE :")
        while selectedoption not in ['1','2','3','4']:
            selectedoption=input("PLEASE SELECT A VALID OPTION NUMBER :")
        if int(selectedoption)==options[4]:
            score+=4
        print("-----------------------------------------------------")
    return score
questions={'who developed python?':['Wick van Rossum','Rasmus Lerdorf','Guido van Rossum','Niene Stom',3],
           'Which type of Programming does Python support?':['object-oriented programming','structured programming','functional programming','all of the mentioned',4],
           'Is Python case sensitive when dealing with identifiers?':['no','yes','machine dependent','none',2],
           'Which of the following is the correct extension of the Python file?':['.python','.py','.pl','.p',2],
           'Is Python code compiled or interpreted?':['Is Python code compiled or interpreted?','Python code is neither compiled nor interpreted','Python code is only compiled','Python code is only interpreted',1]}
totalmarks=len(questions)*4
print('CHOOSE AN OPTION ','1.ATTEMPT QUIZ','2.EXIT')
choice=input()
while choice not in ['1','2']:
    print('PLEASE CHOOSE A VALID OPTION ', '1.ATTEMPT QUIZ', '2.EXIT')
    choice=input()
if choice=='1':
    score=startquiz()
    print(f'THANKS FOR ATTEMPTING THE QUIZ YOUR SCORE IS {int(score/totalmarks*100)}%')
elif choice=='2':
    print(f'THANKS YOUR SCORE IS 0')
else:
    print(f'PLEASE ENTER A VALID CHOICE')


