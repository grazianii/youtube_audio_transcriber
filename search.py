from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)


def search_videos(query, max_results):

    # Define parâmetros de busca de vídeos no YouTube
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results,
        order="relevance",
        relevanceLanguage="pt",
        regionCode="BR"
    )

    # Armazena resposta da busca de vídeos
    response = request.execute()

    # Define lista de vídeos
    videos = []

    # Armazena dados de vídeos
    for item in response["items"]:

        videos.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published": item["snippet"]["publishedAt"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })

    return videos