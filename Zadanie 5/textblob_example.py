from textblob import TextBlob

text = "Python is an amazing programming language. I love it!"
blob = TextBlob(text)

print("Sentiment:", blob.sentiment)

print("POS Tags:", blob.tags)

print("Words:", blob.words)