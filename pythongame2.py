import random
lst=["snake","water","gun"]
print("Welcome to game;-",lst)
userc=0
compc=0
i=1
for i in range(10):
    choice=random.choice(lst)
    user= input("player select any one form gun,snake,water:-")
    print(f"choice by computer:-",{choice})
    if(user==choice):
            print("draw")
    if (user=="snake" and choice=="water"):
        
        print(" snake vs water:- brave user won")
        userc=userc+1
    elif(user=="snake"and choice=="gun"):
         print(" snake vs gun:- computer won")
         compc+=1
        
    elif(user=="water"and choice=="snake"):
         print(" water vs snake:- computer won")
         compc+=1
         
    elif(user=="water"and choice=="gun"):
         print(" water vs gun :- user won")
         userc=userc+1
    elif(user=="gun" and choice=="snake"):
         print(" gun vs snake:- user won")
         userc=userc+1
         
    elif(user=="gun"and choice=="water"):
         print(" gun vs water:-computer won")
         compc+=1
     
    else:
        print("nobody wins")

print(compc,userc)

if (compc==userc):
    print("equal no one wins")
elif(compc>userc):
    print("computer won and get", +compc)
elif(userc>compc):
    print("user won and get",+userc)
else:
    print("no one wins")
        
         

 
