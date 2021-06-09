import random
import math


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
dealHand = []
playing = True
playerHand = []
playerMoney = 1000

def default():
    pass

def shuffle(alist):
    deck = random.shuffle(alist)

def placeBets():
    print("Your Total Is ", playerMoney)
    bet = int(input("How much would you like to bet?"))
    print("Your Total Is Now ", playerMoney-bet)
    

def dealCards():
    shuffle(deck)
    for card in deck[:2]:
        #print(card, end=" ")
        dealHand.append(card)
        deck.pop(deck.index(card))
    for card in deck[:2]:
        #print(card, end=" " )
        playerHand.append(card)
        deck.pop(deck.index(card))

    print("Dealer's Hand Cards: ", dealHand)
    print("Dealer's Hand Total:" , )
    print("Your Hand Cards: ", playerHand)

def score(card):
    if card == 11:
        card = "A"
        
    if card == 12:
        card = "J"

    if card == 13:
        card = "Q"

    if card == 14:
        card = "K"


def playAgain():
    play=input("Would You Like to Play Again? Y/N: ").lower()
    if play == "y":
        dealHand.clear()
        playerHand.clear()
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
    if play == "n":
        playing = False
        print("Thanks For Playing!")
        print("Have a Nice Day :)")
        print("Money: ", playerMoney)
        exit()

    

def main():
    while(playing == True or playerMoney > 0):
        placeBets()
        dealCards()
        playAgain()

if __name__ == '__main__':
    main()
