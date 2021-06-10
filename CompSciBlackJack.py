import random
import math


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]*4
dealHand = []
playing = True
playerHand = []
playerMoney = 1000
bet = 0
dealerTotal = 0
playerTotal = 0


def default():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]*4
    dealHand.clear()
    playerHand.clear()
    playing = True
    

def shuffle(alist):
    deck = random.shuffle(alist)

def placeBets():
    global bet
    error = True
    while(error == True):
        try:
            print("Your Total Is ", playerMoney)
            bet = int(input("How much would you like to bet?"))
            if bet >= playerMoney:
                print("You Are All In")
                print("You Have Bet ", playerMoney )
                bet = playerMoney
            print("Your Total Is Now ", playerMoney - bet,"\n")
            error = False
        except:
            error == True
    


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
    global bet
    global dealerTotal
    global playerTotal
    global playerMoney
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
    if playerTotal <= 21 and dealerTotal <= 21:        
        if playerTotal == 21:
            print("You Got Blackjack. You Win")
            playerMoney = playerMoney + bet
        elif dealerTotal == 21:
            print("The Dealer Got Blackjack. You Lose")
            playerMoney = playerMoney - bet
        else:
            if dealerTotal >= playerTotal:
                print("The Dealer Wins. You Lose")
                playerMoney = playerMoney - bet
            elif playerTotal > dealerTotal:
                print("You Win")
                playerMoney = playerMoney + bet
    else:
        if playerTotal > 21:
            print("You Busted. You Lose")
        else: 
            print("The Dealer Busted. You Win!!")
    print("Dealer Total: ", dealerTotal)
    print("Player Total: ", playerTotal)
    print(playerMoney)
    

        

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
    while dealerTotal <= 16:
        dealHand.append(deck[0])
        deck.pop(0)
        print(dealHand)
        totalScore()
        


def playerInput():
    print(
        "Press 1 To Hit\n",
        "Press 2 To Stand",
    )
    action = int(input("Action To Perform:\n"))
    if playerMoney > 20:
        if(action == 1):
            print("HIT!")
            playerHand.append(deck[0])
            print("You Got: ", playerHand)
            deck.pop(0)
        elif(action == 2):
            print("You Stood At ", playerTotal)
        totalScore()
            

    



def scoreCheck():
    pass

def main():
    while(playing == True or playerMoney > 0):
        placeBets()
        dealCards()
        totalScore()
        dealerRules()
        playerInput()
        scoreCheck()
        playAgain()
        

if __name__ == '__main__':
    main()
