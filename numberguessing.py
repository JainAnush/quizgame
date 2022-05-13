import random
secret_number=random.randint(1,100)
number=int(input('guess the number between 1-100/ enter any negative value to quit :'))
while number>0:
    if number==secret_number:
        print('well done ! you guessed it right')
        break
    elif number>secret_number:
        print('number too large try again')
        number=int(input())
    else:
        print('number too small try a greater number')
        number=int(input())
else:
    print('thanks for playing !!!')

