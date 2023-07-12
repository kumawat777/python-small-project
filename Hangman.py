from json.tool import main
import random
def Hangman():
    lst=["python","hangman"]
    word=random.choice(lst)
    guesses=""
    turns=10
    valid_entry="abcdfghijklmnoprstuvwxyz"
    while len(word)>0:
        main_word=""
        for char in word:
            if char in guesses:
                main_word=main_word+char
            else:
                main_word += "-"
        if main_word==word:
            print("you win")
            print( main_word)
            break
        print("the word is ", main_word)

        guess=input("enter a guess: ")
        if guess in valid_entry:
            guesses += guess
        else:
            print("write a valid character")
        
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left")
                print("-------------")
            
            if turns==8:
                print("8 turns left")
                print("-------------")
                print("     o      ")

            if turns==7:
                print(" 7 turns left")
                print("-------------")
                print("     o     ")
                print("     |     ")

            if turns==6:
                print(" 6 turns left")
                print("-------------")
                print("     o     ")
                print("     |     ")
                print("    /      ")

            if turns==5:
                print(" 5 turns left")
                print("-------------")
                print("     o     ")
                print("     |     ")
                print("    / \    ")

            if turns==4:
                print(" 4 turns left")
                print("-------------")
                print("    \o     ")
                print("     |     ")
                print("    / \    ")

            if turns==3:
                print(" 3 turns left")
                print("-------------")
                print("    \o/     ")
                print("     |     ")
                print("    / \    ")

            if turns==2:
                print(" 2 turns left")
                print("-------------")
                print("    \o/ |     ")
                print("     |     ")
                print("    / \    ")

            if turns==1:
                print(" only 1 turns left!!!! hangman on his last breath")
                print("-------------")
                print("    \o/_|    ")
                print("     |     ")
                print("    / \    ")

            if turns==0:
                print("you loose")
                print("you let a good man to die")   
                print("-------------")
                print("     o_|    ")
                print("    /|\    ")
                print("    / \    ")   
                break
    print("the wordd is ", word )
name=input("enter  name")
print("welcome", name)
Hangman()
            
        

            
                

   