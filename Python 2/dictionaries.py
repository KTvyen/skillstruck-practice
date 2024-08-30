#holidays = ["Christmas", "Hanukkah", "Thanksgiving", "Halloween"]

#classmates = {
    #"Billy" : 8,
    #"Vance" : 12,
   # "Alice" : 10,
#}

#print(classmates)

#{'Billy': 8, 'Vance': 12, 'Alice': 10}

#dicrionary vaules appear as pairs seperated by a comma, 
# the first item in the paring is called akey 
#the secoond is called a vaule 
# key : Vaule
# accessing items in the dictionary 

#classmates = {
    #"Billy" : 8,
    #"Vance" : 12,
    #"Alice" : 10
#}

#print(classmates["Vance"])

#output > 12
# the computer looks at the key and accesses the vaule attached 

#You can change a vaule in the dictionary by doing this 
#classmates = {
   # "Billy" : 8,
    #"Vance" : 12,
    #"Alice" : 10
#}
#classmates["Alice"] = 15
#print(classmates)
#output > {'Billy': 8, 'Vance': 12, 'Alice': 15}

#mountains = {
    #"Timpanogos" : 3,
    #"Everest" : 1,
    #"Kilimanjaro" : 2,
    #"Vesuvius" : 4
#}

#print(mountains)
#print(mountains["Vesuvius"])
#mountains["Kilimanjaro"] = 6
#print(mountains)
#print(" rate items.1 is not at all important and 10 is very important.")
#rate1 = input("rate a knife,  1 - 10")
#rate2 = input("rate a fire starter,  1 - 10")
#rate3 = input("rate a pot, 1 - 10")
#rate4 = input("rate a rope,  1 - 10")
#rate5 = input("rate a  tarp, 1 - 10")

#important = {
    #"Knife" : rate1,
    #"Fire starter" : rate2,
    #"Pot" : rate3,
    #"Rope" : rate4,
    #"Tarp" : rate5
#}

#print(important)

#knife = int(input("From 1-10, how important is a knife?"))
#fire_starter = int(input("From 1-10, how important is a fire starter?"))
#pot = int(input("From 1-10, how important is a pot?"))
#rope = int(input("From 1-10, how important is a rope?"))
#tarp = int(input("From 1-10, how important is a tarp?"))

#survive = { "knife" : knife , "fire starter": fire_starter , "pot": pot , "rope": rope , "tarp": tarp }

#print(survive)

#colors = { "red" : 4, "blue" : 5, "orange" : 1, "purple" : 6, "pink" : 2}

#colors["red"] = 14
#colors["blue"] = 15
#print(colors["orange"])
#print(colors["purple"])
#print(colors)

pets = {"fish" : 30, "dogs" : 2, "chickens" : 5, "cats" : 2, "bunny" : 1}

pets["fish"] = 20 
pets["bunny"] = 7


print("Because 10 fish died, and the bunny had 6 babies, you now have {} fish and {} bunnies at your house.".format(pets["fish"], pets["bunny"]))
print(pets)




