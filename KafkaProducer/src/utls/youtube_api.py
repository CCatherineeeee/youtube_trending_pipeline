import os
from dotenv import load_dotenv
import googleapiclient.errors
from googleapiclient.discovery import build

def youtube_trending_data():
    load_dotenv()
    api_key = os.getenv('youtubeAPI')  # Please set your API key
    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, developerKey=api_key)
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        maxResults=10,
        regionCode="US"
    )
    response = request.execute()
    return response
    '''
    content: 
    '''

if __name__ == "__main__":
    youtube_trending_data()