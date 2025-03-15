# Word Scramble

import random

def show_rules():
    print("These are the rules : ")
    print("1. You will have 4 rounds in this game")
    print("2. If you guess the correct word then you will get 1 point")
    print("3. If you didn't guess the correct word then you will get 0 point")
    print("Best of luck!!!")


def startgame():
    words_tuple = ("Developer","mouse","Laptop","screen","basic","computer","ooty")

    Usedword = set()
    points = 0
    i=1
    while i<5:
        word = random.choice(words_tuple)
        word = word.upper()

        if word in Usedword:
            continue

        Usedword.add(word)
        computer_word = word
        # sample ->
        # "CODER"-> "ODERC"
        word = '|'.join(random.sample(word,len(word))) # O|D|E|R|C

        print(f"ROUND - {i}")
        print(word)

        user_word = input("Guess the word : ")

        if user_word.upper()==computer_word:
            points+=1
            print("You guess correct word.")
        else:
            print("You didn't guess the correct word. The word was : ",computer_word)
        print("Your score is : ",points)
        print()
        i+=1
    print("4 rounds has completed")
    print("Your final score is : ", points)
    print("Thanks for playing this game.")

def main():
    show_rules()

    inp = input("Enter any key except (n/N) to start the game : ")

    if inp in ('n',"N"):
        print("You don't want to start the game")
        return

    startgame()


main()