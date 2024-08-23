#if statements = a condition if something is met then somethting else will happen
#what is a qualifies as a condition? checking to see what kind of value a piece of data has. (x==10) or (x>=15) or (x == "toad")
#After the condition, there is a new line of code that is indented, indicating that this is the code to be executed if the condition is met.
#comparison operator = the character that compares two things = >< 
#Greater than: > 
#Greater than or equal to: >=
#Less than: <
#Less than or equal to: <=
#Equal to ==

pasteries_bought = input("How many pasteries did you want to buy? ")
pasteries_eaten = input("what many pasteries did you eat? ")

if int(pasteries_eaten) < int(pasteries_bought):
    print("Woah really?")
    print("what kind did you eat? ")
    input("types of pasteries eaten: ")
    print("woah I'm jealous")
else: 
    print("Where did the other pasteries comes form?")
    print("hold on did you eat the others and went back to buy more?!")
    print(" how could you only get me " + pasteries_bought + "!")


#janet_age = 16
#eva_age = 6
#if eva_age == janet_age:
    #print("Eva and Janet are the same age.")
#else:
    #print("they are different ages")


#mood = "chill" 
#if mood == "chill":
    #print("You are feeling chill.")
#else:
    #print("You are not feeling chill.")

#friend_pet = "poodle"
#your_pet = "fish"
#if friend_pet != your_pet:
    #print("You and your friend have the same kind of pet!")
#else: 
    #print("You and your friend have different kind of pets.")

#baked_goods = 40 
#other_stuff = 10

#if baked_goods < 2 or other_stuff > 5: 
    #print("you didn't make enough")
#else:
    #print("Thats great! You made extra!")

#age = input("How old are you? ")
#license = True
#if int(age) >= 16 and license == True: 
    #print("You are old enough to drive.")
#else:
    #print("You are not able to drive.")

#dogs = 5
#if dogs > 5:
    #print("You have a lot of dogs")
#else:
    #print("You have a few dogs")

#price = 10
#your_cash = 10

#if your_cash > price:
    #print("You have MORE than enough money to buy it.")
#elif your_cash == price:
    #print("You have exactly enough money to buy it.")
#else:
    #print("You do not have enough to but it.")

#coins = 10
#if coins > 20:
    #print("You have more than enough to buy a puppy")
#elif coins == 20:
   # print("You have exactly enough to buy a puppy")
#else:
   # print("You do not have enough to buy a puppy")