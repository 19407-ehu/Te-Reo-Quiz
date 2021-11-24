
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
    time.sleep(1)
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
  time.sleep(0.8)
  print()
  print("Now before we begin, do you remember the rules of TRO, or do you need a reminder? ")
  no1 = input().lower()
  
  if no1 == "yes" or no1 == "y":
    print()
    print("Very well then! "+ rules) 

  elif no1 == "no" or no1 == "n":
    print()
    print("Very well then, lets get on with the show!")

  else:
    print()
    print("uh-huh, I have no clue what you just said, but we move on anyways.")

elif yes_or_no == "rap god" or yes_or_no == "rg":
  print()
  print("Uh, summa-lumma, dooma-lumma, you assumin’ I’m a human What I gotta do to get it through to you I’m superhuman? Innovative and I’m made of rubber so that anything you say is ricochetin’ off of me and it’ll glue to you and I’m devastating, more than ever demonstrating How to give a motherfuckin’ audience a feeling like it’s levitating Never fading, and I know the haters are forever waiting For the day that they can say I fell off, they’ll be celebrating ‘Cause I know the way to get ’em motivated I make elevating music, you make elevator music")

else:
  print()
  print("umm...") 
  time.sleep(0.5)
  print("I'll just take that as a no and carry on.")

#Sequence 2: Quiz start, asks a question and gives the player three prompts, one prompt is correct while the others are incorrect. Version 1. Harley Lambert-Ehu.

print("Alright, Here's the first question: ")
print("What is the English translation for Whaanau?")
print()
print("Is it..")
time.sleep(0.5)
print("A) Friend")
time.sleep(0.5)
print()
print("B) Family")
time.sleep(0.5)
print()

ans1 = input("Or C) Enemy ").lower()

if ans1 == "a" or ans1 == "c":
  print ("Your answer is...")
  time.sleep(1)
  print ("Incorrect! The correct answer is B) Family!")
  

elif ans1 == "b":
  print ("Your answer is...")
  time.sleep(1)
  print ("Correct! Good job on getting the first question right!")

else:
  print ("I'm sorry, thats not one of the answers. Please pick one of the three options.")

print("Well the second question is preped so get ready: ")
print("Fill in the blank. 'I'm hungry. Maybe i'll eat some _____' ")
print()
print("Is the blank..")
time.sleep(0.5)
print("A) Kaimoana")
time.sleep(0.5)
print()
print("B) Moana")
time.sleep(0.5)
print()

ans2 = input("Or C) Kai ").lower()

if ans2 == "a" or ans2 == "c":
  print ("Your answer is...")
  time.sleep(1)
  print ("Correct! This was actually a trick question since 'Kaimoana' translates to 'seafood' and 'kai' just translates to 'food'. So both answers wouldve been correct either way")
  

elif ans2 == "b":
  print ("Your answer is...")
  time.sleep(1)
  print ("Incorrect! Just in case you did not know, the word 'moana' translates to 'ocean', whereas  ")

else:
  print ("I'm sorry, thats not one of the answers. Please pick one of the three options.")

print("Anyways lets move on to the third question now, shall we? ")
print("What is the rough translation for the word 'whakapapa'")
print()
print("Is it..")
time.sleep(0.5)
print("A) Smooth")
time.sleep(0.5)
print()
print("B) Lineage")
time.sleep(0.5)
print()

ans3 = input("Or C) Hollow ").lower()

if ans3 == "a" or ans3 == "c":
  print ("Your answer is...")
  time.sleep(1)
  print ("Incorrect")
  

elif ans3 == "b":
  print ("Your answer is...")
  time.sleep(1)
  print ("Incorrect! Just in case you did not know, the word 'moana' translates to 'ocean', whereas ")

else:
  print ("I'm sorry, thats not one of the answers. Please pick one of the three options.")


