words = ["eating", "eats", "eaten", "writing", "writes", "programming", "programs", "history", "finally", "finalized"]

# Porter Stemmer
from nltk.stem import PorterStemmer
stemming = PorterStemmer()
print("###Porter Stemming###")
for word in words:
    print(word+"--->"+stemming.stem(word))

# Disadvantage of Stemming
disadvantage1 = stemming.stem('Congratulations')
disadvantage2 = stemming.stem('Sitting')
print(disadvantage1)
print(disadvantage2)

#RegexpStemmer class
from nltk.stem import RegexpStemmer
reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print("###Regex Stemming###")
for word in words:
    print(word+"--->"+reg_stemmer.stem(word))

# Snowball stemmer
from nltk.stem import SnowballStemmer
snowball = SnowballStemmer('english')
print("###Snowball Stemming###")
for word in words:
    print(word+"--->"+snowball.stem(word))

# Difference between Porter Stemmer and Snowball stemmer
a= stemming.stem("fairly"),stemming.stem("sportingly")
b = snowball.stem("fairly"),snowball.stem("sportingly")
print(a,b)


