from feedparser import parse
from bs4 import BeautifulSoup
from pydantic import BaseModel, PositiveInt, Field
from typing import Literal

# def fetch_articles(feed_urls):
#     articles = []
#     for url in feed_urls:
#         source = parse(url)
#         for entry in source.entries:
#             article = {
#                 "feed": source.feed.get("title"),
#                 "title": entry.get("title"),
#                 "author": entry.get("author"),
#                 "summary": BeautifulSoup(entry.get("summary", ""), "html.parser").get_text()[:300],
#                 "published": entry.get("published"),
#                 "link": entry.get("link")
#             }    
#             articles.append(article)


#     return articles
# urls = ["https://www.theverge.com/rss/index.xml"]
# print(fetch_articles(urls)[0])

class ArticleAnalysis(BaseModel):
    summary : str
    category: Literal["AI", "Hardware", "Security", "Emerging Technology", "Business", "Software", "Other" ]
    companies_mentioned: list[str]
    impact_reason: str
    impact_score: PositiveInt = Field(le=5)


article = ArticleAnalysis(summary= "The Nape Pro was Keychron's first trackball device that was introduced at CES 2026 with a slim and compact design allowing it to be positioned right up against a keyboard",
                          category="Emerging Technology", companies_mentioned=["Logitech", "Keychron"], impact_reason="New Emerging technology", impact_score=2)
article2 = ArticleAnalysis(summary= "Companies_mentioned test with no entry",
                          category="Emerging Technology", companies_mentioned=[], impact_reason="New Emerging technology", impact_score=2)
# article3 = ArticleAnalysis(summary= "Companies_mentioned test with None entry should error",
#                           category="Emerging Technology", companies_mentioned=["apple", None], impact_reason="New Emerging technology", impact_score=2)

print(article2)
print(ArticleAnalysis.model_json_schema())