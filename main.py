"""
MadLibs
Author: Logan Cook
Period/Core: Core 3

All stories courtesy of Pengiun Random House

"""

print("Let's play Silly Setences!")
def mad_libs():
  template_choice = input("Do you want to play template 1, 2, or 3? ")

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


  def template_one():
    print("You chose template 1!")
    tempone_adj = input("Please choose an adjective: ")
    tempone_ing = input("Please choose a verb ending in ing: ")
    tempone_plunn = input("Please choose a plural noun: ")
    tempone_nn = input("Please choose a noun: ")
    tempone_nn_two = input("Please choose a noun: ")
    tempone_nn_three = input("Please choose a noun: ")
    tempone_nn_four = input("Please choose a noun: ")
    tempone_adj_two = input("Please choose an adjective: ")
    tempone_nn_five = input("Please choose a noun: ")
    tempone_plunn_two = input("Please choose a plural noun: ")
    tempone_plunn_three = input("Please choose a plural noun: ")
    tempone_nn_six =   input("Please choose a noun: ")
    tempone_adverb = input("Please choose an adverb: ")
    tempone_nn_seven = input("Please choose a noun: ")
    tempone_nn_eight = input("Please choose a noun: ")
    print(" ")
    print(f"To be performed by two {tempone_adj} students. \n OFFICER: Sir, do you realize how fast you were {tempone_ing}? \n DRIVER: No, how fast was I {tempone_ing}? \n OFFICER: You were going fifty {tempone_plunn} per hour in a twenty-five {tempone_nn} zone \n DRIVER: I'm sorry. I'm nervous. I'm taking my {tempone_nn_two} to the hospital. She's about have a/an {tempone_nn_three}. \n OFFICER: You also went through a red {tempone_nn_four} and failed to stop at a/an {tempone_adj_two} sign. May I see your driver's {tempone_nn_five}? \n DRIVER: Yes. Oh, my! I left it in my other pair of {tempone_plunn_two}. You see, my wife started to have labor {tempone_plunn_three} and I wanted to get her to the {tempone_nn_six} as {tempone_adverb} as possible. \n OFFICER: Your wife? \n DRIVER: She's right there in the back {tempone_nn_seven}. Oh, my! Would you believe I forgot my {tempone_nn_eight} too?")


  def template_two():
    print("You chose template 2!")
    temptwo_adv = input("Please choose an adverb: ")
    temptwo_plunn = input("Please choose a plural noun: ")
    temptwo_adj = input("Please choose an adjective: ")
    temptwo_plunn_two = input("Please choose a plural noun: ")
    temptwo_body = input("Please choose a body part: ")
    temptwo_adj_two = input("Please choose an adjective: ")
    temptwo_animal = input("Please choose an animal: ")
    temptwo_adj_three = input("Please choose an adjective: ")
    temptwo_nn = input("Please choose a noun: ")
    temptwo_number = input("Please choose a number: ")
    temptwo_adj_four = input("Please choose an adjective: ")
    temptwo_verb = input("Pleasae choose a verb: ")
    temptwo_body_two = input("Please choose a body part: ")
    temptwo_adj_five = input("Please choose an adjective: ")
    temptwo_food = input("Please choose a type of food: ")
    temptwo_body_three = input("Please choose a body part: ")
    print(" ")
    print(f"Although we believe ourselves to be {temptwo_adv} civilized, most of us are really {temptwo_plunn} at heart, because we will believe in {temptwo_adj} superstitions that began while humans still lived in {temptwo_plunn_two}. Some of those superstitions are: \n 1: If you spill salt, throw some over your left {temptwo_body} for {temptwo_adj_two} luck. \n 2: If a black {temptwo_animal} runs in front of you, you are in {temptwo_adj_three} trouble. \n 3: If you break a/an {temptwo_nn} you will have {temptwo_number} years of {temptwo_adj_four} luck. \n 4: Never {temptwo_verb} under a ladder. \n 5: If your {temptwo_body_two} itches, it means you will have a/n {temptwo_adj_five} visitor. \n 6: If you want to keep vampires away from you, always wear {temptwo_food} on a string around your {temptwo_body_three}.")


  def template_three():
    print("You chose template 3!")
    tempthree_nn = input("Please choose a noun: ")
    tempthree_nn_two = input("Please choose a noun: ")
    tempthree_adj = input("Please choose an adjective: ")
    tempthree_body = input("Please choose a plural body part: ")
    tempthree_color = input("Please choose a color: ")
    tempthree_plunn = input("Please choose a plural noun: ")
    tempthree_nn_three = input("Please choose a noun: ")
    tempthree_ing = input("Please choose a verb ending in ing: ")
    tempthree_plunn_two = input("Please choose a plural noun: ")
    tempthree_adj_two = input("Please choose an adjective: ")
    tempthree_adj_three = input("Please choose an adjective: ")
    tempthree_plunn_three = input("Please choose a plural noun: ")
    tempthree_nn_four = input("Please choose a noun: ")
    tempthree_adj_four = input("Please choose an adjective: ")
    tempthree_body_two = input("Please choose a body part: ")
    tempthree_nn_five  = input("Please choose a noun: ")
    tempthree_nn_six  = input("Please choose a noun: ")
    tempthree_adv = input("Please choose an adverb: ")
    print(" ")
    print(f"If a story begins \"Once upon a/an {tempthree_nn}\" you know you are about to read a fairy {tempthree_nn_two}. It is amazing how these {tempthree_adj} stories remain indelibly ethced in our {tempthree_body}. Who can forget Snow {tempthree_color} and the Seven {tempthree_plunn}, Beauty and the {tempthree_nn_three}, or Little Red {tempthree_ing} Hood! Fairy tales introduced us to the magical world of wicked {tempthree_plunn_two}; big, {tempthree_adj_two} wolves; {tempthree_adj_three} wizards; and dwarfs who wore funny {tempthree_plunn_three}. These remarkable stories taught us that good always triumphs over {tempthree_nn_four} and make us believe in the {tempthree_adj_four} power of a kiss. Why not? One good smack on the {tempthree_body_two} could change a frog into a handsome {tempthree_nn_five}, enabling him to marry the {tempthree_nn_six} of his dreams and live, as is written all these romantice stories, {tempthree_adv} ever after.")


  if int(template_choice) == 1:
    template_one()
  elif int(template_choice) == 2:
    template_two()
  elif int(template_choice) == 3:
    template_three()

count = 0
while count < 3:
  mad_libs()
  count = count + 1
  print("Let's play Silly Setences again, try out a different template!")