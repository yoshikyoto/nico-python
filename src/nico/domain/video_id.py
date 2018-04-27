import math

class VideoId():

    def __init__(self, id):
        self.__id = id

    def get_number(self):
        return int(self.__id[2:])

    def get_comment_dataset_archive_name(self):
        return str(math.floor(self.get_number() / 10000))
