from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse

from .models import News, Urls, StopWords


logger = get_task_logger(__name__)

@shared_task(serializer='json')
def save_function(article_list):
    source = article_list[0]['source']
    new_count = 0
    error = True
    try:
        latest_article = News.objects.filter(source=source).order_by('-id')[0]
        print(latest_article.published)
        print('var TestTest: ', latest_article, 'type: ', type(latest_article))
    except Exception as e:
        print('Exception at latest_article: ')
        print(e)
        error = False
        pass
    finally:
        if error is not True:
            latest_article = None

    for article in article_list:
        if latest_article is None:
            try:
                News.objects.create(
                    title=article['title'],
                    link=article['link'],
                    category=article['category'],
                    description=article['description'],
                    published=article['published'],
                    source=article['source']
                )
                new_count += 1
            except Exception as e:
                print('failed at latest_article is none')
                print(e)
                return
        elif latest_article.published < article['published']:
            try:
                News.objects.create(
                    title=article['title'],
                    link=article['link'],
                    category=article['category'],
                    description=article['description'],
                    published=article['published'],
                    source=article['source']
                )
                new_count += 1
            except:
                print('failed at latest_article.published < j[published]')
                return
        else:
            print('news scraping failed')
            return

    logger.info(f'New articles: {new_count} articles(s) added.')
    print('finished')
    return

@shared_task
def news_rss():
    try:
        urls = Urls.objects.all().values_list('url', flat=True).distinct()
        word_set = set(StopWords.objects.all().values_list('word', flat=True).distinct())
        for url in urls:
            print(f'Starting the scraping tool {url}')
            article_list = []
            request = requests.get(url)
            soup = BeautifulSoup(request.content, features='xml')
            articles = soup.findAll('item')
            for aticle in articles:
                title = aticle.find('title').text
                title_set = {i.lower() for i in title.split()}
                try:
                    for word in title_set:
                        for a in word_set:
                            if word.find(a) != -1:
                                raise StopIteration
                except StopIteration:
                    continue
                link = aticle.find('link').text
                category = aticle.find('category').text
                description = aticle.find('description').text
                published_wrong = aticle.find('pubDate').text
                published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
                source = urlparse(url)
                article_ = {
                    'title': title,
                    'link': link,
                    'category': category,
                    'description': description,
                    'published': published,
                    'source': source.netloc
                }
                article_list.append(article_)
            print(f'Finished scraping the articles {url}')
            save_function(article_list)
        return
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)