from textblob import TextBlob

print("----- Sentiment Analysis Project -----")


text = input("Enter a sentence or review: ")


analysis = TextBlob(text)


polarity = analysis.sentiment.polarity


if polarity > 0:
    sentiment = "Positive 😊"
elif polarity < 0:
    sentiment = "Negative 😞"
else:
    sentiment = "Neutral 😐"


print("\nText:", text)
print("Polarity Score:", polarity)
print("Sentiment:", sentiment)
