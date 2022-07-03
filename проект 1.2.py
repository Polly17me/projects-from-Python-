import random

print('Добро пожаловать в числовую угадайку')

def is_valid(vvd):
    if vvd.isdigit() and 1<=int(vvd)<=100:
        return True
    else:
        return False
    
def game_continuation(): #конец игры или продолжение
    print("Спасибо, что играли в числовую угадайку. Хотите еще?")
    answ = input()
    if answ == 'да':
        print('Ура! Играем еще!')
        game_guessing()
    elif answ!='да':
        print("Спасибо, что играли в числовую угадайку.")
            

def game_guessing(): #основная игра
    print('Давай играть!')
    print('Введите верхнюю границу')
    highest = int(input())
    slnum = random.randint(1, highest) #случайное число
    while True:
        print("Введите число от 1 до", highest)
        vvd = input() #число,введенное пользователем
        if not is_valid(vvd):
            print("Данные некорректны. Попробуйте снова")
            continue
        vvd = int(vvd)
        if vvd == slnum:
            print("Вы угадали, поздравляем!")
            game_continuation()
            break
        elif vvd>slnum:
            print("Ваше число больше загаданного, попробуйте еще")
        else:
            print("Ваше число меньше загаданного, попробуйте еще")
            
            
#slnum = random.randint(1, highest+1) #случайное число            
game_guessing()


