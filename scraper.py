import requests
import math
from bs4 import BeautifulSoup
import csv
import string
from datetime import date, timedelta

url_full='https://www.kijiji.ca/b-room-rental-roommate/gta-greater-toronto-area/c36l1700272r5.0?ad=offering&price=__1200&address=M6K+1Y6&ll=43.636322,-79.424146&furnished=1'
url_first='https://www.kijiji.ca/b-room-rental-roommate/gta-greater-toronto-area/page-'
url_second='/c36l1700272r5.0?ad=offering&price=__1200&address=M6K+1Y6&ll=43.636322,-79.424146&furnished=1'

# all in lower case since they will be compared to text in lower case
red_flags = ["year", "lease", "male", "guy", "basement", "permanent", "long-term"]
# 4th year student
# males

topFiveFile='previousFive.csv'
file_name='results.csv'
f=open(file_name, 'a')
f_writer=csv.writer(f)

newTopFive=[]

## if there isn't one, we need to create one here
##TODO

## text is a list of <p>
## p is a sentence containing words
## this fixed the puntuation stuff and works fine now
def qualifies(text):
    for p in text:
        p=p.string.lower()  #now p is a string of sentence
        wordList=[word.strip(string.punctuation) for word in p.split()]
        for word in red_flags:
            if word in wordList:
                #print("not qualified because of "+word)
                return False
    return True


def get_postDate(text):
    try:
        ## if the ad was posted several days ago (including 1 day)
        time=text.index('/')
        return text
    except:
        try:
            time=text.index('Yesterday')
            yd=date.today()-timedelta(1)
            day=yd.strftime('%d/%m/%y')
            return day
        except:
            day=date.today().strftime('%d/%m/%y')
            return day

# fileName should be in the form : 'exmaple.txt' (a string)
def visited(adId):
    if adId in open(topFiveFile).read():
        return True
    return False

############################################################
try:
    url=url_first+str(1)+url_second
    response = requests.get(url)
    html_doc=response.text
except:
    print("URL not accessible")
    exit()
soup = BeautifulSoup(html_doc, 'html.parser')

try:
    ads_per_page=20
    total_results=soup.find(attrs={'class':'showing'}).get_text()
    total_results_num = int(total_results[total_results.index("of")+3: total_results.index("Ads")-1].strip())/ads_per_page
    last_page=int(math.ceil(total_results_num))
    print("last page: "+str(last_page))
except:
    print("No jobs found")

adNo=0  #this is for storing topFive

for pgno in range(0,last_page,1):

    print("reached page "+str(pgno+1))
    if pgno > 0:
        response = requests.get(url_first+str(pgno+1)+url_second)
        html_doc=response.text
        soup = BeautifulSoup(html_doc, 'html.parser')

    for ad in soup.find_all(attrs={'class':'regular-ad'}):
        #ad=soup.find(attrs={'class':'regular-ad'})

        adId=ad.get('data-ad-id')
        if (visited(adId)):
            exit();     # end the execution of this whole thing

        # now this ad is not visitied before, we want to store its info

        # get the actual content of the ad
        href_link="https://www.kijiji.ca"+ad.get('data-vip-url')
        info=ad.find(attrs={'class':'info'})
        #title=info.find('a',{'class':'title'}).text.strip()    // this can cause unicode error
        title=info.find('a',{'class':'title'}).text.encode('utf-8').strip()

        price=info.find('div',{'class':'price'}).text.strip()
        postTime=info.find('span',{'class':'date-posted'}).text.strip()
        postTime=get_postDate(postTime)
        distance=info.find('div',{'class':'distance'}).text.strip()
        # print("\n"+title)
        # print(adId)
        # print(price)
        # print(postTime)
        # print(distance)
        # print(href_link)
        # print(title)
        # can also do a search in the brief description first

        # to get the content of the page
        actual_page=requests.get(href_link)
        page_content=BeautifulSoup(actual_page.text, 'html.parser')
        descriptionContainer=page_content.find(attrs={'class':'descriptionContainer-3246526397'})
        description = descriptionContainer.find_all('p')
        #print(description)

        if (qualifies(description)):
            # write all info you need the href_link to csv file
            f_writer.writerow([adId, href_link, title, price, distance, postTime])
            f_writer.writerow([])
            #print("qualifies")

            if (adNo < 5):  # we want to store it as the top five
                newTopFive.append(adId)
                #print("adding to top five\n")
                adNo+=1
f.close()

# we need to write the newTopFive to previousTopFive.csv
with open(topFiveFile, 'w') as tf:
    tf_writer=csv.writer(tf)
    for ad in newTopFive:
        tf_writer.writerow([ad])
tf.close()




