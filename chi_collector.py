import feedparser
import pprint
import nltk



feeds = [
	'https://news.ycombinator.com/rss',
	#Python jobs on UpWork
	'https://www.upwork.com/jobs/rss?q=python&from=find-work#filter/?q=python&spellcheck=1&highlight=1&sortBy=relevance+desc&exp%5B%5D=3'
]


keywords = ['freelance', 'data visualization', 'big data', 'python', ' r ', 'pandas',
	'data', 'Dropbox', 'd3.js', 'd3', 'data analysis']


def clean_feed_fields(text):
	#cleaned_html = nltk.clean_html(text)
	lowerwords = text.lower()
	return lowerwords


score_dictionary = {}
for feed in feeds:
	f = feedparser.parse(feed)
	for entry in f['entries']:
		entry_score = 0
		entry['title'] = clean_feed_fields(entry['title'])
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

#Filter out articles that are not sufficiently relevant
score_threshold = 1
filtered_dictionary = {key: value for key, value in score_dictionary.items() if value >= score_threshold}

#Sort so article with the most keyword hits is first

sorted_dictionary = sorted(filtered_dictionary.items(), key=lambda x: x[1], reverse=True)

pprint.pprint(sorted_dictionary)


