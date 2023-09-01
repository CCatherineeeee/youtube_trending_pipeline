import os
from dotenv import load_dotenv
import googleapiclient.errors
from googleapiclient.discovery import build

def youtube_data():
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
    # print(response)
    # video_infos = response["items"]
    # print (len(video_infos))
    # count = 0
    # for info in video_infos:
    #     print (count)
    #     print (info)
    #     count += 1
    '''
    content: 
    '''

if __name__ == "__main__":
    youtube_data()