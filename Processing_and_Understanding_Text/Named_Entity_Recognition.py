import pandas as pd
import spacy 
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from text_preprocessing import normalize_corpus

nlp = spacy.load('en_core_web_lg', parse=True, tag=True, entity=True)

tokenizer = ToktokTokenizer()
stopwords_list = nltk.corpus.stopwords.words('english')
stopwords_list.remove('no')
stopwords_list.remove('not')

news_df = pd.read_csv('news.csv')

sentence = str(news_df.iloc[1].full_text)
sentence_nlp = nlp(sentence)

corpus = normalize_corpus(news_df['full_text'], tokenizer, stopwords_list, text_lower_case=False, 
                          text_lemmatization=False, special_char_removal=False)

named_entities = []
for sentence in corpus:
    temp_entity_name = ''
    temp_named_entity = None
    sentence = nlp(sentence)
    for word in sentence:
        term = word.text 
        tag = word.ent_type_
        if tag:
            temp_entity_name = ' '.join([temp_entity_name, term]).strip()
            temp_named_entity = (temp_entity_name, tag)
        else:
            if temp_named_entity:
                named_entities.append(temp_named_entity)
                temp_entity_name = ''
                temp_named_entity = None

entity_frame = pd.DataFrame(named_entities, 
                            columns=['Entity Name', 'Entity Type'])

top_entities = (entity_frame.groupby(by=['Entity Name', 'Entity Type'])
                           .size()
                           .sort_values(ascending=False)
                           .reset_index().rename(columns={0 : 'Frequency'}))
