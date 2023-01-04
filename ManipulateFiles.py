import os

class ManipulateFiles:
    def __init__(self, folder):
        self.folder = folder
        #transformar as listas em variáreis e declará-las Null no construtor

    def listFiles(self):
        files_list = list()
        for files in os.scandir(self.folder):
            if files.is_file():
                    files_list.append(files.name)
        return files_list
 
    def listSubfolders(self):
        files_list = list()
        for files in os.scandir(self.folder):
            if not files.is_file():
                    files_list.append(files.name)
        return files_list

    def creatSubfolders(self):
        pass

    def moveFiles(self, destination):
        pass