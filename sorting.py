
print ("=================")
print (" The Sorting Hat ")
print ("==================")

gryffindor = 0
slytherin = 0
hufflepuff = 0
ravenclaw = 0 

#question 1

print ("Q1) Do you like Dawn or Dusk? ")
print( "1) Dawn")
print ("2) Dusk")
answer = int(input("Enter Answer 1-2: "))
if answer == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif answer == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print ("Wrong output.")

# question 2 

print ("Q2) When I'm dead, I want people to remember me as: ")
print( "1) The Good")
print ("2) The Great")
print ("3) The Wise")
print ("4) The Bold")
answer = int(input("Enter Answer 1-4: "))
if answer == 1:
  hufflepuff = hufflepuff + 2
elif answer == 2:
  slytherin = slytherin + 2
elif answer == 3:
  ravenclaw = ravenclaw + 2
elif answer == 4:
  gryffindor = gryffindor + 2
else: 
  print ("Wrong output.")

# question 3
print ("Q3) Which kind of instrument most pleases your ear?")
print ("1) The violin")
print ("2) The trumpet")
print ("3) The piano")
print ("4) The drum")
answer = int (input ("Enter Answer 1-4: "))
if answer == 1:
  slytherin = slytherin + 2
elif answer == 2:
  hufflepuff = hufflepuff + 2
elif answer == 3:
  ravenclaw = ravenclaw + 2
elif answer == 4:
  gryffindor = gryffindor + 2
else:
  print ("Wrong output.")

# question 4
print ("Q1) Do you like Sea or Mountain? ")
print( "1) Sea")
print ("2) Mountain")
answer = int(input("Enter Answer 1-2: "))
if answer == 1:
  gryffindor = gryffindor + 1
  slytherin = slytherin + 1
elif answer == 2:
  hufflepuff = hufflepuff + 1
  ravenclaw = ravenclaw + 1
else:
  print ("Wrong output.")

# question 5
print ("Q3) What's your favourite colour?")
print ("1) Green")
print ("2) Yellow")
print ("3) Blue")
print ("4) Red")
answer = int (input ("Enter Answer 1-4: "))
if answer == 1:
  slytherin = slytherin + 2
elif answer == 2:
  hufflepuff = hufflepuff + 2
elif answer == 3:
  ravenclaw = ravenclaw + 2
elif answer == 4:
  gryffindor = gryffindor + 2
else:
  print ("Wrong output.")

# question 6
print ("Q1) Do you like to write or to read, or both? ")
print( "1) Write")
print ("2) Read")
print ("3) Both")
print ("4) Neither")
answer = int(input("Enter Answer 1-4: "))
if answer == 1:
  slytherin = slytherin + 2
elif answer == 2:
  hufflepuff = hufflepuff + 2
elif answer == 3:
	ravenclaw = ravenclaw + 2
elif answer == 4:
  gryffindor = gryffindor + 2
else:
  print ("Wrong output.")

# question 7
print ("Q3) What do you value most in a friend?")
print ("1) Loyalty")
print ("2) Kindness")
print ("3) Honesty")
print ("4) Brotherhood")
answer = int (input ("Enter Answer 1-4: "))
if answer == 1:
  slytherin = slytherin + 2
elif answer == 2:
  hufflepuff = hufflepuff + 2
elif answer == 3:
  ravenclaw = ravenclaw + 2
elif answer == 4:
  gryffindor = gryffindor + 2
else:
  print ("Wrong output.")

# question 8
print ("Q3) Choose a pet.")
print ("1) Cat")
print ("2) Hamster")
print ("3) Owl")
print ("4) Dog")
answer = int (input ("Enter Answer 1-4: "))
if answer == 1:
  slytherin = slytherin + 2
elif answer == 2:
  hufflepuff = hufflepuff + 2
elif answer == 3:
  ravenclaw = ravenclaw + 2
elif answer == 4:
  gryffindor = gryffindor + 2
else:
  print ("Wrong output.")

# final count
print ("-----------------")
print ("   Final score!  ")
print ("-----------------")
print ("Gryffindor: ", gryffindor)
print ("Slytherin: ", slytherin)
print ("Ravenclaw: ", ravenclaw)
print ("Hufflepuff: ", hufflepuff)

# bonus 
print ("-----------------------")
print ("THE SORTING IS COMPLETE!")
print ("-----------------------")
print ("According to your score, you are a...")
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print ("🦁  GRYFFINDOR!!!!  🦁")
elif ravenclaw >= gryffindor and ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print ("🦅  RAVENCLAW!!!!  🦅")
elif hufflepuff >= gryffindor and hufflepuff >= ravenclaw and hufflepuff >= slytherin:
  print ("🦡  HUFFLEPUFF!!!!  🦡 ")
else:
  print ("🐍  SLYTHERIN!!!!!  🐍")