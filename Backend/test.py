# I copied World News API's documentation example to see if it would work because it wasn't working in my other script.
# Working Version. I figured out that there were errors in the documentation, and I had to use trial and error to figure out what the correct answer was.
# I contacted the creator of World News API and told him about the errors, and what the correct solution was.

import worldnewsapi
from dotenv import load_dotenv
import os
from datetime import date, timedelta

# Initial SDK configuration
def initialize():
    load_dotenv()
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        raise ValueError("WORLD_NEWS_API_KEY not found in .env file")

    global newsapi_configuration
    newsapi_configuration = worldnewsapi.Configuration(api_key={'apiKey': api_key})


try:
    initialize()
    newsapi_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(newsapi_configuration))

    max_results = 250   # replace with your maximum
    offset = 0
    all_results = []

    while len(all_results) < max_results:
        request_count = min(100, max_results - len(all_results)) # request 100 or the remaining number of articles
        one_week_ago = str(date.today() - timedelta(days=7))

        response = newsapi_instance.search_news(
           text='football',
           source_country='us',
           language='en',
           earliest_publish_date=one_week_ago,
           latest_publish_date=str(date.today()),
           categories='sports',
           sort="publish-time",
           sort_direction="desc",
           min_sentiment=-0.8,
           max_sentiment=0.8,
           offset=offset,
           number=request_count)

        print("Retrieved " + str(len(response.news)) + " articles. Offset: " + str(offset) + "/" + str(max_results) +
             ". Total available: " + str(response.available) + ".")

        if len(response.news) == 0:
           break

        all_results.extend(response.news)
        offset += 100

except worldnewsapi.ApiException as e:
    print("Exception when calling NewsApi->search_news: %s\n" % e)


for article in all_results:
    print("Title: " + str(article.title))