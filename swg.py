import random

u = c = t = 0

while(True):
    user = input("enter s for snake , w for water , g for gun, q to quit : ")
    computer = random.choice(['s','w','g'])
    if user == 'q':
        break
    elif user == computer:
        print('it is a tie')
        t += 1
    elif user == 's':
        if computer == 'w':
            print('you won...')
            u += 1
        else:
            print("computer won...")
            c +=1 
    elif user == 'w':
        if computer == 's':
            print("computer won...")
            c += 1
        else:
            print('you won....')
            u += 1
    elif user == 'g':
        if computer == 'w':
            print('computer won...')
            c += 1
        else:
            print('you won...')
            u += 1
            
print(f'you played total {u+t+c} times in which you won {u} times computer won {c} times and it was tie {t} times')
print('you won overall game') if u > c else print('computer won overall game')
    


