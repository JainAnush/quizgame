import random
dest_x=random.randint(1,3)
dest_y=random.randint(1,3)
print('you have 5 chances to reach your destination which is at (%d,%d)'%(dest_x,dest_y))
print('you can take any direction right/left/up/down and any length as you wish')
print('your starting position is (0,0). best of luck')
user_x=0
user_y=0
for i in range(5):
    print('enter the direction or enter -1 to quit')
    print('1. RIGHT')
    print('2. LEFT')
    print('3. UP')
    print('4. DOWN')
    direction=int(input('ENTER THE DIRECTION :'))
    if direction==-1:
        print('thanks for playing!')
        break
    while direction not in [1,2,3,4]:
        direction=int(input('PLEASE CHOOSE CORRECT DIRECTION FROM THE OPTIONS :'))
    steps=int(input('ENTER THE LENGTH YOU WANT TO COVER IN THIS DIRECTION :'))
    if direction==1 or direction==2:
        if direction==1:
            user_x+=steps
        else:
            user_x-=steps
    else:
        if direction==3:
            user_y+=steps
        else:
            user_y-=steps
    #print('so far you have reached (%d,%d)'%(user_x,user_y))
    if dest_x==user_x and dest_y==user_y:
        print('congrats you reached the destination')
        break
else:
    print('sorry you did not reach your destination within 5 tries')