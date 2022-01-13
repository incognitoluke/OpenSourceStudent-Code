from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

pd.set_option('display.max_colwidth', 0)
df = pd.read_csv("Data.csv", encoding='cp1252')

analyzer = SentimentIntensityAnalyzer()

negative = []
neutral = []
positive = []

for n in range(df.shape[0]):
    title = df.iloc[n,0]
    description = df.iloc[n, 2]
    title_analyzed = analyzer.polarity_scores(title)
    description_analyzed = analyzer.polarity_scores(description)
    negative.append(((title_analyzed['neg']) + (description_analyzed['neg']))/2)
    neutral.append(((title_analyzed['neu']) + (description_analyzed['neu'])) / 2)
    positive.append(((title_analyzed['pos']) + (description_analyzed['pos'])) / 2)
df["Negative"] = negative
df["Neutral"] = neutral
df["Positive"] = positive

pd.set_option('display.max_columns', None)
#print(df.head())

print(df["Negative"].mean())
print(df["Neutral"].mean())
print(df["Positive"].mean())
