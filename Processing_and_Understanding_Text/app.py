from data_retrieval import build_dataset

seed_urls = ['https://inshorts.com/en/read/technology',
             'https://inshorts.com/en/read/sports',
             'https://inshorts.com/en/read/world']

news_df = build_dataset(seed_urls)
print(news_df.head(10))