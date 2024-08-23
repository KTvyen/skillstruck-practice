#noun = input("CHoose a noun: ")
#plural_noun = input("Choose a plural noun: ")
#noun2 = input("Choose a noun: ")
#place = input("Name a place: ")
#adj = input("Choose an adjective: ")

#story = """
 #Friend: Wait your pet's name is what? 
 #You: My pet's name is """ + (noun.upper()) + "." + """
 #Friend: Well anyway can you imagine an army of """ +  (plural_noun.upper()) + """ 
 #You: Yeah that would be insane.
 #Friend: Have you heard? 
 #You: What? 
 #Friend: Well apparantly """ + (noun2.upper()) + """ 
 #has  been  the cause of the fires in """ + (place.upper()) + " it's because they are " + (adj.upper())

#print(story) 
#opinion = input(""" isn't that so crazy? What do you think?
#You: """) 

#noun1 = input("Choose a noun: ")

#pnoun1 = input("Choose a plural noun: ")

#noun2 = input("Choose a noun: ")

#place = input("Choose a place: ")

#adjective = input("Choose an adjective (Describing word): ")


#print("Did you know I have a pet " + noun1 + " He likes to run around and play with all of the " + pnoun1 + ". One morning, I woke up and he was wearing a " + noun2 + " for a hat!" + "I especially like to take him to the " + place +" because he shows off his " + adjective + " side.")

#earningsgoal = input("How much money do you want to save? ")

#months = int(earningsgoal)/12
#month_round = round(months, 2)

#weeks = int(earningsgoal)/4
#week_round = round(weeks, 2)



#print("To save up " + str(earningsgoal) + " dollars in one year, you will need to save " +  str(month_round) + " per month, " + str(week_round) + " per week.")

#age = input("What is your age?")
#print(int(age) + 18)

#number = input("random decimal")
#number = float(number)
#print(int(number))

#name = input("What is your name?")
#age = input("What is your age")

#age = int(age)
#print(name*age)

#name = input("What is your name?")
#age = input("What is your age?")
#birthday = input("When is your birthday?")

#print("Hi " + name + "! You are " + age + " years old and you were #born on " + birthday + ".") 

#number = input("Give me a random number")
#word = input("Give me a random word")
#print(number+word)

#animal = input("Give me a random animal")
#place = input("Give me a random place")
#noun = input("Give me a random plural noun")
#adjective = input("Give me a random adjective")

#print("Today I rode a " + animal + " to the " + place + " to buy some " + noun + "." + " It was " + adjective + ".")

#snickers = input("How many snickers you got.")
#nerds = input("How many nerds you got.")
#butterfingers = input("How many butterfingers you got.")


#total_candy = int(snickers) + int(nerds) + int(butterfingers)

#print("This year, you got " + str(snickers) + " snickers, " + str(nerds) + " nerds, and " + str(butterfingers) + " butterfingers. The total number of these candies is " + str(total_candy) + " candies.")

#recipient = input("Who is the message for?")

#place = input("Where do you want to meet?")

#minutes = input("In how many minutes would you like to meet?")

#print("I have an important message for " + recipient + ". Meet me at the " + place + " in " + minutes + " minutes. From, Detective Buggy.")

#number1 = int(input("What is your first number?"))
#number2 = int(input("What is your second number?"))
#print(number1 + number2)

#number = int(input("Choose a number"))
#less_than_number = number - 1 
#more_then_number = number + 1

#print(str(less_than_number) + "," + str(more_then_number))

#helpers = int(input("Who is willing to pitch in? "))
#amount_brining = int(input("How much money are you pitching in? "))

#total_money = helpers*amount_brining
#print(total_money) 

#inheritance_amount = 48682.76
#family_members = int(input("How many people are spliting the money?"))

#shared = inheritance_amount/family_members

#print( "If " + str(family_members) + " people split the inheritance, each person would get " + str(shared) + " dollars.")

#year = int(input("Pick a year "))
#century = (year-1)//100 + 1

#print(century)

#num_people = input("How many people are coming to dinner? ")
#num_people = int(num_people)
#hamburger_price = 1.29
#rolls_price = 0.49
#corn_price = 0.80
#hamburger_count = int(input("How many hamburgers will everyone have? "))
#rolls_count = int(input("How many rolls will everyone have? "))
#corn_count = int(input("How many pieces of corn will you have? "))
#total = 0
#total = total + (hamburger_count * hamburger_price * num_people)
#total = total + (rolls_count * rolls_price * num_people)
#total = total + (corn_count * corn_price * num_people)
#noChange = int(total / num_people)
#change = float(total / num_people)
#print("Each person owes $" + str(noChange) + " without change, or $" + str(change) + " if change is included.")

#family_members = int(input("How many family members do you have"))
#numbers_oranges = int(input("How many oranges are you eating?"))
#divided = numbers_oranges%family_members
#print(int(divided))

#number = int(input("Choose a number in the hundreds"))
#output = number % 100
#print(output)

#number = int(input("Choose a number in the tens place "))
#tens = int(number/10)
#ones = number % 10
#print(str(tens) + " " + str(ones))

#number = input("Choose a number in the tens place ")
#reverse = number[len(number)::-1]
#print(int(reverse))

#number = int(input("Choose a number in the hundreds"))
#output = number % 100
#print(int(output/10))

#short_quote = "We pick up our pens to write, and stand up to say what we wrote"
#long_quote =""" Welcome 
#when we stare into the abyass
#it eventually stares back at us"""

#print(short_quote)
#print(long_quote) 

#journal = """Today is the 7th of august
#its a wednesday 
#and a short day at my school"""
#print(journal)

#ideas =""" if i could i would want to creat a game that imitates knitting
#I would also like to create something that is like a bakery simulator"""

#sentence = input("sentence with @")
#print(sentence.replace("@", ""))

#greet = input("type a sentence")
#print(len(greet.split()))

#test = input("type a sentence that has a lot of e(s) ")
#print(str(test.find("e")) + "-" + str(test.rfind("e")))

#string = input("type a word ")

#third_char = string[2]
#third_last_char = string[-3]
#fourth_char = string[3]

#print(third_char + third_last_char + fourth_char)


#u_input = input("write something that has two 'g'(s) in it")
#print(u_input.rfind("g"))

#string = input("word")
#middle = len(string)//2
#front = string[middle:]
#back = string[ :middle]
#print(front + back)

#string1 = input("type a sentence that has 2 j(s) ")
#new_stringname = stringname[stringname.find("j"):stringname.rfind("j")+1]
#print(stringname.replace(stringname[stringname.find("j"):stringname.rfind("j")+1], ""))
#firstj = string1.find("j")
#lastj = string1.rfind("j")
#result = string1[:firstj] + string1[lastj + 1:]
#print(result)

#passage = "Cassowaries, genus Casuarius, are ratites (flightless birds without a keel on their sternum bone) that are native to the tropical forests of New Guinea (Papua New Guinea and Indonesia), East Nusa Tenggara, the Maluku Islands, and northeastern Australia. There are three extant species. The most common of these, the southern cassowary, is the third-tallest and second-heaviest living bird, smaller only than the ostrich and emu. Cassowaries feed mainly on fruit, although all species are truly omnivorous and will take a range of other plant food, including shoots and grass seeds, in addition to fungi, invertebrates, and small vertebrates. Cassowaries are very wary of humans, but if provoked they are capable of inflicting serious, even fatal, injuries to both dogs and people. The cassowary has often been labeled the world's most dangerous bird. Typically, all cassowaries are shy birds that are found in the deep forest. They are adept at disappearing long before a human knows they were there."
#check = "dangerous" in passage
#print(check)


#apple_per_tree = float(input("apples per tree"))
#per_1_wheelbarrow = apple_per_tree/3
#total = apple_per_tree*8
#per_whole_wheelbarrow = total/3
#bob = "If Bob harvested one tree, he would have {} apples per wheelbarrow. If he harvested the whole orchard, he would have {} apples per wheelbarrow."
#print(bob.format(per_1_wheelbarrow, per_whole_wheelbarrow)) 

#time_passed = float(input("number of minutes"))
#hours = round(time_passed/60)
#minutes = int(time_passed - (hours*60))
#answer = "It has been {} hour(s) and {} minute(s) since midnight."
#print(answer.format(hours, minutes))

#people = float(input("How many employees? "))
#tables = round(people/2)
#print("Minimum number of tables: " + str(tables))

#jasmine_bag = int(input("How many marble bags does Jasmine have?" ))
#chole_bag = int(input("How many marble bags does Chole have?" ))
#jasmine_marbles = jasmine_bag*12
#chole_marbles = chole_bag*10
#answer = "If Jasmine had {} bags, she would have {} marbles total. If Chloe had {} bags, she would have {} marbles total."
#print(answer.format(jasmine_bag, jasmine_marbles, chole_bag, chole_marbles)) 

#three_digits = input("Three digit number: ")
#sum_digits =  int(three_digits[0]) + int(three_digits[1]) + int(three_digits[2])
#answer = "The sum of those digits is {}" 
#print(answer.format(sum_digits))

#decimal = float(input("random decimal "))
#first_decimal = int((decimal * 10) % 10)
#answer = "The first decimal digit is {}"
#print(answer.format(first_decimal))

#dollar = float(input("ones place number: "))
#cents = float(input("tenths place number: "))/100
#cookie_amount = float(input("cookie amount: "))
#cost = (dollar + cents)*cookie_amount
#answer = "The total cost of {} cookies is ${}"
#print(answer.format(int(cookie_amount), cost))

#day = int(input("one number "))
#weekday = (day + 3)% 7
#answer = "The day of the week is the number {}."
#print(answer.format(weekday))


#memories = [1,2,"kat","mexico",4] 
#print(memories) 

#number1 = 10
#if number1 % 3 != 0:
    #print(str(number1) + " is not divisible by 3.")
#else:
    #print(str(number1) + " is divisible by 3.")