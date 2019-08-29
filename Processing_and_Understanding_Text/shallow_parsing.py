from nltk.corpus import conll2000
from nltk.chunk.util import tree2conllstr, conlltags2tree

data = conll2000.chunked_sents()

train_data = data[:10900]
test_data = data[10900:]

wtc = tree2conllstr(train_data[1])
print(wtc)

tree = conlltags2tree(wtc)