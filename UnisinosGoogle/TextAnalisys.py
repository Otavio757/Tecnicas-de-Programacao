# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'Quero ir pra gravatai e estou em são leopoldo, como está o transito?'
document = language.types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT, language='pt')

def Sentimentos():
    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

def Entidades():
    response = client.analyze_entities(document, encoding_type='UTF32')
    for entity in response.entities:
        print('=' * 20)
        print('         name: {0}'.format(entity.name))
        print('         type: {0}'.format(entity.entity_type))
        print('     metadata: {0}'.format(entity.metadata))
        print('     salience: {0}'.format(entity.salience))


Entidades()
