import os
from dotenv import load_dotenv
import requests
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build


# load_dotenv('.env')

# youtube_api = str(os.getenv('AIzaSyBj2DiHnpuLGudmYwfEYH0m9SGi4b-c99Y'))
# print ()
# api_endpoint = "http://apilayer.net/api/live?access_key=" + exchange_api + "&currencies=JPY,EUR,RMB,CAD&source=USD&format=1"
# response = requests.get(api_endpoint)
# if response.status_code == 200:
#     print ("Success connect with API! Here's the data")
#     data = response.json()
#     print (data)
# elif response.status_code == 404:
#     print ("Unable to reach URL")
# else:
#     print ("unable to connect API or retrieve data")
    


def main():
    load_dotenv()
    api_key = os.getenv('youtubeAPI')  # Please set your API key
    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, developerKey=api_key)
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()
    print(response)

if __name__ == "__main__":
    main()