import nltk
nltk.download('wordnet')

words = ["eating", "eats", "eaten", "writing", "writes", "programming", "programs", "history", "finally", "finalized"]

# Q&A ; Chatsbots, Text summarization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

for word in words:
    print(word+"---->"+lemmatizer.lemmatize(word, pos='v'))