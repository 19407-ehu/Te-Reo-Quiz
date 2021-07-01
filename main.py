#Te Reo Quiz. Harley Lambert-ehu, Version 1, 25/06/2021.

#Sequence 1: introduction to the game, player, and rules. Version 1, by Harley Lambert-Ehu
import time

print("Welcome to the TRO (Te Reo Obviously) Show!")

name = input("Before we beigin, why don't you tell us your name. ")
print()
print("Ah yes, welcome to the show, " + name,"!")
time.sleep(0.5)
print()
yes_or_no = input("Now tell me, is this your first time on the TRO Show? ").lower()
print()
rules = ("So the game is simple, I will ask a question about the meaning for a basic word in Te Reo. You must select one of the three prompts that will popup after I finish asking the question. These prompts will contain three different answers, but only one will be correct, and you must pick the right to move on. If you get it wrong, then you'll look like an idiot.")

if yes_or_no == "yes" or yes_or_no == "y":
  print("It is?")
  time.sleep(1) 
  yes1 = input("Well have you at least seen an episode of it on TV? ").lower()
  
  if yes1 == "yes" or yes1 == "y":
    print()
    print("Ok thank god! Well just incase, let me remind you about the rules of TRO.")
    time.sleep(0.5)
    print()
    print(rules)

  elif yes1 == "no" or yes1 == "n":
    print()
    print("Wha- HUH? How did you even get here?")
    time.sleep(0.5)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1.5)
    print(".")
    time.sleep(2)
    print("Actually nevermind that, allow me to tell you how to play TRO.")
    time.sleep(0.5)
    print()
    print(rules)

  else:
    print()
    print("I'm sorry what did you say? you know what, I'll just explain the rules to you anyways.")
    print()
    print(rules)

elif yes_or_no == "no" or yes_or_no == "n":
  print()
  print("Very nice to have a re-occuring guest, but I can't remember who you are")
  print()
  no1 = input("Now before we begin, do you remember the rules of TRO, or do you need a reminder? ").lower()
  
  if no1 == "yes" or no1 == "y":
    print()
    print("Very well then! "+ rules) 

  elif no1 == "no" or no1 == "n":
    print()
    print("Very well then, lets get on with the show!")

  else:
    print()
    print("uh-huh, I have no clue what you just said, but we move on anyways.")

else:
  print()
  print("umm...") 
  time.sleep(0.5)
  print("I'll just take that as a no and carry on.")



  








