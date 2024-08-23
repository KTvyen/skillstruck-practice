#student_ages = [14, 17, 12, 14, 15, 18, 19, 10]

#for x in student_ages: 
    #if x >= 16: 
        #print( str(x) + " This student is old enough to drve.") 
    #else: 
        #print( str(x) + " This student is not old enought to drive.")

#smells = ["skunk", "lilies", "roses", "rain", "garbage", "cleaner", "cookies"] 
#for x in range(5):
    #print(smells[2:5])

#my_list = [2, 5, 8, 10]
#total = 0
#for x in my_list:
    #total = total + x
    #print(total)

#my_list = input().split()
#print(my_list)

#my_list = [int(n) for n in input("Input list of numbers").split()] 
#print(my_list)


#foods = ["mushrooms", "broccoli", "fish"]
#for x in foods: 
    #if x == "mushrooms":
        #print(x + "are gross.")
    #elif x == "broccoli":
        #print( x + " is gross.")
    #elif x == "fish":
        #print(x + " is gross.")

print("Welcome to programmer's coffe shop. Here is our menu")
#will print additonal information about actions of barista and customer 
print("""- barista hands over menu - 
- you grab it and see ~ -""") 
menu = ["black coffee", "cappacino", "latte", "frappacino"] 
print(menu) 

print("- barista ask for your name - ")
c_name = input("What is your name?") 

order = input("What would you like to order " + c_name + "? ") 

if order == menu[0]: 
    print("That will be 5$")
elif order == menu[1] or menu[2]:
    print("That will be 6$")
elif order == menu[3]:
    print("That will be 8$")
elif not order == menu[0] or menu[1] or menu[2] or menu[3]:
    print("We don't serve that here")