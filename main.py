from random import choice
import art
from game_data import data
from replit import clear

def check_answer(followers_A,followers_B,guess, current_score):
    """Checks between A & B who has the highest followers and computes score accordingly"""
  
  if guess == 'A' and followers_A > followers_B:
    current_score += 1
    print(f"You're right! Current score: {current_score}")
    return True, current_score
  elif guess == 'B' and followers_A < followers_B:
    current_score += 1
    print(f"You're right! Current score: {current_score}")
    return True, current_score
  else:
    print(f"Sorry, that's wrong. Final score: {current_score}")
    return False, current_score

  

def game(compareA):
  """The function keeps the game running by asking user to guess who has more followers. A is chosen randomly the 1st time and thereafter  and B is chosen from previous choice A"""
  
  correct_answer = True
  score = 0
  while correct_answer:
    print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}.")
    print(art.vs)
    
    againstB = choice(data)
    while againstB == compareA:
      againstB = choice(data)
    
    print(f"Against B: {againstB['name']}, a {againstB['description']}, from {againstB['country']}.")
    #Ask Who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    clear()
    print(art.logo)  
    correct_answer, score = check_answer(compareA['follower_count'],againstB['follower_count'],guess, score)
    compareA = againstB

      
#pick random from list for Comparison A
print(art.logo)      
compareA = choice(data)
game(compareA)


