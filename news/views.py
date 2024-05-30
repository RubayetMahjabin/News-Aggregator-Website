from django.shortcuts import render, redirect, get_object_or_404
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Profile
from datetime import datetime

def scrape_onion():
    onion_news = []
    url = "https://www.theonion.com/"
    response = requests.get(url)
    soup = BSoup(response.content, "html.parser")
    
    articles = soup.find_all("article")
    for article in articles:
        title = article.find("h4").text.strip()
        link = article.find("a")["href"]
        image = None  
        img_tag = article.find("img")
        if img_tag:
            image = img_tag.get("src")
        onion_news.append({ "image": image, "title": title, "link": link, "source": "The Onion"})
    
    return onion_news


def save_news_to_db(news_list):
    for news in news_list:
        headline = Headline(title=news['title'], url=news['link'], image=news['image'], source=news['source'])
        headline.save()

def scrape(request):
    try:
        onion_news = scrape_onion()
        save_news_to_db(onion_news)
        
        
        messages.success(request, 'News articles scraped successfully!')
    except Exception as e:
        messages.error(request, f'Error occurred while scraping news: {e}')
    return redirect('dashboard')

@login_required
def save_news(request, news_id):
    news = get_object_or_404(Headline, id=news_id)
    profile = request.user.profile
    profile.saved_news.add(news)
    messages.success(request, 'News article saved to your profile!')
    return redirect('dashboard')

def news_list(request):
    scrape(request)
    headlines = Headline.objects.all()[::-1]
    context = {
        "object_list": headlines,
    }
    return render(request, "news/dashboard.html", context)
