import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')

paragraph = """Dr. APJ Abdul Kalam often emphasized the importance of individual contributions to 
societal change. For instance, he highlighted a "three-dimensional action plan" to combat corruption, 
involving parents and teachers as key influencers in shaping young minds1. He also outlined three visions
for India: freedom, development, and standing up to the world, emphasizing the need for self-confidence and 
strength in both military and economic spheres25. Kalam encouraged youth to dream big and work towards
making India a developed nation, urging them to ask what they could do for their country rather than what
their country could do for them4. His speeches were motivational, focusing on empowerment through 
education and innovation, and inspiring young minds to strive for excellence"""

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stopwords = stopwords.words('english')
print("No of stopwords:", len(stopwords))
print(stopwords)

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
stemmer = PorterStemmer()
sentences = nltk.sent_tokenize(paragraph)

## Apply stopwords and filter and then apply stemming
for i in range (len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word.lower() not in set(stopwords.words('english'))]
    sentences[i] = " ".join(words)
print(sentences)

## Apply stopwords and filter and then apply snowball stemming
from nltk.stem import SnowballStemmer
SnowballStemmer=SnowballStemmer('english')
for i in range (len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [SnowballStemmer.stem(word) for word in words if word.lower() not in set(stopwords.words('english'))]
    sentences[i] = " ".join(words)
print(sentences)

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
for i in range (len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word,pos ='v') for word in words if word.lower() not in set(stopwords.words('english'))]
    sentences[i] = " ".join(words)
print(sentences)

# Parts of speech tagging- we will find POS Tag
from nltk.corpus import stopwords
sentences = nltk.sent_tokenize(paragraph)
for i in range (len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [word for word in words if word.lower() not in set(stopwords.words('english'))]
    pos_tag = nltk.pos_tag(words)
    print(pos_tag)



