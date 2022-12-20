

class GameOfHangman():
    def __init__(self):
        # what vars go in here  
        global numFailed
        numFailed=0
        global lettersGuessed
        lettersGuessed =[]
        global phrase
        global coded
        phrase = input("What phrase would you like the player to guess?\n")
        phrase = phrase.lower()
        coded = []
        for i in range(len(phrase)): # Codes the phrase 
            if phrase[i] != " ":
                coded.append("_")
            else:
                coded.append(" ")
        coded = (''.join(coded))
        print("\n"+coded)
        return
    def play(self):
            hangingMan = [
            ["__________"],
            ["|        |"],
            ["|         "],
            ["|         "],
            ["|         "],
            ["|         "],
            ["|         "],
            ["|_________"]
            ]
            for row in hangingMan:  # Renders
                for content in row: 
                    print(content)
            while (numFailed !=6):
                GameOfHangman.play_turn(numFailed)
            return 
    def render(self,numFailed):
        if numFailed ==6:
            hangingMan = [
            ["__________"],
            ["|        |"],
            ["|        O"],
            ["|       /|\\"],
            ["|        |"],
            ["|        /\\"],
            ["|"],
            ["|_________"]
        ]
        elif numFailed == 5:
            hangingMan = [
            ["__________"],
            ["|        |"],
            ["|        O"],
            ["|       /|\\"],
            ["|        |"],
            ["|        /"],
            ["|"],
            ["|_________"]
        ]
        elif numFailed == 4:
            hangingMan = [
            ["__________"],
            ["|        |"],
            ["|        O"],
            ["|       /|\\"],
            ["|        |"],
            ["|         "],
            ["|"],
            ["|_________"]
        ]
        elif numFailed == 3:
            hangingMan = [
            ["__________"],
            ["|        |"],
            ["|        O"],
            ["|       /|"],
            ["|        |"],
            ["|         "],
            ["|         "],
            ["|_________"]
        ]
        elif numFailed == 2:
            hangingMan = [
            ["__________"],
            ["|        |"],
            ["|        O"],
            ["|        |"],
            ["|        |"],
            ["|         "],
            ["|         "],
            ["|_________"]
        ]
        elif numFailed == 1:
            hangingMan = [
            ["__________"],
            ["|        |"],
            ["|        O"],
            ["|         "],
            ["|         "],
            ["|         "],
            ["|         "],
            ["|_________"]
        ]
        elif numFailed == 0:
            hangingMan = [
            ["__________"],
            ["|        |"],
            ["|         "],
            ["|         "],
            ["|         "],
            ["|         "],
            ["|         "],
            ["|_________"]
        ]
        for row in hangingMan:  # Renders
           for content in row: 
                print(content)
        return
    def play_turn(self):
       if coded.lower() == phrase.lower():
        GameOfHangman.end()
       newInput=input("What letter would you like to guess?\n")
       lettersGuessed.append(newInput)
       Location = GameOfHangman.find(phrase,newInput)
       if Location == []:
        numFailed=+1
       else:
        for i in Location:
            coded.replace(newInput,coded(i))    

       GameOfHangman.render(numFailed)
       print(coded)
       return numFailed
    
    def exit(self):
        if numFailed == 6:
            print("The correct phrase was "+ phrase)
        else:
            print("You guessed the phrase right! You win!")
                   
        return 
    
    @staticmethod
    def find(str, ch):
        for i, ltr in enumerate(str):
            if ltr == ch:
                yield i



def main():
    game = GameOfHangman()
    game.play()

# # Stages Function
# def visual(numFailed):
    
#     if numFailed ==6:
#         hangingMan = [
#             ["__________"],
#             ["|        |"],
#             ["|        O"],
#             ["|       /|\\"],
#             ["|        |"],
#             ["|        /\\"],
#             ["|"],
#             ["|_________"]
#         ]
#     elif numFailed == 5:
#         hangingMan = [
#             ["__________"],
#             ["|        |"],
#             ["|        O"],
#             ["|       /|\\"],
#             ["|        |"],
#             ["|        /"],
#             ["|"],
#             ["|_________"]
#         ]
#     elif numFailed == 4:
#         hangingMan = [
#             ["__________"],
#             ["|        |"],
#             ["|        O"],
#             ["|       /|\\"],
#             ["|        |"],
#             ["|         "],
#             ["|"],
#             ["|_________"]
#         ]
#     elif numFailed == 3:
#         hangingMan = [
#             ["__________"],
#             ["|        |"],
#             ["|        O"],
#             ["|       /|"],
#             ["|        |"],
#             ["|         "],
#             ["|         "],
#             ["|_________"]
#         ]

#     elif numFailed == 2:
#         hangingMan = [
#             ["__________"],
#             ["|        |"],
#             ["|        O"],
#             ["|        |"],
#             ["|        |"],
#             ["|         "],
#             ["|         "],
#             ["|_________"]
#         ]
#     elif numFailed == 1:
#         hangingMan = [
#             ["__________"],
#             ["|        |"],
#             ["|        O"],
#             ["|         "],
#             ["|         "],
#             ["|         "],
#             ["|         "],
#             ["|_________"]
#         ]
#     elif numFailed == 0:
#         hangingMan = [
#             ["__________"],
#             ["|        |"],
#             ["|         "],
#             ["|         "],
#             ["|         "],
#             ["|         "],
#             ["|         "],
#             ["|_________"]
#         ]
#     return hangingMan
# def render(hangmanStructure):
#     for row in hangmanStructure:
#         for content in row: 
#             print(content)
#     return  




# def passPhraseCleaner():
#     global phrase
#     global coded
#     phrase = input("What is the phrase you would like for the player to guess\n")
#     phrase = phrase.upper()
#     coded = []
#     for i in range(len(phrase)):
#         if phrase[i] != " ":
#             coded.append("_")
#         else:
#             coded.append(" ")
#     return ''.join(coded)
# def find(str, ch):
#     for i, ltr in enumerate(str):
#         if ltr == ch:
#             yield i
# def guessCheck():
#     location=[]
#     guess=input("What letter would you like to guess?\n")
#     guess=guess.upper()
#     location=list(find(phrase,guess))
#     if location != []:
#         for i in location:
#             coded.replace(coded[i],guess)        
#     else:
#         numFailed+=1
#     return
# def main():
#     print(list(find(str,""))) 
#     #print(passPhraseCleaner())
#     #render(visual(6))
#     return 

if __name__ == '__main__':
    main()