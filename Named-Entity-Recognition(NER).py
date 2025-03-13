import nltk
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')


sentence = """The Eiffel Tower was built from 1887 by French engineer Gustave Eiffel, whose company
specialized in building metal frameworks and structures."""

words = nltk.word_tokenize(sentence)
pos_tag = nltk.pos_tag(words)
ne = nltk.ne_chunk(pos_tag).draw()


