from wordshangman import fetchWord

class User:
    def __init__(self,name):
        self.name = name
    def welcome(self):
        print("Hello Mr. {} welcome to the pyhthon's HANGMAN".format(self.name))
    def startgame(self):
        correctlist = []
        word = fetchWord()
        answerlist = list(word)
        answerlist.sort()
        wordlength = len(word)
        numberofattempt = 2*wordlength
        print("Guess this word -> ","_"*wordlength)
        print()
        print("Number of attempt ->",'*'*numberofattempt)
        while numberofattempt>0:
            datainput = input("Enter your choice -> ")[0]

            if datainput in word:
                print("Very Good")
                correctlist.append(datainput)
            correctlist.sort()
            if correctlist == answerlist:
                print("Congrats {}..You guessed it right".format(self.name))
                print("The word is {}".format(word))
                break
            numberofattempt = numberofattempt-1
            print("Number of attempt ->",'*'*numberofattempt)
        if numberofattempt==0:
            print("Correct word is {}".format(word))


if __name__ == '__main__':
   name = input("Enter your name :- ")
   usr = User(name)
   usr.welcome()
   input("Press any key to start the game..")
   print()
   usr.startgame()