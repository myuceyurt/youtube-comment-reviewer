import googleapiclient.discovery
from googletrans import Translator
import textblob
import random
import sys

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = sys.argv[1]

def getComments(id,api_service_name,api_version,DEVELOPER_KEY):    
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=id,
        maxResults = 50,
        textFormat="plainText"
    )
    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        commentList.append(comment)

def getVideoID(url):
    return url[url.index("=")+1 : url.index("&")]

def newRange(old_min,old_max,new_min,new_max,old_val):
    new_value = ((old_val - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min # Linear Interpolation Formula
    return new_value


overall_score = 0
url = input("Enter the URL: ")
id = getVideoID(url)
commentList = list()

getComments(id,api_service_name,api_version,DEVELOPER_KEY)

translator = Translator()
my_lang = translator.detect(commentList[random.randint(0,len(commentList)-1)])
print(my_lang.lang)
isEng = True if my_lang == "en" else False
for comment in commentList: 
    try:
        print(comment)
        my_sentence = textblob.TextBlob(translator.translate(comment).text) if isEng == False else textblob.TextBlob(comment)
        overall_score += newRange(-1,1,0,100,my_sentence.sentiment[0])
    except Exception:
        pass

result = (int)(overall_score / len(commentList))
print(result)
if result in range(53,100): print("Mostly Liked")
else : print("Mostly Neutral" if result in range(47,53) else "Mostly Disliked")
