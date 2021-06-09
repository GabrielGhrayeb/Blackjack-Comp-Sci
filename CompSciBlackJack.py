import random
import math


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]*4
dealHand = []
playing = True
playerHand = []
playerMoney = 1000
dealerTotal = 0
playerTotal = 0



def default():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
    dealHand.clear()
    playerHand.clear()
    playing = True
    playerMoney = 1000

def shuffle(alist):
    deck = random.shuffle(alist)

def placeBets():
    error = False
    while(error == True):
        try:
            print("Your Total Is ", playerMoney)
            bet = int(input("How much would you like to bet?"))
            if bet >= playerMoney:
                print("All In")
                bet = playerMoney
            print("Your Total Is Now ", playerMoney-bet)
            error = False
        except:
            error == True


def dealCards():
    shuffle(deck)

    for card in deck[:2]:
        # if card == 11:
        #     card = "A"
        
        # if card == 12:
        #     card = "J"

        # if card == 13:
        #     card = "Q"

        # if card == 14:
        #     card = "K"
                
        #print(card, end=" ")
        dealHand.append(card)
        deck.pop(deck.index(card))

        # for royal in 
    #
    for card in deck[:2]:
        deck.pop(deck.index(card))
        #print(card, end=" " )
        playerHand.append(card)
        #deck.pop(deck.index(card))

    print("Dealer's Hand Cards: ", dealHand)
    print("Dealer's Hand Total:" , )
    print("Your Hand Cards: ", playerHand)

def score(card):
    pass

def totalScore():
    for i in dealHand:
        if i == "J" or i == "Q" or i == "K":
            dealerTotal+= 10
        elif i == "A":
            if dealerTotal >= 11:
                dealerTotal+= 1
            else:
                dealerTotal+= 11
        else:
            dealerTotal+= i

    for i in playerHand:
        if i == "J" or i == "Q" or i == "K":
            playerTotal+= 10
        elif i == "A":
            if playerTotal >= 11:
                playerTotal+= 1
            else:
                playerTotal+= 11
        else:
            playerTotal+= i
    print("Dealer Total: ", dealerTotal)
    print("Player Total: ", playerTotal)
        
def playAgain():
    play=input("Would You Like to Play Again? Y/N: ").lower()
    if play == "y":
        default()
    if play == "n":
        playing = False
        print("Thanks For Playing!")
        print("Have a Nice Day :)")
        print("Money: ", playerMoney)
        exit()

def scoreCheck():
    pass

def main():
    while(playing == True or playerMoney > 0):
        placeBets()
        dealCards()
        scoreCheck()
        playAgain()

if __name__ == '__main__':
    main()
