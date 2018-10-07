# try:
        #     response = requests.get(url_first+str(pgno)+url_second)
        #     html_doc=response.text
        # except:
        #     break;




## try to make sure it is new

    ## - check date posted, then check the id
    ## - save a local value of the last day posted in some other file
    ## check with the array of id that i have

    ## pull out the id, the title, the price, the distance, the link and img

    # for ad in soup.find_all(attrs={'class':''}):
    #     ## id=ad.find(attrs={'data-ad-id':''})
    #     title=ad.find(attrs={'class':'clearfix'}).find(attrs={'class':'info'}).find(attrs={'class':'info-container'}).find(attrs={'class':'title'}).find(attrs={'class':'titleNavigationFlag'})
    #     price=ad.find(attrs={'class':'clearfix'}).find(attrs={'class':'info'}).find(attrs={'class':'info-container'}).find(attrs={'class':'price'})
    #     distance=ad.find(attrs={'class':'clearfix'}).find(attrs={'class':'info'}).find(attrs={'class':'info-container'}).find(attrs={'class':'distance'})
    #     postTime=ad.find(attrs={'class':'clearfix'}).find(attrs={'class':'info'}).find(attrs={'class':'info-container'}).find(attrs={'class':'location'}).find(attrs={'class':'date-posted'})
    #     print(ad).get_text()
    #     ##print(title)
    #     ##print(price)
    #     ##print(distance)
    #     ##print(postTime)




    # save id to somewhere else so we are not mistaken


## you can also try to search to phone number: not necessary though, im going to manually
## open the page anyways




# everytime we start scrapping, we compare the files to the previous file
# where we save the most recent five ads from last scrap
# until we see one that has the same id, we stop

# @ file with all the data
# @ file with most recent five ads from the most recent scrap)

# get the result of the first page to see if the url works
# for the first 20 pages, we compare the most recent ads to the list we have before
#



##  READ THIS FILE when you think you need more space/more efficient in reading files
## see the top answer: https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files