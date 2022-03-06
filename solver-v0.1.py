#Read Words
file = open('/usr/share/dict/words', 'r')
words = file.readlines()
file.close()

current = 0
possible = []

while len(possible) != 10:
    word = words[current].rstrip()
    if len(word) == 5:
        possible.append(word)
        current = current + 1
    else:
        current = current + 1
        continue
