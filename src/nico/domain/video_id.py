class VideoId():

    def __init__(self, id):
        self.__id = id

    def get_number(self):
        return int(self.__id[2:])
