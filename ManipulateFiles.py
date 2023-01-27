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

    def createSubfolders(self, destination):
        path = os.scandir(self.folder)
        has_subfolder = False

        for files in path:
            if files == destination:
                has_subfolder = True
        
        if(not has_subfolder):
            os.mkdir(f"{destination}")

        return

    def moveFiles(self, file, destination):
        os.rename(f"{file}", f"{destination}/{file}")
        return    