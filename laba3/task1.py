inputString = input("InputString = ")
row = inputString[0: inputString.index(".")]
words = row.split(" ")
maxWordLength = len(words[0])
minWordLength = len(words[0])
for word in words:
    if len(word) > maxWordLength:
        maxWordLength = len(word)
    if len(word) < minWordLength:
        maxWordLength = len(word)
changedRow = row.replace("*", "")
finalRow = [None] * len(changedRow) * 2
for i in range(len(changedRow)):
    curr = changedRow[i]
    finalRow[i * 2] = curr
    finalRow[i * 2 + 1] = curr
print("row length " + str(len(row)))
print("max word length " + str(maxWordLength))
print("min word length " + str(minWordLength))
print("final row " + "".join(finalRow))
