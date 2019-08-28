from data_retrieval import build_dataset
from nltk.tokenize.toktok import ToktokTokenizer
import nltk
import spacy

nlp = spacy.load('en_core', parse=True, tag=True, entity=True)

tokenizer = ToktokTokenizer()
stopwords_list = nltk.corpus.stopwords.words('english')
stopwords_list.remove('no')
stopwords_list.remove('not')

seed_urls = ['https://inshorts.com/en/read/technology',
             'https://inshorts.com/en/read/sports',
             'https://inshorts.com/en/read/world']

news_df = build_dataset(seed_urls)

