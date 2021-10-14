import pandas as pd
import re

from newspaper import Article
from bs4 import BeautifulSoup

twenty_nineteen_months = {
	'08': range(1, 3),
	'09': range(1, 31),
	'10': range(1, 32),
	'11': range(1, 31),
	'12': range(1, 32)
}

twenty_twenty_one_months = {
	'01': range(1, 32),
	'02': range(1, 29),
	'03': range(1, 32),
	'04': range(1, 31),
	'05': range(1, 32),
	'06': range(1, 31),
	'07': range(1, 32),
	'08': range(1, 32),
	'09': range(1, 31)
}

twenty_twenty_months = {
	'01': range(1, 32),
	'02': range(1, 29),
	'03': range(1, 32),
	'04': range(1, 31),
	'05': range(1, 32),
	'06': range(1, 31),
	'07': range(1, 32),
	'08': range(1, 32),
	'09': range(1, 31),
	'10': range(1, 32),
	'11': range(1, 31),
	'12': range(1, 32)
}

dates = {
	'2019': twenty_nineteen_months,
	'2020': twenty_twenty_months,
	'2021': twenty_twenty_one_months 
}

article_data = []

for year in dates:
	for month in dates[year]:
		for day in dates[year][month]:
			article = Article(f'https://www.uexpress.com/life/dearabby/{year}/{month}/{day}', keep_article_html=True)
			article.download()
			soup = BeautifulSoup(article.html, 'html.parser')
			divs = soup.select('div[class*="Article_article__content__"]')[0:2]
			for div in divs:
				parsed_text = re.sub('[A-Z]{2,}:?', '', div.text)
				article_data.append([f'{year}-{month}-{day}', parsed_text])

parsed_data = pd.DataFrame(article_data, columns=['date', 'body'])
parsed_data.to_csv('ask_abby.csv')

