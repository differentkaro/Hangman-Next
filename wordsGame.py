import words
import random

#declaring variableS
wordsToGuess = ["seven", "world", "about", "again", "heart", "pizza", "water", "happy", "sixty", "board",
                "month", "angel", "death", "green", "music", "fifty", "three", "party", "piano", "mouth", "woman", "sugar",
                "amber", "dream", "apple", "laugh", "tiger", "faith", "earth", "river", "money", "peace", "forty", "smile", "abate", "house", "alone",
                "watch", "lemon", "south", "erica", "anime", "after", "santa", "stone", "china", "blood"]
score = 0
life = 5
picture0 = """
          =============================================
          ░█──░█ ░█▀▀▀█ ░█─░█ 　 ░█──░█ ░█▀▀▀█ ░█▄─░█ █ 
          ░█▄▄▄█ ░█──░█ ░█─░█ 　 ░█░█░█ ░█──░█ ░█░█░█ ▀ 
          ──░█── ░█▄▄▄█ ─▀▄▄▀ 　 ░█▄▀▄█ ░█▄▄▄█ ░█──▀█ ▄
          =============================================
"""
picture1 = """
       +----+ =========================================================
       |    ┃  ░█▀▀█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀ 　 ░█▀▀▀█ ░█──░█ ░█▀▀▀ ░█▀▀█ █ 
       O    ┃  ░█─▄▄ ░█▄▄█ ░█░█░█ ░█▀▀▀ 　 ░█──░█ ─░█░█─ ░█▀▀▀ ░█▄▄▀ ▀ 
      /|\   ┃  ░█▄▄█ ░█─░█ ░█──░█ ░█▄▄▄ 　 ░█▄▄▄█ ──▀▄▀─ ░█▄▄▄ ░█─░█ ▄ 
      / \   ===========================================================
            ┃
    =========
"""


#main code

print("""
          =======================================================
          F.I.V.E  L.E.T.T.E.R                              V1.05
          =======================================================
         ░█─░█ ─ ─█▀▀█ ─ ░█▄─░█ ─ ░█▀▀█ ─ ░█▀▄▀█ ─ ─█▀▀█ ─ ░█▄─░█ 
         ░█▀▀█ ▄ ░█▄▄█ ▄ ░█░█░█ ▄ ░█─▄▄ ▄ ░█░█░█ ▄ ░█▄▄█ ▄ ░█░█░█ 
         ░█─░█ █ ░█─░█ █ ░█──▀█ █ ░█▄▄█ █ ░█──░█ █ ░█─░█ █ ░█──▀█
         ========================================================
         """)
#welcome texts
print("welcome to the five letter Hangman guessing game!")
print("You would be given a defination of a 5 letter word and youll have to guess all 5 possible letters that could be found in the word")
print("you get one(1) point on correctly getting each letter and get and extra life at the completion of each word")
print("by default you have 0 score and 5 lives. enter \"exit\" to exit at any point of the game")
with open('score.txt', 'r') as high:
    highScore = int(high.read())
    print("Your High Score is ", highScore)
while "true": #main game starts here
    option = input("\nenter \"start\" to start or \"exit\" to exit or \"reset\" to reset your high score \n")
    if option.lower() == "start":
        selectedWord = ""
        used = [""]
        while "true":
            if len(used) <= 47:
                if life < 1:
                    score = 0
                    life = 5
                    break
                else:
                    while selectedWord in used:
                        selectedWord = random.choice(wordsToGuess)
                    used.append(selectedWord)
                    print("Guess the possible letters found in the word with the defination:", words.meaning(selectedWord))
                    chosen = [""]
                    blanks = "_" * 5
                    while "true":
                        if life < 1:
                            print(picture1)
                            print("Game Over! Sorry you have no lifes left. The correct answer is", selectedWord)
                            if score > highScore:
                                with open('score.txt', 'r+') as high:
                                    high.write(str(score))
                                highScore = score
                                print("You Have a new High Score!")
                            print("your score is ", score)
                            print("play again?")
                            break
                        if len(chosen) >= 6:
                            break
                        else:
                            print(blanks)
                            answer = input()
                            answer = answer.lower()
                            if answer == "exit":
                                print("Hangman would now exit...")
                                exit()
                            else:
                                if len(answer) != 1:
                                    print("sorry! try again, please enter one letter only")
                                elif answer not in "abcdefghijklmnopqrstuvwxyz":
                                    print("sorry! try again, please enter a letter")
                                else:
                                    if answer in chosen:
                                        print("letter has been entered previously, enter a new letter")
                                    else:
                                        for i in range(5):
                                            if selectedWord[i] in answer:
                                                blanks = blanks[:i] + selectedWord[i] + blanks[i + 1:]
                                        if answer in selectedWord:
                                            score += 1
                                            if len(chosen) >= 5:
                                                if score == 4:
                                                    score += 1
                                                life += 1
                                                print("Congratulations! you finished this word, your score is", score,
                                                      " and you now have", life, " life! Try out the next word!")
                                                chosen.append(answer)
                                            else:
                                                if blanks == selectedWord:
                                                    score += 1
                                                    life += 1
                                                    print("Congratulations! you finished this word", selectedWord,
                                                          "your score is", score, " and you now have", life,
                                                          " life! Try out the next word!")
                                                    chosen.append(answer)
                                                    chosen.append(answer)
                                                else:
                                                    print("that is correct!, your score is", score,
                                                          ". now enter another possible letter")
                                                    chosen.append(answer)
                                        else:
                                            life -= 1
                                            if life > 0:
                                                print("that is wrong! you have", life, " life(s) left. Try again!")
            else:
                print(picture0)
                if score > highScore:
                    with open('score.txt', 'r+') as high:
                        high.write(str(score))
                    highScore = score
                    print("You Have a new High Score!")
                print("your score is ", score)
                print("Play again?")
                break
                
    elif option.lower() == "exit":
        print("Hangman would now exit...")
        exit()
    elif option.lower() == "reset":
        with open('score.txt', 'w') as high:
            high.write(' ')
        with open('score.txt', 'r+') as high:
            high.write('0')
        with open('score.txt', 'r') as high:
            resetHighScore = high.read()
            print("Your high score has been reset. Your new high score is ", resetHighScore)
    else:
        print("entry not understood, please try again!")
