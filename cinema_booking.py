#ticket booking system
films = {
    "Finding Dory": [3,5],
    "End Game": [18,1],
    "Bad Boys": [18,5],
    "Birds Of Prey" : [15,8]
    }

while True:
    choice = input("Which film you want to watch?: ").strip().title()

    
    #check the film

    
    if choice in films:

        #check the tickets

        
        if films[choice][1] > 0:
            age = int(input("How old are you?:").strip())

            #check age
            
            if age >= films[choice][0]:
                print("Enjoy the movie!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("You are too young to watch this movie")
        else:
            print("Sorry! we are sold out!")
        
    else:
        print("This movie is not available here")
            
            
