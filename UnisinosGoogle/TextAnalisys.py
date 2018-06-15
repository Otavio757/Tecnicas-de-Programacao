# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# part-of-speech tags from enums.PartOfSpeech.Tag
pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

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

def syntax_text():
    """Detects syntax in the text."""
        
    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens

    for token in tokens:
        print(u'{}: {}'.format(pos_tag[token.part_of_speech.tag], token.text.content))

def floresta_tagger():
    # import nltk.data
    # tagger = nltk.data.load("taggers/NAME_OF_TAGGER.pickle")
    from nltk.corpus import floresta
    tsents = floresta.tagged_sents()
    tsents = [[(w.lower(),simplify_tag(t)) for (w,t) in sent] for sent in tsents if sent]
    train = tsents[100:]
    test = tsents[:100]

def classify_text():
    """Classifies content categories of the provided text."""
    
    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' * 20)
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))

floresta_tagger()
