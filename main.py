import random
import os
from art import logo
import emoji

def blackJack():
    """Math and info used for blackJack"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer = []
    player = []
    playerTotal = 0 
    dealerTotal = 0 


    
    def endOfGame(loss, playerTotal):
        """Compiles information from game and determines result of the game"""
        print(f"Final Score | Dealer {dealer} Total: {dealerTotal} | You {player} Your Total: {playerTotal}")

        if loss == True and playerTotal > 21:
            print(emoji.emojize(f'You went over 21 :crying_cat_face:', language='alias'))
        elif loss == True:
            print(emoji.emojize('The dealer beat you :crying_cat_face:', language='alias'))
        elif loss == False and dealerTotal > 21:
            print("Dealer went over! ")
        elif loss == False:
            print("You won!! Congrats")
        elif loss == None:
            print("It's a Tie!!")
        if (input("Would you like to play again? y/n ")) == 'y':
            os.system('cls')
            blackJack()

    def winnerOrLoser(playerTotal, dealerTotal):
        if playerTotal > dealerTotal:
            endOfGame(loss=False, playerTotal=playerTotal)
        elif playerTotal < dealerTotal:
            endOfGame(loss=True, playerTotal=playerTotal)
        elif playerTotal == dealerTotal:
            endOfGame(None, playerTotal=playerTotal)        
    
    
    for i in range(0, 2):
        dealerCardPick = random.choice(cards)
        playerCardPick = random.choice(cards)
        dealer.append(dealerCardPick)
        player.append(playerCardPick)
        playerTotal += playerCardPick
        dealerTotal += dealerCardPick
        #print(f'Dealer: {dealerCardPick} | Player: {playerCardPick}')


    #print(f'Dealer\'s First card: {dealer[0]} | Player: {player} | Your Total: {playerTotal}')
    #continuePickingCards = False
    while not playerTotal > 21:
        print(f"Final Score | Dealer {dealer} Total: {dealerTotal} | You {player} Your Total: {playerTotal}")

        hitAgain = input("Would you like to take another card y/n: ").lower()
        if hitAgain == 'y':
            afterFirstPick = random.choice(cards)
            player.append(afterFirstPick)
            playerTotal += afterFirstPick
            if playerTotal <= 21: 
                print(f'Dealer\'s First card: {dealer[0]} | Player: {player} | Your Total: {playerTotal}')
            elif playerTotal > 21:
                if 11 in player:
                    aceIndex = player.index(11)
                    player.pop(aceIndex)
                    player.insert(aceIndex, 1) 
                    playerTotal -= 10
                    print("You went over 21, your ace was turned to a 1!")
                    continue
                endOfGame(loss=True, playerTotal=playerTotal)
            #come back to figureout

        elif hitAgain == 'n':    
            while dealerTotal < 17:
                dealerPickAgain = random.choice(cards)
                dealer.append(dealerPickAgain)
                dealerTotal += dealerPickAgain
            if dealerTotal > 21:
                endOfGame(loss=False, playerTotal=playerTotal)   
            else:
                winnerOrLoser(playerTotal, dealerTotal)


        else:

            print("Invalid Input")
            continue
           # print(f'Dealer\'s First card: {dealer[0]} | Player: {player} | Your Total: {playerTotal}')

        
        

            
askToPlay = input("Would you like to play blackjack y/n: ")
if askToPlay == 'y':
    print(logo)
    blackJack()


