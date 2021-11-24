
def main():
  while True:

    import time


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



