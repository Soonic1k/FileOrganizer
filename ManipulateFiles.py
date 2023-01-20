import os

class ManipulateFiles:
    def __init__(self, folder):
        self.folder = folder

    def listFiles(self):
        files_list = list()
        path = os.scandir(self.folder)
        for files in path:
            if files.is_file():
                    files_list.append(files.name)
        return files_list
 
    def listSubfolders(self):
        files_list = list()
        path = os.scandir(self.folder)
        for files in path:
            if not files.is_file():
                    files_list.append(files.name)
        return files_list

    def creatSubfolders(self):
        pass

    def moveFiles(self, destination):
        pass