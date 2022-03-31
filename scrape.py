"""Python Web Scraping Example."""
import requests
from bs4 import BeautifulSoup


def get_stock_reco():
    """Stock reco data extraction using Web Scraping."""
    res1 = requests.get('https://www.moneycontrol.com/news/business/stocks/')
    res2 = requests.get(
        'https://www.moneycontrol.com/news/business/stocks/page-2')
    soup1 = BeautifulSoup(res1.text, 'html.parser')
    soup2 = BeautifulSoup(res2.text, 'html.parser')

    # heads up! .storylink changed to .titlelink
    link1 = soup1.select('#cagetory')
    link2 = soup2.select('#cagetory')
    links = link1 + link2

    def fetch_market_news(links):
        """Fetch market feeds."""
        news = []
        for item in links:
            level1 = item.select('.clearfix')
            for element in level1:
                # sub_element = element.h2
                level2 = element.a
                news.append(level2.get('title'))
        return news

    market_news = fetch_market_news(links)
    return market_news


def main():
    """Entry point"""
    market_feed = get_stock_reco()
    for news in market_feed:
        print(news)


if __name__ == '__main__':
    main()
