# Reporting 2 Data Analysis

## Files

- [Ask Abby Scraping](https://github.com/vincentvb/reporting_2/blob/master/ask_abby.py) - Runs a sraper to gather Dear Abby data
- [NYTimes Social Q's Scraping](https://github.com/vincentvb/reporting_2/blob/master/nytimes.py)
- [WaPo Work Advice Scraping](https://github.com/vincentvb/reporting_2/blob/master/wapo.py)
- [Text analysis](https://github.com/vincentvb/reporting_2/blob/master/text_analysis.py) is run through a configurable script that allows you to examine either of the datasets. Right now the script displays the top 50 occuring words pre-pandemic and post-pandemic. More configurations to come.

## Examples
```
# Scrapes ask abby columns and generates CSV
python ask_abby.py

# Runs text analysis on nytimes data
DATA=nytimes python text_analysis.py
```