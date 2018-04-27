from nico.api.search_api_client import VideoSearchApiClient
from nico.domain.video_id import VideoId
from nico.repository.comment_repository import CommentRepository

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
archive_dir = "data/"
repository = CommentRepository(archive_dir)
for video in videos:
    print(video)
    video_id = VideoId(video["contentId"])
    archive_name = video_id.get_comment_dataset_archive_name()
    zip_name = archive_name + ".zip"
    zip_exists = repository.download_archive(zip_name)
    if zip_exists:
        repository.unzip_archive(zip_name, archive_name)