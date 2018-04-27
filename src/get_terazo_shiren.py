from nico.api.search_api_client import VideoSearchApiClient
from nico.domain.video_id import VideoId

limit = 100
offset = 0

videos = []

while True:
    api = VideoSearchApiClient()
    query = "ゲーム テラゾー 風来のシレン"
    result = api.search_by_tag(
        query=query,
        limit=limit,
        offset=offset
    )
    items = result["data"]
    videos.extend(items)
    if len(result["data"]) < 100:
        break;
    offset = offset + limit;

print("-- videos ----------------------------------------")
for video in videos:
    print(video)
    video_id = VideoId(video["contentId"])
    print(video_id.get_number())