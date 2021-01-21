from typing import Optional
from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import text2emotion as te
import flair

flair_sentiment = flair.models.TextClassifier.load('en-sentiment')


class SentimentAnalyzer(Component):
    """A pre-trained sentiment component"""

    name = "sentiment"
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(SentimentAnalyzer, self).__init__(component_config)

    def train(self, training_data, config: Optional[RasaNLUModelConfig] = None, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def convert_to_rasa(self, value):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {"value": value,
                  "entity": "Sentiment",
                  "extractor": "sentiment_extractor"}

        return entity

    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""

        sid = SentimentIntensityAnalyzer()
        res = sid.polarity_scores(message.text)
        key, value = max(res.items(), key=lambda x: x[1])

        s = flair.data.Sentence(message.text)
        flair_sentiment.predict(s)
        total_sentiment = s.labels

        t2em = te.get_emotion(message.text)
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

        entity = self.convert_to_rasa(model_dict)

        message.set("entities", [entity], add_to_output=True)

    def persist(self, file_name, model_dir):
        """Pass because a pre-trained model is already persisted"""
        pass
