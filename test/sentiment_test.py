import text2emotion as te
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import flair

flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
text = "I've never been more bored"

sid = SentimentIntensityAnalyzer()
res = sid.polarity_scores(text)
# key, value = max(res.items(), key=lambda x: x[1])

s = flair.data.Sentence(text)
flair_sentiment.predict(s)
total_sentiment = s.labels
# key = total_sentiment[0].value
# value = total_sentiment[0].score

t2em = te.get_emotion(text)
key, value = max(t2em.items(), key=lambda x: x[1])

model_dict = {}
score = res["compound"]
if score >= 0.05:
    model_dict["Vader"] = {"Emotion": "Positive", 'Score': score}
elif -0.05 < score < 0.05:
    model_dict["Vader"] = {"Emotion": "Neutral", 'Score': score}
elif score <= -0.05:
    model_dict["Vader"] = {"Emotion": "Negative", 'Score': score}

model_dict["Flair"] = {"Emotion": str(total_sentiment[0].value).capitalize(), 'Score': total_sentiment[0].score}
if value == 0:
    model_dict["Text2emotion"] = {"Emotion": 'Neutral', 'Score': 1.00}
else:
    model_dict["Text2emotion"] = {"Emotion": key, 'Score': value}

print(model_dict)
# for item in model_dict.items():
#     if item[1]["Emotion"]
# print()
# print(key)
# print(value)
