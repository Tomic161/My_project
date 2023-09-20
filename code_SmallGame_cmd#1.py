import os
import random
import time

print ("\t Добро пожаловать в игру")
print ("\nPlay \n") 
print ("Exit")  
live = 3
restrictions = 10
beginning = 0
points = 1
answer = input("\n")
if answer.lower() == "play" :
    os.system('clear') 
    while live > 0:
        if points == 100:
            break         
        
        os.system('clear')
        
        if points % 5 == 0:
            restrictions += 10
            beginning += 10 
        
        num1 = random.randrange(beginning,restrictions)
        num2 = random.randrange(beginning,restrictions)
        meaning = random.randint(0,3)
       
        addition = num1 + num2
        Minus = num1 - num2
        multiplication = num1 * num2
        
        
        #print (restrictions) 
        print ("Ваши жизни:", live,"\tРекорд:",points ) 
        #+
        if meaning == 1:
            print(num1, "+", num2, "="  )
            end = int(input())
            if end == 000:
                os.system('clear') 
                print("Пока") 
                break 
            if addition == end:
                os.system('clear') 
                points += 1
                continue
            else:
                if addition != end:
                    print ('Неверно')
                    time.sleep(1) 
                    live -= 1
                    os.system('clear') 
                    continue
        #-            
        if meaning == 2:
            print(num1, "-", num2, "=" )
            end = int(input())
            if end == 000:
                os.system('clear') 
                print("Пока") 
                break
            if Minus == end:
                os.system('clear') 
                points += 1
                continue
            else:
                if Minus != end:
                    print ('Неверно')
                    time.sleep(1)
                    live -= 1
                    os.system('clear') 
                    continue 
        #*
        if meaning == 3:
            print(num1, "*", num2, "=" )
            end = int(input())
            if end == 000:
                os.system("clear") 
                print("Пока")
                break
            if multiplication == end:
                os.system('clear') 
                points += 1
                continue
            else:
                if multiplication != end:
                    print ('Неверно')
                    time.sleep(1)
                    live -= 1
                    os.system('clear') 
                    continue
        
else:
    os.system('clear')
    print("Пока!") 
if live == 0:
    print("Вы проиграли!""\tВаш рекорд:", points) 
if points == 100:
    print("Вы прошли игру!!!""\tДостиг:",points,"!!") 