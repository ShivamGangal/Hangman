

class GameOfHangman():
    def __init__(self):
        # what vars go in here  
        # numFailed=0
        # self.numFailed = numFailed
        # lettersGuessed = []
        # self.lettersGuessed=lettersGuessed
        self.numFailed = 0
        self.lettersGuessed = []
        self.guess_phrase = None 

        # coded = []
        # self.coded=coded
        # for i in range(len(self.guess_phrase)): # Codes the phrase 
        #     if self.guess_phrase[i] != " ":
        #         self.coded.append("_")
        #     else:
        #         self.coded.append(" ")
        # self.coded = (''.join(self.coded))
        # print("\n"+self.coded)
        # return

    def mask_phrase(self):
        # want a set of all unique characters 

        # if 
        return 
        

    def init_game(self):
        # intialize any necessary game state 

        guess_phrase = input("What phrase would you like the player to guess?\n")
        self.guess_phrase = guess_phrase
        #phrase = phrase.lower()

        self.masked_word = ['_' for i in len(self.guess_word)]

        return 

    def play(self):
            self.init_game()
            self.render()
            while ((self.coded.lower() == self.phrase.lower()) or self.numFailed==6):
                self.play_turn()
            return 


    def render(self):


        if self.numFailed ==6:
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
        elif self.numFailed == 5:
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
        elif self.numFailed == 4:
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
        elif self.numFailed == 3:
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
        elif self.numFailed == 2:
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
        elif self.numFailed == 1:
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
        elif self.numFailed == 0:
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
        for row in hangingMan:  # Renders Hangman structure 
           for content in row: 
                print(content)

        # print out the lettters guessed at base of hangman
        for letter in self.lettersGuessed: 
            print(letter,sep=' ')
        print('\n')


        return

    def play_turn(self):
    
       newInput=input("What letter would you like to guess?\n")
       self.lettersGuessed.append(newInput)
       
       #print(self.lettersGuessed)
       Location = GameOfHangman.find(self.phrase,newInput)
       if Location == []:
        self.numFailed=+1
       else:
        for i in Location:
            self.coded.replace(newInput,self.coded[int(i)])

       
       self.render()
       print(self.coded)
       return self.numFailed

    def exit(self):
        if self.numFailed == 6:
            print("The correct phrase was "+ self.guess_phrasephrase)
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