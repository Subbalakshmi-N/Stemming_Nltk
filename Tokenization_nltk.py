corpus = """Hello, Welcome to my Github account.
Please do follow my account! you'll become expert in NLP.
"""
print(corpus)

## Paragraph -> Sentence
from nltk.tokenize import sent_tokenize
documents = sent_tokenize(corpus)
type(documents)
for sentence in documents:
    print(sentence)

## Sentence to words
from nltk.tokenize import word_tokenize
words = word_tokenize(corpus)
for word in words:
    print(word)

from nltk.tokenize import wordpunct_tokenize
words = word_tokenize(corpus)
for word in words:
    print(word)

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
output = tokenizer.tokenize(corpus)
for word in output:
    print(word)

