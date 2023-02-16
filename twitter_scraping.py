

!pip install pandas

!pip install snscrape
!pip install pymongo

!pip install streamlit

!pip install pyngrok

"""Twitter Scrapping"""

!pip install -q streamlit



##pip install snscrape # Installing library social networking services.

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:elonmusk) until:2023-01-20 since:2022-10-01"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) ==limit:
    break
    #(date, id, url, tweet content, user,reply count, retweet count,language, source, like count etc) from twitter.
  else:
        tweets.append([tweet.id,tweet.url,tweet.user.username,tweet.content,tweet.date,tweet.source,tweet.retweetCount,tweet.likeCount,tweet.replyCount])
      
tweets_df = pd.DataFrame(tweets,columns=['Tweeter_ID', 'Url', "Account_Name", 'Content', 'Datetime','Source','Number_Retweets', 'Number_Likes', 'Number_Comments']) 

print(tweets_df)


tweets_df = tweets_df.to_csv("Tweeter_scraping") # converting dataframe to csv file.



#pip install pymongo # installing mongo db library

#!python --version

from pymongo import MongoClient # Importing Mongo db cloud server library

Tweet = MongoClient("mongodb+srv://lakshmi:Lachunov2@cluster0.9kjx5ob.mongodb.net/?retryWrites=true&w=majority")

Tweeterscraping = Tweet["Tweeter_task"] # creating a database in Mongodb server
Tweets = Tweeterscraping["Elon_Task"]

import pandas as pd # importing pandas library

Tweet = pd.read_csv("/content/Tweeter_scraping")  # Importing the converted Twetterscraping csv file
print(Tweet)

Tweet=Tweet.to_dict("records") #Converting datas to a dictionary

Tweets = Tweeterscraping["Twetter_scrapingDB"] #importing all the datas to the mongodb server
Tweets.insert_many(Tweet)

!pip install twint

!pip install botocore

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import twint
# import pandas as pd
# import json
# import botocore
# 
# 
# 
# st.set_page_config(page_title='Twitter scraper',page_icon=':iphone:')
# 
# 
# 
# st.subheader("""
# Scrape some Twitter Tweets and Download:
# """)
# 
# languages = []
# sentiments = []
# 
# with st.form(key='Twitter_form'):
#     search_term = st.text_input('What do you want to search for?')
#     limit = st.slider('How many tweets do you want to get?', 0, 500, step=20)
#     output_csv = st.radio('Save a CSV file?', ['Yes', 'No'])
#     output_Json = st.radio('Save a json file?', ['Yes', 'No'])
#     file_name = st.text_input('Name the CSV file:')
#     file_name = st.text_input('Name the json file:')
#     submit_button = st.form_submit_button(label='Search')
# 
#     if submit_button:
#         # configure twint
#         c = twint.Config()
# 
#         c.Search = search_term
#         c.Limit = limit
# 
#         c.Store_csv = True
# 
#         if c.Store_csv:
#             c.Output = f'{file_name}.csv'
#             
#         if c.Store_json:
#             c.Output = f'{file_name}.json'
# 
#         twint.run.Search(c)
# 
#         data = pd.read_csv(f'{file_name}.csv', usecols=['date', 'tweet'])
#         data1 = open('{file_name}.csv', usecols=['date', 'tweet'])
#         
# 
#         for x in data,data1['tweet']:
#             # Get language of the tweet
#             lang = comprehend.detect_dominant_language(Text=x)['Languages'][0]['LanguageCode']
#             languages.append(lang)
#             print(f'Language detected: {lang}')
#         data['languages']=languages
# 
#             # Get the sentiment of the tweet
#         for x in range(len(data['tweet'])):
#             try:
#                 sent = comprehend.detect_sentiment(
#                                                     Text=data['tweet'][x],
#                                                     LanguageCode= data['languages'][x]
#                                                     )['Sentiment']
#                 sentiments.append(sent)
#                 print(f'Sentiment detected:{sent}')
#             except botocore.exceptions.ClientError as error:
#                 print(f'Error: {error}')
#                 sentiments.append(error)
#         data['sentiment']= sentiments
#         st.table(data)
# 
# 
# try:
#     st.download_button(label='Download results', data=convert_df(data), file_name = f'{file_name}.csv', mime='text/csv')
#     st.download_button(label='Download results', data=convert_df(data), file_name = f'{file_name}.json', mime='text/json')
# except:
#     pass
#

!npm install localtunnel

!streamlit run /content/app.py &>/content/logs.txt &

!npx localtunnel --port 8501
