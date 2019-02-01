from textblob import TextBlob

def Analyze(msg):
    w=TextBlob(msg)
    return w.sentiment.polarity

#m = input("Enter text:")
#print("Sentiment polarity of given text is:"+ str(Analyze(m)))