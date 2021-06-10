import random
import math


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]*4
dealHand = []
playing = True
playerHand = []
playerMoney = 1000

def default():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
    dealHand.clear()
    playerHand.clear()
    playing = True
    

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
    #return bet


def dealCards():
    shuffle(deck)

    for card in deck[:2]:
        dealHand.append(card)
        deck.pop(deck.index(card))
        
    for card in deck[:2]:
        deck.pop(deck.index(card))
        #@ts-ignore
        playerHand.append(card)

    print("Dealer's Hand Cards: ", dealHand)
    print("Your Hand Cards: ", playerHand)


def totalScore():
    playerMoney = 1000
    dealerTotal = 0
    playerTotal = 0
    
    for i in dealHand:
        if i == "J" or i == "Q" or i == "K":
            dealerTotal+= 10
        elif i == "A":
            if dealerTotal >= 11:
                dealerTotal+= 1
            else:
                dealerTotal+= 11
        else:
            dealerTotal = dealerTotal + i
    

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
    if playerTotal == 21:
        print("You Got Blackjack. You Win")
        playerMoney = playerMoney - bet
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

def dealerRules():
    if dealerTotal<=16:
        deck.append()
        


def playerInput():
    print(
        "Press 1 To Hit",
        "Press 2 To Stand",
    )
    action = int(input("Action To Perform:\n"))
    
    if(action == 1):
        print("HIT!")
        playerHand.append()
        

    



def scoreCheck():
    pass

def main():
    while(playing == True or playerMoney > 0):
        placeBets()
        dealCards()
        totalScore()
        scoreCheck()
        playAgain()

if __name__ == '__main__':
    main()
