import random
# ASCII art Sourced from github user wynand1004
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# The following function takes in a move as a parameter.
# It will return the corresponding string art based on the move.
"""
e.g:
move = "rock"
moveArt = printMove(move)
print(moveArt)
# will print the rock hand as shown below
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    
"""
def printMove(move):
#This conditional returns the appropriate string art if the move matches the art
  if move == 'rock':
    return rock
  if move == 'paper':
    return paper
  if move == 'scissors':
    return scissors


# The following function takes in the playerName as a parameter.
# The function will return the playerMove as a string
"""
e.g:
playerName = "Alex"
makePlayerMove(playerName)
# the following would get printed
Choose rock, paper, or scissors:
rock
Alex chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        
"""     

def makePlayerMove(playerName):
  playerMove = input("Choose rock, paper, or scissors: ")
  playerArt = printMove(playerMove)
  return playerArt



# The following function takes in the computerName as a parameter.
# The function will return the computerMove as a string
"""
e.g:
computerName = "Eric"
makeComputerMove(computerName)
# for this example, we will say the random number drawn was 1, so the following
will get printed
Eric chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        
"""
def makeComputerMove(computerName):
# Code
  compHand = random.randint(1,3)
#This conditional assigns a random string art to one of the random numbers 
  if compHand == 1:
    computerMove = "rock"
  elif compHand == 2:
    computerMove = "paper" 
  else: 
    computerMove = "scissors"

  computerArt = printMove(computerMove)

  return computerArt




# The following function takes in the playerMove and computerMove as parameters 
# and returns the winner as a string.
def checkRoundWinner(playerMove, computerMove):

#This conditonal returns the results of the round based on the player/comptuter
# moves
  if playerMove == rock and computerMove == paper:
    return "Computer Won"
  elif playerMove == rock and computerMove == scissors:
    return "Player Won"
  elif playerMove == rock and computerMove == rock:
    return "Tie"
  elif playerMove == paper and computerMove == paper:
    return "Tie"
  elif playerMove == paper and computerMove == scissors:
    return "Computer Won"
  elif playerMove == paper and computerMove == rock:
    return "Player Won"
  elif playerMove == scissors and computerMove == paper:
    return "Player Won"
  elif playerMove == scissors and computerMove == scissors:
    return "Tie"
  else:
    return "Computer Won"




# The main function will be the main driver for your game of rock, paper,
# scissors.

# We want the game to continue until either the player or the computer wins the
# best out of three.
# *Hint: a while loop might be helpful :)*
def main():
  playerName = input("Enter Player's Name: ")
  computerName = input("Enter Computer's Name:  ")

  playerScore = 0
  computerScore = 0
  round = 0

#This while loop ensures that the game runs if there is less than 3 rounds 
#and breaks when there is more than 3 rounds
  while round < 3:
#This condiitonal checks if player/computer does not have 2 points and 
#runs the game
    if playerScore != 2 or computerScore != 2:
      player_move = makePlayerMove(playerName)
      print(playerName + " chose " + player_move)
      computer_move = makeComputerMove(computerName)
      print(computerName + " chose " + computer_move)
      winner = checkRoundWinner(player_move, computer_move)
#This conditional checks and returns the results of the round, adds a 
#point to the winner and increases the round by 1
      if winner == "Computer Won":
        print(computerName + " won the round!")
        computerScore += 1
        round += 1
      elif winner == "Player Won":
        print(playerName +  " won the round!")
        playerScore += 1
        round += 1
      else:
        print("It was a tie!")
        round += 0
    else:
      break
      
#This conditional checks which player has the highest score and returns 
#the winner
  if playerScore > computerScore: 
    print(playerName + " won the match!")
  else: print(computerName, " won the match!")

  

main()
