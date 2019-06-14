import sys, tweepy, calendar
from datetime import date,datetime
import requests
from datetime import date,datetime
from lxml import html


###############################################################################
########## Crawl 3djuegos.com to obtain topgames of the next month ############
###############################################################################

session = requests.Session()
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
session.headers = headers

#get the current year and month to complete after the url
c_year = date.today().year 
c_month = date.today().month

#next month = current month + 1
if c_month<12:
	next_month = c_month+1
#if we are in december next month has to be 1 and not 13, and the year will also increment
else: 
	c_month = 0 
	next_month = c_month+1
	c_year = c_year + 1

#complete the link that we need to get the page where appear the top games of the next month
base_link = "https://www.3djuegos.com"
url_to_crawl = base_link+"/lanzamientos-juegos/todos/por-mes/0/"+str(c_year)+"/"+str(next_month)+"/"
#url_to_crawl = base_link+"/lanzamientos-juegos/todos/por-mes/0/"+str(c_year)+"/"+str(c_month)+"/"


#we get the page.
page = session.get(url_to_crawl)
tree = html.fromstring(page.content)
 
#get the text of the top games. they are in a ul list
h1 = tree.xpath("//ul[@class='list_foro fw5']//text()")

#Tweet the top games of next month according to 3dgames in Twitter
API_KEY = "BT4RdMtN5nHGcHgvKXRBvp2Ti"
API_SECRET = "9aZFukesG4ZSoq7JooWEk7PBODzXURjfv3lqnvUDtuuQ8K29F0"
ACCESS_TOKEN = "1129832031226073088-eYNH7J3vhRCrYbvNWGM8rJaUKLBluZ"
ACCESS_TOKEN_SECRET = "jMVHwGobCyLMPhuhCISZSTG74COD5kYlHFRDiw6TXH4AD" 
#using these credentials, we create an API object. 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

text_file = open("TopGames.txt", "w")

allmsg = ""
for x in h1:
        allmsg+=x+"\n"
        text_file.write(x+"\n")
text_file.close()
print(allmsg)
#tweet the top games of the next month based on 3djuegos
api.update_status(">>>>>>>> Best games of "+calendar.month_name[next_month]+" "+str(c_year)+" according to 3djuegos.com <<<<<<<<\n\n"+str(allmsg))
