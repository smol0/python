#############################################
#cc battle ship


from random import randint # here we are calling the module random and importing the randint(low, high) function


board = [] # we made a verible called board and stored a empty list to it []


for i in range(5): #here we have used a for loop and range function so that we iterate throgh a specific line of code and we go through that code 5 times with the range function
  board.append(['O'] * 5) # here we are using the board verible and the .append to add O five times to the verible board it wont print it out it will keep it in the verible
print (board) # here we are printing out the content of the verible board

def print_board(board_in): # this is a typical define function we defiine a function called print_board that takes one argument called board_in
  for row in board: # here we are using the in built row function to make a for loop that will go through all the rows in the verible board
        print (" " .join(row)) #we woont use a noomal print statement to get a 5X5 O grid we need to get rid of the bracket and commas to do thst we use a built in function called .join which will join all the strings together to look a lot more like a grid we need use the " " qoute marks at first then .join then the verible 
        """print (row)""" # here we are printing out each row in board in differient row each so there wil be five O on each row until there are are 5 rows which means tha there should be 5X5 O grid
                  # .join is a built in function
def random_row(board): #here we are difine a function called random_row and giving it one argument called board 
  return randint(0, len(board) - 1) # then the funnction will return a random position between 0 to 5 on a row on the grid
    
def random_col(board): #here we are difine a function called random_col and giving it one argument called board 
  return randint(0, len(board) - 1) # then the funnction will return a random position between 0 to 5 on a colum on the grid
#we use len(board) - 1 in case we want to change the board size later.

ship_row = random_row(board)#here we are calling the random_row function to run the scripted code on that function
ship_col = random_col(board)#here we are calling the random_col function to run the scripted code on that function
######
print_board(board)# here we are callng the print_board function which will run the script that has this function name
######
print(ship_row, ship_col)
for turn in range(4): # here we are using a forloop so that the user get 4 guses.
  guess_row = int(input("Guess Row: ")) # here we are going to ask the user to Guess a number for the row
  guess_col = int(input("Guess Col: ")) # here we are going to ask the user to Guess a number for the coloum
##

  print(ship_row, ship_col) # this is for debugging here we are checking where the battle ship is if it is random and if it works
# we use ship_row and ship_col verible that are athached to the function of random_col and random_row to find the corinats of the ship

##########################################################################################################################################

  if guess_row == ship_row and guess_col == ship_col: # this is a typical if statement it will check if your answer is correct
    print ("Congratulation! You sank my battleship!") # and will congratulate you if you are right
    break # we use a break function s when we do get the guess right we dont have to guess 4 tiems 

###########################################################################################################################################
 # here we made an if to else statement within the else statement this is to see all the posible wrong answer that you can give and each different wrong answer will triger a different statement within the else statement
  else: # the else state ment is for if you you get it wrong if you do get it wrong it run this script
    if guess_row not in range(5) or \
       guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
###############################################
    elif (board[guess_row][guess_col] == 'X'): # this check the board to see wheather you have already guesed that position we do this by checking if your guess on the board if it is equaled to X it will tell you that you already guessed that 
      print ("You guessed that one already.")
#########################################
    else:
      print ("You missed my battleship!") # it will tell you that your answer was wrong
      print ("Your guess was row" ,guess_row, "collum" ,guess_col, "your guess is in the marking X")
      board[guess_row][guess_col] = "X" # it will place an X on the place where you guessed where the battel ship is because the 5x5 board is in a list all we do is use the list verible which is board and from that we use squre bracket to repersent the indecies in this case it will be the guess row and col   
      print_board(board) # here we are callng the print_board function which will run the script that has this function name
 ###
      print("The battle ship was at row" ,ship_row, "collum"  ,ship_col,"The battle ship is in the marking B")
      board[ship_row][ship_col] = "B"
      print_board(board)
  ###################################
    turn + 1 # returning to the for loop we set the for loop to a verible called turn here we are adding 1 to turn everytime we have completed 1 gusess  
    print ("This is your",turn,"turn") # here we are showing the user what turn they are on using the verible turn 
    if (turn == 3): # here is a if statement that follow if the verible turn exuals 3 we print game over the line we wrote turn + 1 will add 1 untill it is 3
          print("Game Over")





    
  
  
