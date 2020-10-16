from typing import Optional
from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import flair
# flair_sentiment = flair.models.TextClassifier.load('en-sentiment')


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

    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {"value": value,
                  "confidence": confidence,
                  "entity": "Sentiment",
                  "extractor": "sentiment_extractor"}

        return entity

    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""

        sid = SentimentIntensityAnalyzer()
        res = sid.polarity_scores(message.text)
        key, value = max(res.items(), key=lambda x: x[1])

        # s = flair.data.Sentence(message.text)
        # flair_sentiment.predict(s)
        # total_sentiment = s.labels
        # key = total_sentiment[0].value
        # value = total_sentiment[0].score
        entity = self.convert_to_rasa(key, value)

        message.set("entities", [entity], add_to_output=True)

    def persist(self, file_name, model_dir):
        """Pass because a pre-trained model is already persisted"""
        pass
