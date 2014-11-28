import feedparser
import tweepy
import time

#d = feedparser.parse('https://sports.yahoo.com/nhl/blog/puck_daddy/rss.xml')
#d = feedparser.parse('http://feedparser.org/docs/examples/atom10.xml')

#print d.feed.link
#print d['feed']['link']
#print len(d['entries'])
#print d.entries

#For entry in d.entries:
	#print entry

#lastPost=""

def processFeed(lastPost):
  latestPost=""
  #print "Last Post: " + lastPost
  d = feedparser.parse('https://sports.yahoo.com/nhl/blog/puck_daddy/rss.xml')
  for post in d.entries:
	#print post.title + ": " + post.link + "\n"
  	link=post.link
  	id=post.id
	title=post.title
	if id==lastPost:
		# We are at the end
		#print "done"
		if latestPost == "":
			return (lastPost)
		else:
			return (latestPost)
	tweet= title[:80] + ' ' + link
	#print tweet
	api.update_status(tweet)
	# Sleep for 30 seconds between tweeets
	time.sleep(30)
	
	# Store the last post
	if latestPost == "":
		latestPost=str(id)
	# Temporary hack
  	#return(id)
  return(latestPost)




# Main
# Consumer keys and access tokens, used for OAuth
f = open('keys', 'r')
consumer_key,consumer_secret,access_token,access_token_secret=f.read().splitlines()
f.close

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


# Get the last article processed
f = open('lastpost', 'r')
lastPost=f.read()
f.close


latestPost=processFeed(lastPost)

#print "Last post:" + latestPost

if str(lastPost) != latestPost and latestPost!="":
        f = open('lastpost', 'w')
        f.write(latestPost)
        f.close
