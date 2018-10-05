import requests
import math
from bs4 import BeautifulSoup

## args={'ll':'43.636322,-79.424146','address':'M6K%201Y6','ad':'offering','furnished':'1','price':'__1200' }
## search_url='https://www.kijiji.ca/b-room-rental-roommate/city-of-toronto/c36l1700273'
url='https://www.kijiji.ca/b-room-rental-roommate/city-of-toronto/c36l1700272?ll=43.636322,-79.424146&address=M6K%201Y6&ad=offering&furnished=1&price=__1200'
url2='https://www.kijiji.ca/b-room-rental-roommate/gta-greater-toronto-area/c36l1700272r5.0?ad=offering&price=__1200&address=M6K+1Y6&ll=43.636322,-79.424146&furnished=1'
url_first='https://www.kijiji.ca/b-room-rental-roommate/gta-greater-toronto-area/page-'
url_second='/c36l1700272r5.0?ad=offering&price=__1200&address=M6K+1Y6&ll=43.636322,-79.424146&furnished=1'

try:
    response = requests.get(url_first+str(1)+url_second)
    html_doc=response.text
except:
    print("URL not accessible")
    exit();
soup = BeautifulSoup(html_doc, 'html.parser')
## print("Ready")
try:
    total_results=soup.find(attrs={'class':'showing'}).get_text()
    total_results_num = int(total_results[total_results.index("of")+3: total_results.index("Ads")-1].strip())/20
    last_page=int(math.ceil(total_results_num))
    print("last page: "+last_page)
except:
    print("No jobs found")

jobs_per_page=20
for pgno in range(0,last_page,1):
    ## try to get the page result
    if pgno > 0:
        try:
            response = requests.get(url_first+str(pgno)+url_second)
            html_doc=response.text
        except:
            break;
        soup = BeautifulSoup(html_doc, 'html.parser')

    ## try to make sure it is new

    ## - check date posted, then check the id
    ## - save a local value of the last day posted in some other file
    ## check with the array of id that i have

    ## pull out the id, the title, the price, the distance, the link and img

    for ad in soup.find_all(attrs={'class':''}):
        ## id=ad.find(attrs={'data-ad-id':''})
        title=ad.find(attrs={'class':'clearfix'}).find(attrs={'class':'info'}).find(attrs={'class':'info-container'}).find(attrs={'class':'title'}).find(attrs={'class':'titleNavigationFlag'})
        price=ad.find(attrs={'class':'clearfix'}).find(attrs={'class':'info'}).find(attrs={'class':'info-container'}).find(attrs={'class':'price'})
        distance=ad.find(attrs={'class':'clearfix'}).find(attrs={'class':'info'}).find(attrs={'class':'info-container'}).find(attrs={'class':'distance'})
        postTime=ad.find(attrs={'class':'clearfix'}).find(attrs={'class':'info'}).find(attrs={'class':'info-container'}).find(attrs={'class':'location'}).find(attrs={'class':'date-posted'})
        print(title)
        print(price)
        print(distance)
        print(postTime)






