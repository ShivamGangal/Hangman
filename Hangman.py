

class GameOfHangman():
    def __init__(self):
        # what vars go in here  
        # numFailed=0
        # self.numFailed = numFailed
        # lettersGuessed = []
        # self.lettersGuessed=lettersGuessed
        self.numFailed = 0
        self.lettersGuessed = [] # set or an array 
        self.guess_word = None 

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

    def update_word_mask(self,letter_locations, player_guess):
        # want a set of all unique characters 
        word_mask = list(self.masked_word)
        check_against = list(self.guess_word)
        for i in list(letter_locations):
            if check_against[i] == player_guess.upper():
                word_mask[i]=player_guess.upper()
            else:
                word_mask[i]=player_guess.lower()
        
        self.masked_word = ''.join(word_mask)
        

    def init_game(self):
        # intialize any necessary game state 

        guess_word = input("What phrase would you like the player to guess?\n")
        self.guess_word = guess_word
        #phrase = phrase.lower()
        masked_word = ['_' for i in range(len(self.guess_word))]
        self.masked_word = ''.join(masked_word)       
 

    def play(self):
            self.init_game()
            self.render()

            guessed_word_correctly = False 

            while (not guessed_word_correctly and  self.numFailed!=6):
                self.play_turn()
                guessed_word_correctly = self.guess_word.lower() == self.masked_word.lower()


            if guessed_word_correctly:
                print('You won!')
            else: 
                print('You lose')

        


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

        print('\n')

        print(self.masked_word)

        print("\n")

        # print out the lettters guessed at base of hangman
        for letter in self.lettersGuessed: 
            print(letter,end=' ')
        
        print('\n')

    def play_turn(self):
        # player can only guess a single letter at a time
        
        player_guess=input("What letter would you like to guess?\n")
        self.lettersGuessed.append(player_guess)
       
        if player_guess.lower() in self.guess_word.lower(): 
            letter_locations = GameOfHangman.find(self.guess_word.lower(),player_guess.lower()) 
            self.update_word_mask(letter_locations,player_guess)

        else: 
            self.numFailed +=1 
       
        self.render()

    
    @staticmethod
    def find(str, ch):
        for i, ltr in enumerate(str):
            if ltr == ch:
                yield i



def main():
    game = GameOfHangman()
    game.play()


if __name__ == '__main__':
    main()