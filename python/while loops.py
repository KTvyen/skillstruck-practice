#people_in_line = 20
#while people_in_line > 0:
    #print("There are " + str(people_in_line) + " people in #line. Keep costar running!") 
    #people_in_line = people_in_line -1

    #Every time the loop runs, it subtracts 1 from the variable named people_in_line.

    #print("Stop the ride")

#While loops run while a condition is true.
#Every time the loop runs, it checks the line to see if it's empty. If the line is empty, the people_in_line condition is not met, which will end the while loop.

# If you don't include a way for the condition to stop being met, the code will just run and run without an exit.  The programmer must include a way to quit the loop.  These are done with decrement and increment operators. 

#loop will continue without stop unless programed to 

#loops that continue for too long can lead to computer crashes

# people_in_line = people_in_line -1 <- in this line its a decrement a way to quit a loop 
#Line above can also be written like this people_in_line = -1

#and increment operator works like a decrement operator but instead of subtracting it adds 

#example people_in_line += 1 

#  += means shorthand for addition and assignment. It adds the value on the right side of the operator to the variable on the left side and then assigns the result back to that variable.

# if you make and infinate loop and run it (thats fine) just quit that tab and come back and add an increment or decrement before running again.

#loops don't stop unless you tell it too

#age = 17
#while age >= 0:
    #print(age)
    #age -= 1

#age = 17
#while age >= 0:
    #if age == 5 or age == 10:
        #print(age)
    #age -= 1

    # you can add if statments into while loops (other type of of loop is for in variable *


#total = 0
#number = int(input("enter a number"))
#hile number > 0:
    #total += 1
    #number = int(input("enter a number"))
#print(total)

#my_number = int(input("Pick a number."))
#total = my_number
#while my_number != 0 :
	#my_number = int(input("Pick a number."))
	#total += my_number 
	
#print(total)

#my_number = int(input("Pick a number."))
#largest = my_number
#while my_number != 0:
	#my_number = int(input("Pick a number."))
	#if my_number > largest :
		#largest = my_number 

#print(largest)

#my_number = int(input("Pick a number."))
#total = my_number
#number_count = 1
#while my_number != 0 :
	#my_number = int(input("Pick a number."))
	#total += my_number
	#number_count += 1
	#if my_number == 0 :
		#number_count -= 1
	
#average = total/number_count

#print(average)

#x=0
#y=0
#run=True
#while x < 5 and y < 5 and x > -5 and y > -5 and run == True:
	#direction=input('What way would you like to go (n,s,e,w)? ')
	#if direction == "n":
		#y+=1
	#elif direction == "s":
		#y-=1
	#elif direction == "e":
		#x+=1
	#elif direction == "w":
		#x-=1
	#elif direction=='Exit':
		#print('Program exited. You left the grid at (' + str(x) + ',' + str(y) + ')')
		#run=False
	#else:
		#print('Bad input')
#print('You left the grid at ' + '(' + str(x) + "," + str(y) + ')')

day1 = int(input("Enter your first distance on day 1 (10 or bigger)"))
day2 = int(input("Enter your race distance"))
total_days = 1
loop = 0
max_loops = 100
while day1 <= day2 and loop < max_loops:
    day1 += day1 * .1
    total_days += 1
    loops += 1

if loop == max_loops:
    break

print(total_days)
