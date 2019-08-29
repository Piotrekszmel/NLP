from data_retrieval import build_dataset
from nltk.tokenize.toktok import ToktokTokenizer
import nltk
import spacy
import pandas as pd
import numpy as np
from text_preprocessing import normalize_corpus

tokenizer = ToktokTokenizer()
stopwords_list = nltk.corpus.stopwords.words('english')
stopwords_list.remove('no')
stopwords_list.remove('not')

seed_urls = ['https://inshorts.com/en/read/technology',
             'https://inshorts.com/en/read/sports',
             'https://inshorts.com/en/read/world']

news_df = build_dataset(seed_urls)

news_df['full_text'] = news_df['news_headline'].map(str)+ ' ' + news_df['news_article']
news_df['clean_text'] = normalize_corpus(news_df['full_text'], tokenizer=tokenizer, stopword_list=stopwords_list)
norm_corpus = list(news_df['clean_text'])

news_df.to_csv('news.csv', index=False, encoding='utf-8')


