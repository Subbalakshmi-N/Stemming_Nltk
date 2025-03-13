
# Text Pre-Processing with NLTK

This project demonstrates essential **Natural Language Processing (NLP)** techniques using the **Natural Language Toolkit (NLTK)** in Python. The key topics covered include:

- **Tokenization** (Splitting text into sentences and words)
- **Stemming** (Reducing words to their root form)
- **Lemmatization** (Reducing words to their dictionary base form)
- **Stopword Removal** (Filtering out common words)
- **POS Tagging** (Identifying parts of speech in text)

## 📌 Features
- Convert a **paragraph into sentences**.
- Convert **sentences into words**.
- Apply different **tokenizers**.
- Perform **stemming** using Porter, Regexp, and Snowball stemmers.
- Apply **lemmatization** for text normalization.
- Remove **stopwords** to clean text data.
- Identify **parts of speech (POS)** in sentences.

## 📜 Code Explanation

### 1️⃣ Tokenization
```python
from nltk.tokenize import sent_tokenize, word_tokenize, TreebankWordTokenizer

corpus = """Hello, Welcome to my Github account.
Please do follow my account! you'll become expert in NLP.
"""
print(corpus)

documents = sent_tokenize(corpus)
for sentence in documents:
    print(sentence)

words = word_tokenize(corpus)
for word in words:
    print(word)

tokenizer = TreebankWordTokenizer()
output = tokenizer.tokenize(corpus)
for word in output:
    print(word)
```
---

### 2️⃣ Stemming
#### **Porter Stemmer**
```python
from nltk.stem import PorterStemmer

words = ["eating", "writes", "programming", "history", "finalized"]
stemming = PorterStemmer()
for word in words:
    print(word + " ---> " + stemming.stem(word))
```

#### **Regexp Stemmer**
```python
from nltk.stem import RegexpStemmer

reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
for word in words:
    print(word + " ---> " + reg_stemmer.stem(word))
```

#### **Snowball Stemmer**
```python
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer('english')
for word in words:
    print(word + " ---> " + snowball.stem(word))
```

---

### 3️⃣ Lemmatization
```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
for word in words:
    print(word + " ---> " + lemmatizer.lemmatize(word, pos='v'))
```
---

### 4️⃣ Stopword Removal & Text Cleaning
```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

paragraph = """Dr. APJ Abdul Kalam often emphasized the importance of individual contributions..."""
stop_words = set(stopwords.words('english'))
words = word_tokenize(paragraph)
filtered_words = [word for word in words if word.lower() not in stop_words]
print(filtered_words)
```
---

### 5️⃣ POS Tagging
```python
from nltk import pos_tag

words = word_tokenize(paragraph)
pos_tags = pos_tag(words)
print(pos_tags)
```
---

## 🛠 Requirements
Ensure you have **NLTK** installed before running the script:
```bash
pip install nltk
```

To download necessary NLTK datasets, run:
```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
```

---

## 🚀 Run the Script
Simply execute the script in a Python environment:

---

## 📢 Follow Me!
If you found this project helpful, **star** 🌟 the repository and follow me on GitHub for more NLP projects!

Happy Coding! 🎯

