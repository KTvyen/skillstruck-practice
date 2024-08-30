#funtion parameters are where you go inside of the funtions paratheses ex: def mylist(type)

#def weather(forecast):
    #print("its a soggy day outside becasue it is " + #forecast)

#weather("raining")

#output = its a soggy day outside because it is raining 
#the function that takes the string and puts it inside the string using concatenation. the vaule of "raining" in the ex is the duntion's argument 

#def weather(forecast):
    #print("It's a soggy day outside becasue it is " + #forecast)

#weather("raining")
#weather("snowing")
#weather("drizzling")

#output prints the same sentence with different forecast 

#It's a soggy day outside becasue it is raining
#It's a soggy day outside becasue it is snowing
#It's a soggy day outside becasue it is drizzling

#def customer(order):
    #print("I would to order a " + order) 
    #print("Today I will have a " + order)

#customer("tart")
#customer("bread")
#customer("sandwich")

#fruit = input("Please enter the name of a fruit: ")

#def hungryForApples(choice):
    #print(choice + choice  + choice )
	
#hungryForApples(fruit)


#month = int(input("name a number 1 - 12"))

#def information(choice):
    #if choice == 4 or choice == 6 or choice == 9 or #choice == 11:
       # print(30)
    #elif choice == 2:
        #print(28)
    #else:
        #print(31)

#information(month)

#def odd_even(num):
	#if num % 2 == 0 :
		#print("even")
	#else:
		#print("odd")

#odd_even(2)
#odd_even(5)
#odd_even(8)


#choice = int(input("Enter a year"))

#def leap_year(leap):
    #if (leap % 4 == 0 and leap % 100 != 0) or (leap % 400 == 0):
        #print("Leap year!")
    #else:
        #print("Not a leap year.")

#leap_year(choice)

#answer = int(input("What is the radius of the circle?"))

#def circle (radius) :
	#answer = 3.14159 * radius * radius
	#print(round(answer, 1))
	

#circle(answer)

thing=input('Input a snack or activity to see if it is allowed at the party.')

my_thing= list(thing)
def allowed(thing):
	if my_thing[0]=='c' or my_thing[0]=='C':
		print('{} can be a part of the party!'.format(thing))
		
	elif my_thing[0]!='c'or my_thing[0]!='C':
		print("Sorry! {} doesn't start with the letter c!".format(thing))
		
		
allowed(thing)