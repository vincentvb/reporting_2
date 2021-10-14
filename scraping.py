import pandas as pd
import json
import re

from newspaper import Article
from bs4 import BeautifulSoup

with open("nytimes.json", "r") as read_file:
	data = json.load(read_file)
	print(data[0])


	article_data = []

	for url in data[0:1]:
		# Retrieve article content and download HTML
		article = Article(url, keep_article_html=True)
		article.download()

		# Parse HTML with BeautifulSoup and extract date
		soup = BeautifulSoup(article.html, 'html.parser')
		date = soup.time.attrs['datetime'][0:10]

		# Initialize blank article body
		article_body = ''
		for index, element in enumerate(soup.find('section', {'name': 'articleBody'})):
			if index == 0:
				article_body = element.get_text()
			else:
				article_body += element.get_text()
		
        # Push article body/date to array for future processing

		article_body = article_body.split("For help with your awkward situation", 1)[0]
		# article_body = re.sub(r'([A-Z]{2,})', r'\1\n', article_body)
		print(article_body)
		article_data.append([date, article_body])


    # Convert to DataFrame and generate csv file
	parsed_data = pd.DataFrame(article_data, columns=['date', 'body'])
	print(parsed_data.head())
	parsed_data.to_csv('nytimes_data.csv')