import pandas as pd

from newspaper import Article
from bs4 import BeautifulSoup

data = pd.read_csv('./wapo_work_advice.csv')

article_dates = data['Date'].to_numpy()
urls = data['Link'].to_numpy()

article_data = []

for index, url in enumerate(urls):
	article = Article(url, keep_article_html=True)
	article.download()

	soup = BeautifulSoup(article.html, 'html.parser')
	article_body = soup.find("div", {"class":"article-body"})

	remove_phrases = [
		'Reader 1:',
		'Reader 2:',
		'Subscribe today ArrowRight',
		'AdvertisementStory continues below',
		'advertisement'
	]
	final_text = article_body.text

	for phrase in remove_phrases:
		final_text = final_text.replace(phrase, " ")

	article_data.append([article_dates[index], final_text])

parsed_data = pd.DataFrame(article_data, columns=['date', 'body'])
parsed_data.to_csv('wapo_data.csv')

