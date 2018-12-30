import nltk

text = "This is Andrew's text, isn't it ?"

tokenizer = nltk.tokenize.WhitespaceTokenizer()
text_tokenized = tokenizer.tokenize(text)
print(text_tokenized)

tokenizer = nltk.tokenize.TreebankWordTokenizer()
text_tokenized = tokenizer.tokenize(text)
print(text_tokenized)

tokenizer = nltk.tokenize.WordPunctTokenizer()
text_tokenized = tokenizer.tokenize(text)
print(text_tokenized)
