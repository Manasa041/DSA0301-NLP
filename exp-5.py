import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
porter_stemmer = PorterStemmer()
words = ["running", "easily", "jumps", "happily", "cats", "better"]
stemmed_words = [porter_stemmer.stem(word) for word in words]
print("Original words:", words)
print("Stemmed words:", stemmed_words)
