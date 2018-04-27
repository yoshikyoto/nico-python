import os.path
import urllib.request
import zipfile

class CommentRepository():

    __archive_base_url = "http://dlsv.dsc.nii.ac.jp/idr/stb_yoshiyuki-s@hotmail.co.jp/158c402d9e8c6f17/nicocomm/data.20161216/comment/"

    def __init__(self, base_dir):
        self.base_dir = base_dir

    def download_archive(self, filename):
        filepath = self.base_dir + filename
        if os.path.isfile(filepath):
            print("File already exists")
            return True

        url = self.__archive_base_url + filename
        try:
            print("Download: " + url + "to" + filepath)
            urllib.request.urlretrieve(url, filepath)
            return True
        except urllib.error.HTTPError:
            print("No Archive")
            return False

    def unzip_archive(self, src, dest):
        srcpath = self.base_dir + src
        destpath = self.base_dir + dest
        if os.path.isfile(destpath):
            print("Already unziped")
            return True
        zip = zipfile.ZipFile(srcpath, 'r')
        zip.extractall(destpath)
        zip.close()
