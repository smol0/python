loop_condition = False

while loop_condition:
  print ("I am a loop")
  loop_condition = False
  loop_condition = True
  

while loop_condition:
  print ("I am a loop")
  loop_condition = False


  loop_condition = True

while loop_condition:
  print ("I am a loop")
  loop_condition = False
  




from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
while guesses_left > 0:
  guess = int(input("Your guess: "))
  if random_number == guess:
    print ("You win!")
    break
  guesses_left -= 1
    
