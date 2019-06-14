import sys, tweepy, calendar
import re, json
from datetime import date,datetime
from classifier import *
from itertools import chain
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

from flask import Flask, jsonify
from flask_cors import CORS


def percentage(part, whole):
	return round((100 * float(part)/float(whole)),2)

###############################################################################
########## Crawl Twitter to obtain tweets that talks  #########################
########## about the topgames of the next month       #########################
###############################################################################
API_KEY = "BT4RdMtN5nHGcHgvKXRBvp2Ti"
API_SECRET = "9aZFukesG4ZSoq7JooWEk7PBODzXURjfv3lqnvUDtuuQ8K29F0"
ACCESS_TOKEN = "1129832031226073088-eYNH7J3vhRCrYbvNWGM8rJaUKLBluZ"
ACCESS_TOKEN_SECRET = "jMVHwGobCyLMPhuhCISZSTG74COD5kYlHFRDiw6TXH4AD" 


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

#using these credentials, we create an API object. 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

MAX_TWEETS = 50000000000000000000000000000000000000
msg=""
f = open("TopGames.txt")
listcounts = []
json_items = []

for x in f:	
	count = 0
	x = x.rstrip("\n")#para quitar el salto de linea
	query = x + "-filter:retweets"

	print("#################################################################")
	print("###################### "+x+" #######################")
	print("#################################################################\n")

	results = tweepy.Cursor(api.search,q=query,lang="en",tweet_mode='extended').items(100)#Cuanto mas tweets mas tiempo tarda en procesar
	positive = 0
	negative = 0
	neutral = 0
	polarity = 0
	
	for result in results:
		
		count = count +1
		content = result.full_text
		#print(content)
		#print("===========================================================================================")
		analysis = TextBlob(content)
		polarity += analysis.sentiment.polarity
		
		if(analysis.sentiment.polarity == 0):
			neutral += 1
			#print("Neutral "+ str(neutral))
		elif(analysis.sentiment.polarity < 0.00):
			negative += 1
			#print("Negative " + str(negative))
		elif(analysis.sentiment.polarity > 0.00):
			positive += 1
			#print("Positive " + str(positive))
	
	nTweets = str(count)
#	print("------------- tweets= "+nTweets+"-------------\n")
	listcounts = listcounts+[(x,int(nTweets))]
	
	ppositive = percentage(positive,nTweets)
	pnegative = percentage(negative,nTweets)
	pneutral = percentage(neutral, nTweets)
	
	#save all in json to get it after from the web site
	GAMES = {
			"name":x,
			"positive":{
				"percentage": str(ppositive)+"%",
				"totalTweets": str(positive)
			},
			"negative": {
				"percentage":str(pnegative)+"%",
				"totalTweets": str(negative)
			},
			"neutral": {
				"percentage":str(pneutral)+"%",
				"totalTweets": str(neutral)
			}
		}
	json_items.append(GAMES)

	#msg = msg +"How people are reacting on " + x + " by analysing " + str(nTweets) + " Tweets."\
	#+"\n"+"Positive " + str(ppositive)+" %\n"+"Negative "\
	#+ str(pnegative)+" %\n"+"Neutral "+ str(pneutral)+" %\n\n"
	
	
	api.update_status("How people are reacting on " + x + " by analysing " + str(nTweets) + " Tweets."
	+"\n"+"Positive " + str(ppositive)+" %\n"+"Negative "
	+ str(pnegative)+" %\n"+"Neutral "+ str(pneutral)+" %\n")

listcounts.sort(key=lambda x: x[1], reverse=True)#ordenar por nTweets


res = ""
for x in listcounts:
	res = res + x[0]+"-> "+str(x[1])+" \n"

	
api.update_status(">>> Mejores juegos de "+str(next_month)+"/"+str(c_year)+" según el #Tweets <<<\n\n"+str(res))

f.close()

print("Python Server running ...")
# configuration
DEBUG = True

#SERVER ____________________________________________________________________________________________________________________
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/games', methods=['GET'])
def gamesReleasedNextMonth():
    return jsonify({
        'status': 'success',
        'games' : json_items
    })


if __name__ == '__main__':
    app.run()


