import nltk
nltk.data.path.append('D:/IA/Projets/NLP/nltk_data/')

text = "Feet cats wolves talked"

tokenizer = nltk.tokenize.TreebankWordTokenizer()
text_tokenized = tokenizer.tokenize(text)

stemmer = nltk.stem.PorterStemmer()
portStemmer = " ".join(stemmer.stem(word) for word in text_tokenized)
print(portStemmer)


stemmer = nltk.stem.WordNetLemmatizer()
wordLemmat = " ".join(stemmer.lemmatize(word) for word in text_tokenized)
print(wordLemmat)
