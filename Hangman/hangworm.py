#!/usr/bin/python 
import sys, string, random
wordlist =[]
class Hangworm():
    global wordlist
    try:
        filename = sys.argv[1]
        wordfile=open(filename,"r")
    except IOError:
        print "Can't find or open file!"
        exit()
    else:  
        for line in wordfile:
            wordlist.append(line[0:2])    
    def __init__(self):
        choice = raw_input("Would you like to play? (y/n): ")
        if choice == 'y':
            name = raw_input("What is your name? ")
            print "Hello, " + name + ". Time to play hangworm!\n"
            self.game()
        elif choice == 'n':
            print "Okay then, bye for now~"
            exit()
        else:
            print "Um, type 'y' or 'n' please."
            self.__init__()
    def game(self):
        guesses = 0
        letters_used = ''
        index = random.randint(0, len(wordlist)-1)
        word = wordlist[index]
        word_state = ['_','_']
        while guesses < 4:
            guess = raw_input("Guess a letter: ").lower()
            if len(guess) > 1:
                print "One letter only please."
                continue
            if guess in word and guess not in letters_used:
                print "Huh, you got one right."
                letters_used += guess
                self.graphic(guesses, word)
                self.word_set(guess, word, word_state)
                print "Word: " + "".join(word_state)
                print "Used Letters: " + letters_used
            elif guess not in word and guess not in letters_used:
                guesses += 1
                print "Oops, that wasn't right."
                letters_used += guess
                self.graphic(guesses,word)
                print "Word: " + "".join(word_state)
                print "Used Letters: " + letters_used
            else:
                print "Um, you already guessed that."
            if "".join(word_state) == word:
                print "You got it!"
                main()
                ##self.__init__()
    def graphic(self, guesses, word):
        if guesses == 0:
            print "_____     "
            print "|         "
            print "|         "
            print "|         "
            print "|         "
            print "|         "
            print "----------"
        elif guesses == 1:
            print "_____     "
            print "|   |     "
            print "|   O     "
            print "|         "
            print "|         "
            print "|         "
            print "----------"
        elif guesses == 2:
            print "_____     "
            print "|   |     "
            print "|   O     "
            print "|   |     "
            print "|         "
            print "|         "
            print "----------"
        elif guesses == 3:
            print "_____     "
            print "|   |     "
            print "|   O     "
            print "|   |     "
            print "|   |     "
            print "|         "
            print "----------"
        else:
            print "_____     "
            print "|   |     "
            print "|   O     "
            print "|   |     "
            print "|   |     "
            print "|   |     "
            print "----------"
            print "Game Over"
            print "The word was " + word
            print "I mean, I did call it hangworm..."
            main()
            ##self.__init__()
    def word_set(self, guess, word, word_state):
        i = 0
        while i < len(word):
            if guess == word[i]:
                word_state[i] = guess
                print word_state[i]
            i += 1
        return "".join(word_state)
    
class Coin():
    def __init__(self):
        choice = raw_input("Would you like to play? (y/n): ")
        if choice == 'y':
            self.game()
        elif choice == 'n':
            print "Okay then, bye for now~"
            exit()
        else:
            print "Um, type 'y' or 'n' please."
            self.__init__()
    def game(self):
        ht = raw_input("Heads or Tails (h/t)? ")
        comp_ht = random.randint(0,1)##0=heads, 1=tails
        if ht == 'h':
            ht_int = 0
        elif ht == 't':
            ht_int = 1
        else:
            print "Please picck heads or tails (h/t)."
            self.game()
        if ht_int == comp_ht:
            print "You won!"
        else:
            print "Nope, try again..."
        main()
        ##self.__init__()

        
def main():
    game_sel = raw_input("Select a game:\n (1)Hangworm\n (2)Coin Flip\n (3)Exit Program")
    if game_sel == '1':
        game = Hangworm()
    elif game_sel == '2':
        game = Coin()
    elif game_sel == '3':
        exit()
    else:
        print "Invalid choice"
        main()
if __name__ == "__main__":
    main()
