#number1 = int(input("choose a number between 1 and 8 "))
#number2 = int(input("Choose a number between 1 and 8 "))
#if (number1 + number2) % 2 == 0:
    #print("No")
#else:
    #print("Yes")



#number1 = int(input("first number"))
#number2 = int(input("second number"))
#if number1 > number2:
    #print("The first number is larger.")
#elif number2 > number1: 
    #print("The second number is larger.")
#else: 
    #print("The numbers are the same.")


#number1 = int(input("first number"))
#number2 = int(input("second number"))
#number3 = int(input("third number"))

#if number1 < number2 and number1 < number3:
    #print(number1)
#elif number2 < number3 and number2 < number1:
    #print(number2)
#else:
   #print(number3)

#number1 = int(input("first number"))
#number2 = int(input("second number"))
#number3 = int(input("third number"))
#if number1 == number2 == number3:
    #print(3)
#elif number1 == number2 or number1 == number3 or number2 == number3:
    #print(2)
#else:
   #print(0)

#print("""You are walking alone in the woods on a narrow pathway. It's a warm summer evening and the sun is just going down. Tall trees cast dark shadows on the path that get darker with the setting sun.

#You come up to a fork in the path that has three choices.The right path leads downhill and the path gets darker with more bushes on each side. The center path has some sort of rustling sound you can hear faintly. The left path has the outline of some sort of building that you can see through the trees. Which path do you take? """)

#print("answers should be written as left, right, or center in lowercase")
#choice = input("Which direction do you want to go.")

#if choice == "left":
    #print("Walking down the left path you notice a builing. Upon walking towards it you hear someone scream. So you run away and hide in a bush and see a girl running from a zombie.")
#elif choice == "center":
    #print("Walking down the center path you notice the rustling sound get louder. So as you approach carefully yout realize it was just a cute cat.")
#elif choice == "right":
    #print("Walking down the right path you notice that the sun is almost covered by the trees and bushes.Upon walking further into the woods you meet someone suspicous who tells you to get out of here in a desperate voice. You ignore them and continue. You die..." )
#else:
   #print("You decide not to continue into the woods and return home")
#print("two inputs have to be the same number")
#number1 = int(input("first number"))
#number2 = int(input("second number"))
#number3 = int(input("third number"))

#if number1 == number2 and number1 != number3:
    #print(3)
#elif number2 == number3 and number2 != number1:
    #print(1)
#elif number3 == number1 and number3 != number2:
    #print(2)

#number1 = int(input("Enter the first number: "))
#number2 = int(input("Enter the second number: "))
#number3 = int(input("Enter the third number: "))

#if number1 < number2 and number1 < number3:
    #first = number1
#elif number2 < number1 and number2 < number3:
    #first = number2
#elif number3 < number1 and number3 < number2: 
    #first = number3

#if number1 > number2 and number1 > number3:
    #third = number1 
#elif number2 > number1 and number2 > number3:
    #third = number2
#elif number3 > number1 and number3 > number2:
    #third = number3

#if number1 < number2 or number1 < number3 and number1 > number2 or number1 > number3:
    #second = number1
#elif number2 < number1 or number2 < number3 and number2 > number1 or number2 > number3:
    #second = number2
#elif number3 < number1 or number3 < number2 and number3 > number1 and number3 > number2:
    #second = number3

#if number1 <= number2 and number1 <= number3:
    #first = number1
    #if number2 <= number3:
        #second = number2
        #third = number3
    #else:
        #second = number3
        #third = number2
#elif number2 <= number1 and number2 <= number3:
    #first = number2
    #if number1 <= number3:
        #second = number1
        #third = number3
    #else:
        #second = number3
        #third = number1
#else:
    #first = number3
    #if number1 <= number2:
        #second = number1
        #third = number2
    #else:
        #second = number2
        #third = number1

#print(str(first) + " " + str(second) + " " + str(third))

#number = int(input("Choose a number between 1 and 12 "))
#if number == 1 or number == 3 or number == 5 or number == 7 or number == 8 or number == 10 or number == 12:
    #print("31")
#elif number == 2:
    #print("28")
#else:
    #print("30")

#x1= int(input("choose a number between 1 and 8 "))
#y1 = int(input("choose another number between 1 and 8 "))
#x2 = int(input("choose another number between 1 and 8 "))
#y2 = int(input("choose another number between 1 and 8 "))

#cordinate1 = x1 + y1
#cordinate2 = x2 + y2 

#if (cordinate1 % 2 == cordinate2 % 2):
    #print("Yes")
#else: 
    #print("No")

#year = int(input("random year"))
#if year % 4 == 0:
    #year = "Leap"
#else:
    #year = "Common"

#print(year)

#var1 = int(input("random number"))
#var2 = int(input("random number"))

#for x in range(var1, var2+1):
    #print(x)

#f_number = int(input("random number"))
#_number = int(input("random number"))
#var = 0 
#for x in range(f_number, s_number):
    #var = var + x
#print(var)

#number = int(input("random number "))
#for x in range(1, number):
    #number = x * number 
#print(number)

#my_list = [int(n) for n in input("Input a list of numbers").split()] 
#total = 0

#for x in my_list:
	#total = x + total

#average = total/len(my_list)

#for y in my_list:
	#if y > average:
		#print(y)


#choice = input("Choose a letter")

#my_list = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "gray", "pink", "indigo", "brown", "tan", "gold", "silver"]

#total = 0

#for x in my_list:
	#if choice in x:
		#total += 1

#print("There are {} items in the list that have the letter {} in it.".format(total,choice))

#numbers = [int(n) for n in input("list of 9 numbers: ").split()]
##print(answer)

#my_list = input().split()

#print("Some animals " + my_list[0] + " and some " + my_list[-1])

#my_list = [int(n) for n in input("Create a list of 6 numbers").split()]

#print( my_list[0] + my_list[1] + my_list[4] + my_list[5])

#my_list = [int(n) for n in input("Input a list of numbers").split()]
	
#for x in my_list:
	#missing = x + 1
	#if missing not in my_list:
		#print(missing)


#choice = input("Choose a letter")
	
#boat = "On our boat cruise we saw crocodiles, flamingos, turtles, fish, and even a manatee!"

#if choice in boat:
	#words = boat.split(choice)
	#print(words)
#else:
	#print("The letter " + choice + " is not in the string")

#smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies", "roses", "new car", "sweaty feet", "peach"]
#print(smells[0:8:2])

#for x in range(0,20,3):
   # print(x)

#my_list = [int(n) for n in input("list of 4 numbers").split()]
#total = 1

#for x in my_list:
	#total = x * total
#print(total)

#my_list = ["James", 10, "blue", "Zoe", 8, "red", "Dan", 12, "pink", "Shana", 11, "orange", "Sebastian", 9, "yellow", "Cynthia", 13, "green"]

#choice = (input("what do you want to know?").lower())


#if choice == "name":
    #name = my_list[0::3]
    #print(name)
#elif choice == "age":
    #age = my_list[1::3]
    #print(age)
#elif choice == "color" or "favorite color":
    #color = my_list[2::3]
    #print(color)
#else:
    #print("Invalid Input")

#options = [.20, .30, .40, .50, .60, .70]
#choice = int(input("Which number will you pick? 0-5 ")) 
#scratch_off = options[choice]
#price = 29.95
#discount = price * options[choice] 
#total = price - discount
#people = int(input("How many people? "))
#per_person = total/people
#print(round(per_person,2))

goats = ["Billy", "Frannie", "Leslie", "Barbara", "Scott"]
goats.append("Molly")
print(goats)