import requests
import logging

class VideoSearchApiClient():
    """http://site.nicovideo.jp/search-api-docs/search.html
    """

    base_url = "http://api.search.nicovideo.jp/api/v2/video/contents/search"

    def search_by_tag(self, query):
        """タグ検索をする

        :param query: スペース区切りだとAND検索
        http://site.nicovideo.jp/search-api-docs/search.html
        """
        targets = "tags"
        sort = "-startTime"
        fields = "contentId,title,startTime"
        limit = 100
        params = {
            "q": query,
            "targets": targets,
            "fields": fields,
            "_sort": sort,
            "_limit": limit,
        }
        response = requests.get(
            self.base_url,
            params=params
        )
        print(response.json())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    api = VideoSearchApiClient()
    api.search_by_tag("テラゾー シレン")
