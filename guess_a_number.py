#second version
import random;
play = True
while play:
  random_number = random.randint(1,10);
#  print ("Random number %d" % random_number)
  keep_going = True
  print ("you only have 5 attempts")
  counter = 5
  while True:
    player = input("guess a secret number: ")
    if random_number != int(player):
      if int(player) > random_number:
        print ("Too high, Keep guessing")
      else:
        print ("Too low, Keep guessing")
      counter -= 1
      if counter > 0:
        print ("You have %d left" % counter)
      else:
        print ("you are done!")
        break
    else:
      print ("Right on! Number was %d" % random_number)
      break
  play_again = raw_input("do you wanna play again? y/n: ")
  if play_again == "y":
    play = True
  else:
    play = False
    print ("Nice playing with you")
    