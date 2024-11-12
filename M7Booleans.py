#Sebastian Cervantes 
#November 12, 2024 
#Write a function 
import resources
def func_name(num):
    print (f"{resources.Sebas.weapons}")

    if num == 1: 
        #for every item on the list that i need, i want to see if it it in my weapons 
        
        for item in ["rope", "coat", "first aid kit"]:
            if item not in resources.Sebas.weapons:
                print(f"{item} is missing")
                return False 
        print ("you have everything you need, goodluck!")
        return True 

    elif num == 2: 
        for item in ["pan", "groceries"]:
            if item not in resources.Sebas.weapons:
                print(f"{item} is missing")
                return False 
        print ("you have everything you need, goodluck!")
        return True 
       

    elif num == 3:
        for item in ["pen", "paper", "idea"]:
            if item not in resources.Sebas.weapons:
                print(f"{item} is missing")
                return False 
        print ("you have everything you need, goodluck!")
        return True 


func_name (2)


#that checks whether your game character has picked up all the items needed to perform certain tasks and checks against any weaknesses. Confirm checks with print statements. The function will take a number in as an argument. You can match the number to the task below. You don’t have to plan for inputs outside of [1,2,3].

# how do I look in my characters weapons to see if they have everything they need