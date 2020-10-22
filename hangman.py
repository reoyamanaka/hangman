"""
book = open('words.txt', encoding="latin-1")
booktxt = book.readlines()
print(len(booktxt))
#print(booktxt[len(booktxt)-2])

wordList = []
with open('wordlist.txt', 'r') as rf:
    for line in rf:
        wordList.append(line)

words = open('wordlist.txt')
wordstxt = words.readlines()
print(wordstxt[len(wordstxt)-1])
"""

wordList = []

with open('wordlist.txt', 'r') as rf:
    for line in rf:
        if len(line) > 6 and len(wordList) < 100:
            wordList.append(line)
             
print(wordList)   
    
