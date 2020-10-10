import random
WORDLIST = 'wordlist.txt'

def fetchWord():
    wordprocessed = 0
    requireword = None
    with open(WORDLIST,'r') as wordfile:
        for text in wordfile:
            wordprocessed += 1
            if random.randint(1,wordprocessed)==1:
                requireword = text.strip('\n')
    return  requireword

