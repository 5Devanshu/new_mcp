from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import os
from bs4 import BeautifulSoup
import json
from datetime import datetime
from typing import List, Dict, Optional
import asyncio
import re
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor 

load_dotenv()

# Initialize MCP server
mcp = FastMCP("Enhanced News Aggregator")

USER_AGENT = "news-app/1.0"

NEWS_SITES = {
    "arstechnica": "https://arstechnica.com",
    "techcrunch": "https://techcrunch.com",
    "bbc": "https://www.bbc.com/news",
    "sports": "https://www.iplt20.com/news"
}

class NewsDB:
    def __init__(self):
        self.articles = {}
        self.user_preferences = {}
        self.bookmarks = {}
    
    def add_article(self, article_id, article_data):
        self.articles[article_id] = article_data
    
    def get_article(self, article_id):
        return self.articles.get(article_id)
    
    def get_all_articles(self):
        return self.articles
    
    def set_user_preference(self, user_id, preferences):
        self.user_preferences[user_id] = preferences
    
    def get_user_preference(self, user_id):
        return self.user_preferences.get(user_id, {"categories": ["general"]})
    
    def add_bookmark(self, user_id, article_id):
        if user_id not in self.bookmarks:
            self.bookmarks[user_id] = []
        if article_id not in self.bookmarks[user_id]:
            self.bookmarks[user_id].append(article_id)
    
    def remove_bookmark(self, user_id, article_id):
        if user_id in self.bookmarks and article_id in self.bookmarks[user_id]:
            self.bookmarks[user_id].remove(article_id)
    
    def get_bookmarks(self, user_id):
        return self.bookmarks.get(user_id, [])

news_db = NewsDB()

async def fetch_news(url: str):
    """It pulls and summarizes the latest news from the specified news site."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            text = " ".join([p.get_text() for p in paragraphs[:5]]) 
            return text
        except httpx.TimeoutException:
            return "Timeout error"

@mcp.tool()  
async def get_tech_news(source: str):
    """
    Fetches the latest news from a specific tech news source.

    Args:
    source: Name of the news source (for example, "arstechnica" or "techcrunch").

    Returns:
    A brief summary of the latest news.
    """
    if source not in NEWS_SITES:
        raise ValueError(f"Source {source} is not supported.")

    news_text = await fetch_news(NEWS_SITES[source])
    return news_text

@mcp.tool()
def get_all_articles() -> str:
    """Get all available news articles"""
    articles = news_db.get_all_articles()
    return json.dumps(list(articles.values()), indent=2)

@mcp.tool()
def get_user_preferences(user_id: str) -> str:
    """Get user news preferences"""
    preferences = news_db.get_user_preference(user_id)
    return json.dumps(preferences, indent=2)

@mcp.tool()
def bookmark_article(user_id: str, article_id: str) -> str:
    """Bookmark an article for a user"""
    if not news_db.get_article(article_id):
        return json.dumps({"status": "error", "message": "Article not found"})
    
    news_db.add_bookmark(user_id, article_id)
    return json.dumps({"status": "success", "message": f"Article {article_id} bookmarked for user {user_id}"})

if __name__ == "__main__":
    mcp.run(transport="stdio")
