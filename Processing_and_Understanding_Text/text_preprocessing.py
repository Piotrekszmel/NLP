import spacy
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
import re
from bs4 import BeautifulSoup
import contractions
import unicodedata

def strip_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    print(soup)
    stripped_text = soup.get_text()
    return stripped_text

print(strip_html_tags('<html><h2>Some important text</h2></html>'))