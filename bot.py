from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN =
"EAAIHe0SZAeJoBALFsCNtZA0vpNIZAMomK7B5k4ZA7L81bCWuMPxsGkeIw6YGXZBPMMv4wZB974H7WDafjihaaAIPEao46OtXsYPjIw6ZC7zmWSodXNlM9E33PNPfzfSZCWBoZC9ZA6NgXtT6c9QarLPyFtypDR9VLkSFlky3WZCBfhGXVPRVXCCYOTJ"
VERIFY_TOKEN = ""
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=["GET", "POST"])
def receive_message():
    if(request.method == "GET"):
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output["entry"]:
            messaging = event["messaging"]
            for message in messaging:
                if(message.get("message")):
                    recipient_id = message["sender"]["id"]
                    if(message['message'].get('text')):
                        response_sent_text = get_message()
                        send_message(recipient_id,
                                response_sent_text)

                    if(message['message'].get('attachments')):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)


    return "Message Processed"

def verify_fb_token(token_sent):
    if(token_sent == VERIFY_TOKEN):
        return request.args.get("hub.challenge")

    return "Invalid verification token"

def get_message():
    sample_responses = ["hellooooo","hello"]
    return random.choice(sample_responses)

def send_message():
    bot.send_text_message(recipient_id, response)
    return "success"

def gintamaScrape():
	#gintama url 
	gintamaUrl = 'https://en.wikipedia.org/wiki/List_of_Gintama_episodes'
	client = urlopen(gintamaUrl); html = client.read(); client.close()
	page_contents = BeautifulSoup(html, "html.parser")
	#Now start to search for wikitables
	listOfTds = page_contents.findAll("td", {"class": "summary"})
	episodeList = []
	for td in listOfTds:
		text = str(td).split("\"")[5]
		episodeList.append(text)
	
	return episodeList
		
def gintamaChat():
	print("Welcome to the gintama episode title generator")
	episodeList = gintamaScrape()
	userChoice = ""
	while(userChoice != 'n'):
		userChoice = str(input("Would you like an episode title (y/n)?").rstrip('\n'))
		if(userChoice == 'y'):
			print(episodeList[randint(0,len(episodeList)-1)])
	
if(__name__ == "__main__"):
    app.run()
