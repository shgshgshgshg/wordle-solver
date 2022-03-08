#Read Words
file = open('/usr/share/dict/words', 'r')
words = file.readlines()
file.close()

current = 0
possible = []

while len(possible) != 158390:
    word = words[current].rstrip()
    if len(word) == 5:
        possible.append(word)
        current = current + 1
    else:
        current = current + 1
        continue

letter = input('Type a letter in word, regardless of position or capitalization: ')

num_checking = 0
word_checking = possible[num_checking]
still_possible = len(possible)

while num_checking != len(possible):
    if letter in word_checking:
        continue
    else:
        possible.pop(num_checking)