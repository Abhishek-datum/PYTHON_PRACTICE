#Task01:count word frequency sentence='python is fun and python is powerful'
sentence = "python is fun and python is powerful"
words=sentence.split()
wordCount={}
for word in words:
    wordCount[word]=wordCount.get(word,0)+1
print(wordCount)