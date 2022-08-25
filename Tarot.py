# Tarot.py
import Deck as deck
import random as random
#generates a global list for the given hand. 
def main():
    fivecardspread()


def fivecardspread():
    hand = []
    for count in range(5):
        pick = random.randrange(0, 78)
        hand.append(deck.Card[pick])
        count += 1
    print(f"\n1.{hand[0][0]} 2.{hand[1][0]} 3.{hand[2][0]} 4.{hand[3][0]} 5.{hand[4][0]} \n")

    print(
        f"\n First Card : Past : {hand[0][0]} : \nIn this position the card represents people and situations of the past... \n{hand[0][1]}")

    print(
        f"\n Second Card : Present : {hand[1][0]} : \nA card present in this position represents the people and situations in your current life... \n{hand[1][1]}")

    print(
        f"\n Third Card : Future : {hand[2][0]} : \nThe Future card represents situations and relationships to come... \n{hand[2][1]}")

    print(
        f"\n Fourth Card : Outcome : {hand[3][0]} : \nThis is the result of all the other cards combined... \n{hand[3][1]}")

    print(
        f"\n Fifth Card : Modifier : {hand[4][0]} : \nThe final card is in support of the outcome as a modifier card... \n{hand[4][1]}")

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Fortune cannot be read : {error}")