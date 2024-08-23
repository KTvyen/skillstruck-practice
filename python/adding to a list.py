#goats = ["Billy", "Frannie", "Leslie", "Barbara", "Scott"]
#goats.append("Molly")
#print(goats)
#adds Molly to the end of the list

#print(10 + 12 * 5 % 3 - 2)

#goats = ["stuuf2", "back", "hello"]
#goats.insert(1,"janie")
#print(goats)

#flowers = ["rose", "tulip", "lilac", "sunflower"]
#flowers.append("lily")
#flowers.extend(["orchids", "carnations", "iris"])
#flowers.insert(1, "hydrangea")
#print(flowers)

#first = input("What other item do you want?")
#second = input("What final item do you want?")
#treats = ["popcorn", "popsicles", "soda", "chips", "cookies"]
#treats.append(first)
#treats.append(second)
#print(treats)

#olympics = ["running", "gymnastics", "swimming", "volleyball", "basketball"]
#new_olympics = ["karate", "surfing", "baseball", "skateboarding", "sport climbing"]
#olympics.extend(new_olympics)
#print(olympics)

#spelling = []
#word = input("What word do you want spelled out?")
#spelling.append(word)
#spelling.extend(word)
#spelling.append(word)
#print(spelling)
#mitch = int(input("how old is mitch?"))
#family = ["Amanda", "Levi", "Nicole", "Lilly"]
#if mitch >= 15:
	#family.insert(0, "Mitch")
#elif mitch >= 13:
   # family.insert(1, "Mitch")
#elif mitch >= 10:
    #family.insert(2, "Mitch")
#elif mitch >= 6:
    #family.insert(3, "Mitch")
#else:
    #family.insert(4, "Mitch")

#print(family)

my_list = [int(n) for n in input("Input a list of numbers").split()] 

cash_back = []

for x in my_list:
	if x >= 5:
		x = x * .1
		cash_back.append(round(x, 1))
		
print(cash_back)