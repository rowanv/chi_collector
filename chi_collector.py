'''
Scrapes sites to find jobs and write to db

'''
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chi_collector.settings")


import feedparser
import pprint
import nltk
import pandas as pd

from django.db import models
from chi_collector import settings
from chi_viewer.models import Posting
from django.utils import timezone



feeds = [

	'https://news.ycombinator.com/rss',
	#Python jobs on UpWork
	'https://www.upwork.com/jobs/rss?q=python&from=find-work#filter/?q=python&spellcheck=1&highlight=1&sortBy=relevance+desc&exp%5B%5D=3',

	'http://www.remotedatascience.com/feeds/posts/default?alt=rss',
	'https://www.upwork.com/jobs/?qs=statistics',
	'https://www.upwork.com/find-work-home/?topic=1830356', #django
	'https://careers.stackoverflow.com/jobs/feed?searchTerm=python&jobType=contract',
	'https://careers.stackoverflow.com/jobs/feed?searchTerm=d3.js&jobType=contract',
	'https://careers.stackoverflow.com/jobs/feed?jobType=contract&allowsremote=true',
	'https://djangogigs.com/feeds/gigs/',
	# Python jobs on Stack Overflow that are remote
	'http://careers.stackoverflow.com/jobs/feed?searchTerm=python&allowsremote=True',
	# d3 jobs on stack overflow that are remote
	'http://careers.stackoverflow.com/jobs/feed?searchTerm=d3&allowsremote=True',
	# Django jobs on StackOverflow that are remote
	'http://careers.stackoverflow.com/jobs/feed?searchTerm=django&allowsremote=True',
]


keywords = ['freelance', 'data visualization', 'big data', 'python', ' r ', 'pandas',
	'data', 'd3.js', 'd3', 'data analysis', 'hadoop', 'bigdata', 'pig', 'bokeh',
	'django', 'etl', 'django', 'flask']


def clean_feed_fields(text):
	#cleaned_html = nltk.clean_html(text)
	lowerwords = text.lower()
	return lowerwords

def collect_job_postings():
	columns = ['Title', 'Link', 'Source', 'Summary', 'Score']
	df = pd.DataFrame(columns=columns)

	score_dictionary = {}
	for feed in feeds:
		f = feedparser.parse(feed)
		for entry in f['entries']:
			entry_score = 0
			entry['title'] = clean_feed_fields(entry['title'])
			#for the remotedatascience site and upwork
			entry['summary'] = clean_feed_fields(entry['summary'])



			for keyword in keywords:
				if entry['title'].count(keyword) > 0:
					print(entry['title'])
					print(entry['title'].count(keyword))
				entry_score += entry['title'].count(keyword) #for HN and Upwork
				entry_score += entry['summary'].count(keyword)
				#Articles with freelance in them get a higher score
				if keyword == 'freelance':
					entry_score += entry['title'].count(keyword) * 10

				score_dictionary['%s : %s' % (entry['title'], entry['link'])] = entry_score
			data = pd.DataFrame({'Title': [entry['title']],
									'Link': [entry['link']],
									'Source': [feed],
									'Summary': [entry['summary']],
									'Score': [entry_score]})
			df = df.append(data)

	#Filter out articles that are not sufficiently relevant
	score_threshold = 1
	filtered_dictionary = {key: value for key, value in score_dictionary.items() if value >= score_threshold}

	df = df.ix[df.Score >= 1,]

	#Sort so article with the most keyword hits is first

	sorted_dictionary = sorted(filtered_dictionary.items(), key=lambda x: x[1], reverse=True)
	df = df.sort(['Score'], ascending=[0])
	df = df.reset_index(drop=True)

	pprint.pprint(sorted_dictionary)
	print(df)

	#from django.db import connection
	#query = str(Posting.objects.all().query)
	#current_data = pd.read_sql_query(query, connection)

	#df.to_sql()



	for row_num, row in df.iterrows():
		current_row = Posting(title=row.Title,
			source=row.Source,
			summary=row.Summary,
			score=row.Score,
			link=row.Link,
			date_written=timezone.now()
			)
		current_row.save()
		print(current_row)

if __name__ == '__main__':
	collect_job_postings()
