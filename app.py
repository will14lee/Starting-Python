# from math import *
# print (floor(3.7))
# print (ceil(3.7))
# print(sqrt(36))
# print ("Say hello to my little triangle!   /|")
# print ("                                  / |")
# print ("                                 /  |")
# print ("                                /___|")
# print ("   ____________")
# print ("  /            \\")
# print (" /    O       O \\")
# print ("|  ___________   |")
# print (" \\ \\---------/  /")
# print ("  \\____________/ ")
# numbers= [5, 4, 3, 2, 1, -9]
# print("Numbers \nnumbers".isupper()) 
# print("numbers \nnumbers".islower()) 
# greeting= "Hello World"
# print(len(greeting)) 
# print(greeting.index("o")) 
# print(greeting.replace("Hello", "Goodbye"))
# print(numbers[0] * numbers[1])
# print("5" + str(10))
# print(abs(numbers[5]))
# print(pow(4, 2))
# print(max(numbers))
# print(min(numbers))
# print(round(4.5))


# name= input("Enter you name: ")
# print("Hello " + name + "!")
# credit_card_info= input("Please type your credit card information: ")
# input("Is " + credit_card_info +" correct?:" )
# print("Thank you.")
# print("Processing.")
# print("Processing..")
# print("Processing...")
# print("Ha ha. Real funny asshole. No. Seriously credit card info now.")

# Simple calculator
# num1=input("First number to add: ")
# num2=input("Second number to add: ")
# result= float(num1) + float(num2)
# print(num1 + " + " + num2 + "= " + str(result))



# print("Who are you?")
# name= input("My name is: ")
# print("Hey, " + name + ". Welcome to your assessment...")
# print("Today we will be measuring your aptitude to being human")
# input("Understood?:")
# print("Whatever...")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("Anyways we will begin. Try to be a little bit human okay?")
# answer=input("12 x 12=:")
# print(answer == "144")





# Madlib game
# electronic= input("Input an electronic: ")
# name= input("Input a name: ")
# date_idea= input("Input a date idea: ")
# verb= input("Input a verb: ")
# adverb= input("Input a adverb: ")
# breakfast_item= input("Input a breakfast item: ")
# tv_show= input("Input a tv show: ")

# print("I want to be a " + electronic + ".")
# print("Because if I was a " + electronic + " maybe " + name + " would be willing to go " + date_idea + " with me.")
# print("But knowing my luck, I will only be able to " + verb + " " + adverb)
# print("I really want to eat some " + breakfast_item + " while watching " + tv_show)

# sentence= ["let's", "eat", "Grandpa"]
# print(sentence[0] + " " + sentence[1] + " " + sentence[2])
# print(sentence[1] + " " + sentence[0] + " " + sentence[2])
# print(sentence[1] + " " + sentence[2] + " " + sentence[0])
# print(sentence[2] + " " + sentence[1] + " " + sentence[0])
# working_sentence= print(sentence[2] + " " + sentence[0] + " " + sentence[1])

# sentence[2]= "Granpear"
# print(sentence[2] + " " + sentence[0] + " " + sentence[1])

from copy import copy


other_sentence= ["Roast beef", "Fried Chicken", "a grape", "nothing"]

# sentence.append("Borscht")
# print(sentence[1:3])
print("This is the initial list=")
print(other_sentence)

# # to put something before fried chicken
# print("Adding Lemons to the list")
# other_sentence.insert(1, "Lemons")
# print(other_sentence)

# print("Removing Lemons to the list")
# other_sentence.remove("Lemons")
# print(other_sentence)


# print("This will destroy the entire list")
# other_sentence.clear()
# print("Well here's the list!")
# print(other_sentence)










# pop, index, count, count, sort, reverse, copy



# other_sentence.pop()
# print("After I pop something off it looks like this")
# print(other_sentence)
# print("\"nothing\" was removed from the list")

# print(other_sentence.index("Fried Chicken"))

# count the number of times that roast beef is in the list
# other_sentence.insert(1, "Roast beef")
# print(other_sentence.count("Roast beef"))


# sorting the list
# other_sentence.sort()

# other_sentence.reverse()
other_sentence2= other_sentence.copy()

print("This is other_sentence2 list")
print(other_sentence2)