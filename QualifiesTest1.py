# used to test the whole qualifies function

import requests
import math
#####################
import string
###################
from bs4 import BeautifulSoup
red_flags = ["year", "lease", "male", "guy", "basement", "permanent", "long-term"]

## successfully avoided skipping ad because they contain
## please or female
def qualifies(text):
    for p in text:
        p=p.string.lower()  #now p is a string of sentence
        wordList=[word.strip(string.punctuation) for word in p.split()]
        for word in red_flags:
            if word in wordList:return False
    return True



url_first='https://www.kijiji.ca/b-room-rental-roommate/gta-greater-toronto-area/page-'
url_second='/c36l1700272r5.0?ad=offering&price=__1200&address=M6K+1Y6&ll=43.636322,-79.424146&furnished=1'

url=url_first+str(1)+url_second
response = requests.get(url)
html_doc=response.text
soup = BeautifulSoup(html_doc, 'html.parser')

for ad in soup.find_all(attrs={'class':'regular-ad'}):
        #ad=soup.find(attrs={'class':'regular-ad'})

        adId=ad.get('data-ad-id')

        # now this ad is not visitied before, we want to store its info

        # get the actual content of the ad
        href_link="https://www.kijiji.ca"+ad.get('data-vip-url')
        info=ad.find(attrs={'class':'info'})
        title=info.find('a',{'class':'title'}).text.strip()
        price=info.find('div',{'class':'price'}).text.strip()
        #postTime=info.find('span',{'class':'date-posted'}).text.strip()
        #postTime=get_postDate(postTime)
        distance=info.find('div',{'class':'distance'}).text.strip()
        print(title+"\n")
        print(adId)

        # can also do a search in the brief description first

        # to get the content of the page
        actual_page=requests.get(href_link)
        page_content=BeautifulSoup(actual_page.text, 'html.parser')
        descriptionContainer=page_content.find(attrs={'class':'descriptionContainer-3246526397'})
        description = descriptionContainer.find_all('p')

        print(description)

        if (qualifies(description)):
            # write all info you need the href_link to csv file
            #f_writer.writerow([adId, href_link, title, price, distance, postTime])
            print("qualifies")
        else:
            print("Not qualified")
