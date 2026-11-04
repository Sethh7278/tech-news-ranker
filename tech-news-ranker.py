from feedparser import parse
from bs4 import BeautifulSoup



def fetch_articles(feed_urls):
    articles = []
    for url in feed_urls:
        source = parse(url)
        for entry in source.entries:
            article = {
                "feed": source.feed.get("title"),
                "title": entry.get("title"),
                "author": entry.get("author"),
                "summary": BeautifulSoup(entry.get("summary", ""), "html.parser").get_text()[:300],
                "published": entry.get("published"),
                "link": entry.get("link")
            }    
            articles.append(article)


    return articles
urls = ["https://www.theverge.com/rss/index.xml"]
print(fetch_articles(urls)[0])