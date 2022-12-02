my_list=[]
while True:

        if len(my_list) < 1:
            print("welcome lets play a game!")
            name=str(input("whats your name?"))
            my_list.append(name)
            continue
        if len(my_list) < 2 :
            Age=input("How old are you?")
            my_list.append(Age)
            continue
        elif len(my_list) < 3:
            food=input("whats your favorite food?")
            my_list.append(food)
            continue
        else:
            print(f"Your name is {name}, age {Age} and your favorite food is {food}. ") 
               
            break