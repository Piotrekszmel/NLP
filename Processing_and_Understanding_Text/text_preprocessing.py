import spacy
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
import re
from bs4 import BeautifulSoup
import contractions
import unicodedata

nlp = spacy.load('en_core_web_lg', parse=True, tag=True, entity=True)

def strip_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    print(soup)
    stripped_text = soup.get_text()
    return stripped_text


def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text


def expand_contractions(text):
    text = contractions.fix(text)
    return text


def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-Z0-9\s]' if not remove_digits else r'[^a-zA-Z\s]'
    text = re.sub(pattern, '', text)
    return text


def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON' else word.text for word in text])
    print(type(text))
    return text


lemmatize_text("My system keeps crashing! his crashed yesterday, ours crashes daily")


def simple_stemmer(text):
    ps = nltk.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text

print(simple_stemmer("My system keeps crashing his crashed yesterday, ours crashes daily"))

print(' '.join([1, 2, 3]))
print(' '.join([1, 2, 3]))
