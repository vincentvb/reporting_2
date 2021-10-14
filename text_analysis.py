"""
Choose dataset when running script
example: DATA=ask_abby python text_analysis.py

Dataset options: ask_abby, nytimes, wapo
"""

import pandas as pd
import numpy as np
import os

from sklearn.feature_extraction.text import CountVectorizer

if os.environ.get('DATA') is None:
	raise Exception("Provide DATA environmental variable to run script")

data = {
	'ask_abby': pd.read_csv('./ask_abby.csv'),
	'nytimes': pd.read_csv('./nytimes_data.csv'),
	'wapo': pd.read_csv('./wapo_data.csv')
}[os.environ['DATA']]
data = data[data['body'].notna()]

def analyze_data(sliced_data):
	word_vectors = ''

	for index, body in enumerate(sliced_data['body'].to_numpy()):

		vectorizer = CountVectorizer(ngram_range=(1,1), stop_words='english')

		X = vectorizer.fit_transform([body])
		df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
		if index == 0:
			word_vectors = df
		else:
			word_vectors = word_vectors.merge(df, how='outer')

	word_vectors_with_metadata = word_vectors.merge(sliced_data['date'].reset_index(), left_index=True, right_index=True)
	# Display top 50 words
	print(word_vectors.sum().sort_values(ascending=False).head(n=50))

data['date'] = pd.to_datetime(data['date'])

before_pandemic = data[data['date'] < '2020-03-10']
after_pandemic = data[data['date'] > '2020-03-10']

analyze_data(before_pandemic)
analyze_data(after_pandemic)
