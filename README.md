# Stemming with NLTK

This code demonstrates how to perform **stemming** using the **Natural Language Toolkit (NLTK)** in Python. Stemming is the process of reducing words to their root form.

## 📌 Features
- Uses **Porter Stemmer**, **Regexp Stemmer**, and **Snowball Stemmer**.
- Compares different stemming techniques.
- Highlights the disadvantages of stemming.

## 📜 Code Explanation

### 1️⃣ Define Words for Stemming
```python
words = ["eating", "eats", "eaten", "writing", "writes", "programming", "programs", "history", "finally", "finalized"]
```
This list contains words that will be stemmed using different algorithms.

---

### 2️⃣ Porter Stemmer
```python
from nltk.stem import PorterStemmer

stemming = PorterStemmer()
print("###Porter Stemming###")
for word in words:
    print(word+"--->"+stemming.stem(word))
```
**Porter Stemmer** applies a series of rules to trim words down to their root form.

#### **Disadvantage of Porter Stemmer**
```python
disadvantage1 = stemming.stem('Congratulations')
disadvantage2 = stemming.stem('Sitting')
print(disadvantage1)
print(disadvantage2)
```
It sometimes produces incorrect root words.

---

### 3️⃣ RegexpStemmer
```python
from nltk.stem import RegexpStemmer

reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print("###Regex Stemming###")
for word in words:
    print(word+"--->"+reg_stemmer.stem(word))
```
This **RegexpStemmer** removes specific suffixes based on a regular expression pattern.

---

### 4️⃣ Snowball Stemmer
```python
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer('english')
print("###Snowball Stemming###")
for word in words:
    print(word+"--->"+snowball.stem(word))
```
**Snowball Stemmer** is an improved version of the Porter Stemmer with better accuracy.

---

### 5️⃣ Comparison: Porter vs. Snowball Stemmer
```python
a = stemming.stem("fairly"), stemming.stem("sportingly")
b = snowball.stem("fairly"), snowball.stem("sportingly")
print(a, b)
```
Snowball Stemmer often produces better results than Porter Stemmer.

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
```

---

## 🚀 Run the Script
Simply execute the script in a Python environment:
```bash
python stemming.py
```

---

## 📢 Follow Me!
If you found this code helpful, **star** 🌟 the repository and follow me on GitHub for more NLP projects!

Happy Coding! 🎯

