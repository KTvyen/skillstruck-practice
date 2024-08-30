#def gifts(first, second):
    #print("Your first choice for a birthday gift would be " + first)
    #print("Your second choice for a brithday gift would be " + second) 

#gifts("bike", "basketball")
#gifts("speaker", "tickets")

#local variable , variable inside a funtion 
#only use inside the funtion 

#favorite = "Ilove juice"
# above is ^ a variable (global variable that can be used anywhere in the program 
#def myfuntion():
#     fruit = "apple"
         #^ above is local variable (can be used inside the funtion not anywhere else in the programm 
#calling the funtion # myfuntion()
#print(favorite)
# will print apple and than Ilove juice 


#def names(first, second):
    #print("Her name is " + first)
    #print("Her friend's name is " + second)

#names("Kaylee", "Sedona")
#names("Lily", "Shae")

#first challenage -->

#fruit1 = input("name a fruit ")
#fruit2 = input("name a fruit ")
#fruit3 = input("name a fruit ")

#def fruit(first, second, third):
    #print(first + second + third)


#fruit(fruit1, fruit2, fruit3) 

#num1 = int(input("Write a number"))
#num2 = int(input("Write another number"))

#def show(first, second):
    #if first > second:
        #print(second)
    #elif second > first:
        #print(first)
    #else:
        #print("equal")
    
#show(num1, num2)

#num1 = int(input("choose a number"))
#num2 = int(input("choose a number"))
#num3 = int(input("choose a number"))

#def same_dif(first, second, third):
    #if first == second == third:
        #print("3")
    #elif first == second or first == third or second == third:
        #print("2")
    #else:
        #print("0")

#same_dif(num1, num2, num3)



#def my_function(choice1, choice2, choice3, choice4, choice5):
	#smallest = choice1
	#if choice2 < smallest:
		#smallest = choice2

	#if choice3 < smallest:
		#smallest = choice3 

	#if choice4 < smallest:
		#smallest = choice4 

	#if choice5 < smallest:
		#smallest = choice5

	#print(smallest)
		
#my_function(first, second, third, fourth, fifth)

#print("two numbers must be the same and one must be different")
#num1 = int(input("choose a number"))
#num2 = int(input("choose a number"))
#num3 = int(input("choose a number"))

#def show(first, second, third):
    #if first == second and first != third:
        #print("3")
    #elif first != second and second == third:
        #print("1")
    #elif first == third and first != second:
        #print("2")
    #else:
        #print("equal")

#show(num1, num2, num3)

first = int(input("Which month? 1-12: "))
second = int(input("What date? 1-31: "))

def my_function(month, date):
    # Months with 30 days: April (4), June (6), September (9), November (11)
    if month in [4, 6, 9, 11]:
        if date == 30:
            next_month = month + 1
            next_day = 1
        else:
            next_month = month
            next_day = date + 1

    # February (2) with 28 days in 2021
    elif month == 2:
        if date == 28:
            next_month = month + 1
            next_day = 1
        else:
            next_month = month
            next_day = date + 1

    # Months with 31 days: January (1), March (3), May (5), July (7), August (8), October (10), December (12)
    else:
        if date == 31:
            if month == 12:  # Special case: December to January
                next_month = 1
                next_day = 1
            else:
                next_month = month + 1
                next_day = 1
        else:
            next_month = month
            next_day = date + 1

    print(next_month)
    print(next_day)

my_function(first, second)








