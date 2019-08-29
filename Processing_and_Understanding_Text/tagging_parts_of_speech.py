import pandas as pd
import nltk
import spacy
from nltk.tokenize.toktok import ToktokTokenizer
from text_preprocessing import normalize_corpus

nlp = spacy.load('en_core_web_lg', parse=True, tag=True, entity=True)

tokenizer = ToktokTokenizer()
stopwords_list = nltk.corpus.stopwords.words('english')
stopwords_list.remove('no')
stopwords_list.remove('not')

news_df = pd.read_csv('news.csv')

corpus = normalize_corpus(news_df['full_text'], tokenizer, stopwords_list, text_lower_case=False, 
                                                text_lemmatization=False, special_char_removal=False)
sentence = str(news_df.iloc[1].news_headline)
sentence_nlp = nlp(sentence)

spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in sentence_nlp]

nltk_pos_tagged = nltk.pos_tag(sentence.split())
