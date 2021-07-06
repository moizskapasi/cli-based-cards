"""
This module contains various functions needed to play a game of blackjack. It also uses
functions from the cards.py module. It also contains the main function that is a test function
that plays a whole game of blackjack to test the functions.

Authors: Moiz Shabbir Kapasi
"""
#double check the names of the hands(must be dealer score and player score).
import cards #imports the cards.py module made in previous activity.

def  hand_score(hand):
    """
    First the function makes a new list with only the ranks of the cards in the hand, and sorts
    them in ascending order. It also declares a new variable to keep track of the points. Then
    it iterates over all the cards, and for each card it adds the appropriate points to the total.
    In the end it returns the total score.
    """
    rankhand=[]
    for card in hand:
        rankhand.append(card[0])
    rankhand.sort()
    totalpoint=0
    for rank in rankhand:
        if rank>=11 and rank<14:
            point=10
        elif rank <11:
            point=rank
        elif rank == 14:
            if totalpoint+11 > 21:
                point=1
            else:
                point=11
        totalpoint=totalpoint+point
    return totalpoint

def print_hand_and_score(name,hand):
    """
    This function prints the name of the player, the cards currently in their hand and it's score.
    This function uses bubble sort to put the cards in ascending order before printing. It also
    prints "Busted" if the score is over 21 (i.e. if the player has lost).
    """
    print("\n",name,"\n")
    x=len(hand)
    count=0
    while count <= x:
        for i in range(x-1):
            if hand[i][0] > hand[i+1][0]:
                hand[i+1],hand[i]=hand[i],hand[i+1]
        count+=1
    for card in hand:
        print(card[3],end="   ")
    print("\n")
    score=hand_score(hand)
    if score > 21:
        print("\nScore :",score,"(Busted)")
    else:
        print("\nScore :",score)

def win_or_lose(player_score,dealer_score):
    """
    This function takes in the player and dealer score to tell
    the user whether they won, or the dealer won, or it is a draw.
    """
    if (player_score > 21 and dealer_score > 21) or player_score == dealer_score:
        print("\nThe game has come to a draw.")

    elif (dealer_score > 21) or ((player_score > dealer_score) and (player_score < 22)):
        print("\nYou win.")

    elif (player_score > 21) or ((dealer_score > player_score) and (dealer_score < 22)):
        print("\nDealer wins.")


def dealer_hit_or_stand(player_hand,dealer_hand):
    """
    This function will return True or False based on the conditions for the dealer to
    draw a card.
    """
    pscore = hand_score(player_hand)
    dscore = hand_score(dealer_hand)
    if dscore < 17 or dscore < pscore:
        return True
    else:
        return False

def player_hit_or_stand():
    """
    This function returns True if the user enters H or False if they enter S. This funciton also
    goes into recursion if the input is not valid.
    """
    player_enter = str(input("\nEnter (H or h) for hit or (S or s) for stand:"))

    if player_enter == "H" or player_enter == "h":
        return True
    elif player_enter == "S" or player_enter == "s":
        return False
    else:
        print("\nSorry you have chosen an invalid input")
        return player_hit_or_stand()
    
def main():
    """
    This is the main function that conrtols the whole blackjack game.
    """
    name=str(input("Enetr your name: "))
    deck=cards.make_deck()
    cards.shuffle(deck)
    topdeck,bottomdeck = cards.cut(deck)
    player,dealer=cards.deal(bottomdeck,2)
    print_hand_and_score(name,player)
    print_hand_and_score("Dealer",dealer)
    hsp=player_hit_or_stand()
    if hsp ==True:
        player=cards.draw(bottomdeck,player)
        print("\nPlayer hits...")
    print_hand_and_score(name,player)
    hsd=dealer_hit_or_stand(player,dealer)
    if hsd == True:
        dealer=cards.draw(bottomdeck,dealer)
        print("\nDealer hits...")
    print_hand_and_score("Dealer",dealer)
    pscore=hand_score(player)
    dscore=hand_score(dealer)
    win_or_lose(pscore,dscore)

if __name__ ==  "__main__": #Name guard for test function.
    main()
    input()
