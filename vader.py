from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentences = ["VADER is smart, handsome, and funny.", "At least it isn't a horrible book."]

sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    print(ss['compound'])
