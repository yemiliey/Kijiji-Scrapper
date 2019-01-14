## Kijiji-Scraper
- Web-scraping tool using Python and BeautifulSoup
- scraps Kijiji housing results with customized filters applied (Unwanted words in title and description, prices, distance, etc)
- Store the most recent results, and only show new Ads the next time we scrap

### Usage
- Clone the repo
- run the script `scraper.py`
- find your resulting Ads with their name, link, price, distance, post time listed in `csv` form
- The next time you run the script, the results will be updated with all new Ads posted after the last time of scraping

### Future Development
- Extend this into a web app built with React.js for a better visual display of the data extracted from the web (work in progress)
- Periodically executes the script and notify user (email/messages) everytime a new and qualified Ad is posted

