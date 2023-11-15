import nltk
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text = "The quick brown foxes jumped over the lazy dogs. Jumper's jumping."
words = word_tokenize(text)
porter = PorterStemmer()
lancaster = LancasterStemmer()
porter_stems = [porter.stem(word) for word in words]
lancaster_stems = [lancaster.stem(word) for word in words]
print("Original Words:", words)
print("Porter Stems:", porter_stems)
print("Lancaster Stems:", lancaster_stems)
