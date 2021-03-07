from selenium import webdriver
import time, codecs


driver = webdriver.Chrome('./chromedriver')
driver.get('https://twitter.com/SHAQ')
already_seen = set()
fw = codecs.open('tweets.txt', 'w', encoding='utf8')

for i in range(5):
    print (i)
    tweets = driver.find_elements_by_css_selector('div[data-testid="tweet"]')
    print (len(tweets))
    for tweet in tweets:
        if tweet in already_seen: continue
        already_seen.add(tweet)
        txt, comments, retweets, likes, date = 'NA', 'NA', 'NA', 'NA', 'NA'
        
        # Text
        try: 
            txt = tweet.find_element_by_css_selector("div.css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0").text
            txt = txt.replace('\n', ' ')
            print(txt)
        except: print ('no text')     

        # Comments
        try:
            commentElement = tweet.find_element_by_css_selector('div[data-testid="reply"]')
            comments = commentElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text  
            print (comments)                                    
        except:
            print ('no comments')

        # Retweets
        try:
            retweetElement = tweet.find_element_by_css_selector('div[data-testid="retweet"]')
            retweets = retweetElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text  
            print (retweets)                                    
        except:
            print ('no retweets')
            
        # Likes
        try:
            likesElement = tweet.find_element_by_css_selector('div[data-testid="like"]')
            likes = likesElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text  
            print (likes)                                    
        except:
            print ('no likes')
            
        # Date
        try: 
            dateElement = tweet.find_element_by_css_selector('a.css-4rbku5.css-18t94o4.css-901oao.r-1re7ezh.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0')
            date = dateElement.find_element_by_tag_name('time').get_attribute('datetime')
            print(date)
        except:
            print ('no date')
                                                             
            
 
        if txt != 'NA':
            fw.write(txt.replace('\n',' ') + '\t' + str(comments) + '\t' + str(retweets) + '\t' + str(likes) + '\t' + str(date) + '\n')
        print()
        print()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
fw.close()