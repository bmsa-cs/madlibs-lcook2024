"""
MadLibs
Author: Logan Cook
Period/Core: Core 3

All stories courtesy of Pengiun Random House

"""

count = 0
tempone_count = 0
temptwo_count = 0
tempthree_count = 0

def template_one():
  global tempone_count
  print("You chose template 1!")
  adj = input("Please choose an adjective: ")
  ing = input("Please choose a verb ending in ing: ")
  plunn = input("Please choose a plural noun: ")
  nn = input("Please choose a noun: ")
  nn_two = input("Please choose a noun: ")
  nn_three = input("Please choose a noun: ")
  nn_four = input("Please choose a noun: ")
  adj_two = input("Please choose an adjective: ")
  nn_five = input("Please choose a noun: ")
  plunn_two = input("Please choose a plural noun: ")
  plunn_three = input("Please choose a plural noun: ")
  nn_six =   input("Please choose a noun: ")
  adverb = input("Please choose an adverb: ")
  nn_seven = input("Please choose a noun: ")
  nn_eight = input("Please choose a noun: ")
  print(" ")
  print(f"To be performed by two {adj} students. \n OFFICER: Sir, do you realize how fast you were {ing}? \n DRIVER: No, how fast was I {ing}? \n OFFICER: You were going fifty {plunn} per hour in a twenty-five {nn} zone \n DRIVER: I'm sorry. I'm nervous. I'm taking my {nn_two} to the hospital. She's about have a/an {nn_three}. \n OFFICER: You also went through a red {nn_four} and failed to stop at a/an {adj_two} sign. May I see your driver's {nn_five}? \n DRIVER: Yes. Oh, my! I left it in my other pair of {plunn_two}. You see, my wife started to have labor {plunn_three} and I wanted to get her to the {nn_six} as {adverb} as possible. \n OFFICER: Your wife? \n DRIVER: She's right there in the back {nn_seven}. Oh, my! Would you believe I forgot my {nn_eight} too?")
  tempone_count = tempone_count + 1

def template_two():
  global temptwo_count
  print("You chose template 2!")
  adv = input("Please choose an adverb: ")
  plunn = input("Please choose a plural noun: ")
  adj = input("Please choose an adjective: ")
  plunn_two = input("Please choose a plural noun: ")
  body = input("Please choose a body part: ")
  adj_two = input("Please choose an adjective: ")
  animal = input("Please choose an animal: ")
  adj_three = input("Please choose an adjective: ")
  nn = input("Please choose a noun: ")
  number = input("Please choose a number: ")
  adj_four = input("Please choose an adjective: ")
  verb = input("Pleasae choose a verb: ")
  body_two = input("Please choose a body part: ")
  adj_five = input("Please choose an adjective: ")
  food = input("Please choose a type of food: ")
  body_three = input("Please choose a body part: ")
  print(" ")
  print(f"Although we believe ourselves to be {adv} civilized, most of us are really {plunn} at heart, because we will believe in {adj} superstitions that began while humans still lived in {plunn_two}. Some of those superstitions are: \n 1: If you spill salt, throw some over your left {body} for {adj_two} luck. \n 2: If a black {animal} runs in front of you, you are in {adj_three} trouble. \n 3: If you break a/an {nn} you will have {number} years of {adj_four} luck. \n 4: Never {verb} under a ladder. \n 5: If your {body_two} itches, it means you will have a/n {adj_five} visitor. \n 6: If you want to keep vampires away from you, always wear {food} on a string around your {body_three}.")
  temptwo_count = temptwo_count + 1

def template_three():
  global tempthree_count
  print("You chose template 3!")
  nn = input("Please choose a noun: ")
  nn_two = input("Please choose a noun: ")
  adj = input("Please choose an adjective: ")
  body = input("Please choose a plural body part: ")
  color = input("Please choose a color: ")
  plunn = input("Please choose a plural noun: ")
  nn_three = input("Please choose a noun: ")
  tempthree_ing = input("Please choose a verb ending in ing: ")
  plunn_two = input("Please choose a plural noun: ")
  adj_two = input("Please choose an adjective: ")
  adj_three = input("Please choose an adjective: ")
  plunn_three = input("Please choose a plural noun: ")
  nn_four = input("Please choose a noun: ")
  adj_four = input("Please choose an adjective: ")
  body_two = input("Please choose a body part: ")
  nn_five  = input("Please choose a noun: ")
  nn_six  = input("Please choose a noun: ")
  adv = input("Please choose an adverb: ")
  print(" ")
  print(f"If a story begins \"Once upon a/an {nn}\" you know you are about to read a fairy {nn_two}. It is amazing how these {adj} stories remain indelibly ethced in our {body}. Who can forget Snow {color} and the Seven {plunn}, Beauty and the {nn_three}, or Little Red {tempthree_ing} Hood! Fairy tales introduced us to the magical world of wicked {plunn_two}; big, {adj_two} wolves; {adj_three} wizards; and dwarfs who wore funny {plunn_three}. These remarkable stories taught us that good always triumphs over {nn_four} and make us believe in the {adj_four} power of a kiss. Why not? One good smack on the {body_two} could change a frog into a handsome {nn_five}, enabling him to marry the {nn_six} of his dreams and live, as is written all these romantice stories, {adv} ever after.")
  tempthree_count = tempthree_count + 1

def mad_libs():
  global template_choice

  #While loop to make sure player is inputting a number for template_choice
  while type(template_choice) != int:
    try:
      int(template_choice)
      while int(template_choice) > 3:
        print("Please pick a number between 1 and 3 ")
        template_choice = input("Do you want to play template 1, 2, or 3? ")
      if type(template_choice):
        break
    except ValueError:
      print("Please input a number!")
      template_choice = input("Do you want to play template 1, 2, or 3? ")

  if int(template_choice) == 1:
    template_one()
  elif int(template_choice) == 2:
    template_two()
  elif int(template_choice) == 3:
    template_three()

def mad_libs_twothree():
  global template_choice
  #While loop to make sure player is inputting a number for template_choice
  while type(template_choice) != int:
    try:
      int(template_choice)
      while int(template_choice) <= 1 or int(template_choice) > 3:
        print("Please pick \'Superstitions\'(2) or \'Fairy Tales and Romance\'(3) ")
        template_choice = input("Do you want to play \'Superstitions\'(2) or \'Fairy Tales and Romance\'(3)? ")
      if type(template_choice):
        break
    except ValueError:
      print("Please input a number!")
      template_choice = input("Do you want to play \'Superstitions\'(2) or \'Fairy Tales and Romance\'(3)? ")
  if int(template_choice) == 2:
    template_two()
  elif int(template_choice) == 3:
    template_three()

def mad_libs_onethree():
  global template_choice

  #While loop to make sure player is inputting a number for template_choice
  while type(template_choice) != int:
    try:
      int(template_choice)
      while int(template_choice) < 1 or int(template_choice) > 3:
        print("Please pick\'A Speeding Ticket\'(1) or \'Fairy Tales and Romance\'(3) ")
        template_choice = input("Do you want to play \'A Speeding Ticket\'(1) or \'Fairy Tales and Romance\'(3)? ")
      if type(template_choice):
        break
    except ValueError:
      print("Please input a number!")
      template_choice = input("Do you want to play \'A Speeding Ticket\'(1) or \'Fairy Tales and Romance\'(3)? ")
  if int(template_choice) == 1:
    template_one()
  elif int(template_choice) == 3:
    template_three()

def mad_libs_twoone():
  global template_choice

  #While loop to make sure player is inputting a number for template_choice
  while type(template_choice) != int:
    try:
      int(template_choice)
      while int(template_choice) < 1 or int(template_choice) > 2:
        print("Please pick\'A Speeding Ticket\'(1) or \'Superstitions\'(2) ")
        template_choice = input("Do you want to play \'A Speeding Ticket\'(1) or \'Superstitions\'(2)? ")
      if type(template_choice):
        break
    except ValueError:
      print("Please input a number!")
      template_choice = input("Do you want to play \'A Speeding Ticket\'(1) or \'Superstitions\'(2)? ")
  if int(template_choice) == 1:
    template_one()
  elif int(template_choice) == 2:
    template_two()



print("Let's play Silly Setences!")
while count == 0:
  template_choice = input("Do you want to play \'A Speeding Ticket\'(1), \'Superstitions\'(2), or \'Fairy Tales and Romance\'(3)? ")
  mad_libs()
  count = count + 1

while count != 3 and count != 0:
  if count != 3 and count != 0:
    print("Let's play Silly Setences again, try out a different template!")
  if count == 0:
    template_choice = input("Do you want to play \'A Speeding Ticket\'(1), \'Superstitions\'(2), or \'Fairy Tales and Romance\'(3)? ")
    mad_libs()
    count = count + 1
    print(" ")
    print("Let's play Silly Setences again, try out a different template!")
  if tempone_count > 0 and temptwo_count == 0 and tempthree_count == 0:
    template_choice = input("Do you want to play \'Superstitions\'(2) or \'Fairy Tales and Romance\'(3)? ")
    mad_libs_twothree()
    count = count + 1
  elif temptwo_count > 0 and tempone_count == 0 and tempthree_count == 0:
    template_choice = input("Do you want to play \'A Speeding Ticket\'(1) or \'Fairy Tales and Romance\'(3)? ")
    mad_libs_onethree()
    count = count + 1
  elif tempthree_count > 0 and tempone_count == 0 and temptwo_count == 0:
    template_choice = input("Do you want to play \'A Speeding Ticket\'(1) or \'Superstitions\'(2)? ")
    mad_libs_twoone()
    count = count + 1
  elif tempone_count != 1 and temptwo_count == 1 and tempthree_count == 1:
    print (" ")
    print("You've played templates 2 and 3, time to play \'A Speeding Ticket\'!")
    template_one()
    count = count + 1
  elif temptwo_count != 1 and tempone_count == 1 and tempthree_count == 1:
    print (" ")
    print("You've played templates 1 and 3, time to play \'Superstitions\'!")
    template_two()
    count = count + 1
  elif tempthree_count != 1 and tempone_count == 1 and temptwo_count == 1:
    print(" ")
    print("You've played templates 1 and 2, time to play \'Fairy Tales and Romance\'!")
    template_three()
    count = count + 1

print(" ")
print("Thanks for playing!")
