#Mars info scraper

#dependencies
from bs4 import BeautifulSoup as bs
import requests
import os
from splinter import Browser
import pandas as pd
import time

def mars_scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

#Get Mars News
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(5)
    soup = bs(browser.html,'html.parser')
    news_title = soup.find('div', class_ = 'content_title').text
    news_blurb = soup.find('div', class_ = 'rollover_description_inner').text
    browser.quit()

#Get JPL Mars Images
    url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url1)
    time.sleep(5)
    soup = bs(browser.html,'html.parser')
    image = soup.find('a', class_ = 'button fancybox')['data-fancybox-href']
    featured_image_url = f'https://www.jpl.nasa.gov{image}'
    browser.quit()

#Get Mars Weather
    url2 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url2)
    time.sleep(5)
    soup = bs(browser.html,'html.parser')
    mars_weather = soup.find('p', class_ = 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    browser.quit()

#Get Mars Facts
    url3 = 'https://space-facts.com/mars/'
    mars_facts = pd.read_html(url3)
    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = ['Mars Fact','Value']
    mars_html_table = mars_html_table.replace('\n','')
#Mars Hemispheres
    mars_info = {}

    mars_info['news_title'] = news_title
    mars_info['news_blurb'] = news_p
    mars_info['featured_image_url'] = featured_image_url
    mars_info['mars_weather'] = mars_weather
    mars_info['mars_html_table'] = mars_html_table

    return mars_info