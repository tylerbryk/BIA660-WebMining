# Tyler Bryk

from bs4 import BeautifulSoup
import re
import time
import requests


def run(url):
    pageNum = 2                                                 # Number of pages to collect
    fw = open('reviews.txt','w')                                # Output file	
    for p in range(1, pageNum+1): 
        print('page', p)
        html = None
        if p == 1: pageLink = url
        else: pageLink = url + '?page=' + str(p) + '&sort='
        for i in range(5):                                      # Try 5 times
            try:
                response = requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',})
                html = response.content
                break
            except Exception:
                print('Failed Attempt: ',i)
                time.sleep(2)
				
        if not html: continue       
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml')
        reviews = soup.findAll('div', {'class':re.compile('review_table_row')})
        for review in reviews:
            critic, rating, src, text, date = 'NA','NA','NA','NA','NA'
            
            # Find the <Critic> of the Review
            criticChunk = review.find('a',{'href':re.compile('/critic/')})
            if criticChunk: critic = criticChunk.text.strip()
            
            # Fresh or Rotten?
            fresh = review.find('div',{'class':'review_icon icon small fresh'})
            rotten = review.find('div',{'class':'review_icon icon small rotten'})
            if fresh: rating = 'fresh'
            if rotten: rating = 'rotten'
            
            # Find the <Source> of the Review
            srcChunk = review.find('em',{'class':'subtle critic-publication'})
            if srcChunk: src = srcChunk.text.strip()
            
            # Find the <Text> of the Review
            textChunk = review.find('div',{'class':'the_review'})
            if textChunk: text = textChunk.text.strip()
            
            # Find the <Date> of the Review
            dateChunk = review.find('div',{'class':'review-date subtle small'})
            if dateChunk: date = dateChunk.text.strip()
            
            fw.write(critic + '\t' + rating + '\t' + src + '\t' + text + '\t' + date + '\n') 
    fw.close()

if __name__ == '__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)