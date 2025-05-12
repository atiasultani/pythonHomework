# Paper , Rock ,  Scissors

import random
def play():
    user=input(" \n 'r' for Rock ,\n 'p' for Paper ,\n 's' for Scissors \n What is Your Choice :")
    computer=random.choice(['r','p','s'])
    if user==computer:
        return "Game is Tie Between You and Computer"

    def is_win(player,oppenent):
    # if rock beat paper r>s ,scissor beat paper s>p, or paper > rock
    # return true if player win
        if (player=='r' and oppenent=='s') or (player=='s' and oppenent=='p') or (player=='p' and oppenent=='r'):
            return True
    
    if is_win(user,computer):
        return 'You Win !'
    return " You Lost ! "

print (play())