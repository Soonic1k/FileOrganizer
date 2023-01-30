import os

class ManipulateFiles:
    def __init__(self, folder):
        self.folder = folder

    def listFiles(path):
        files_list = []
        path = os.scandir(path)
        for files in path:
            if files.is_file():
                    files_list.append(files.name)
        return files_list
 
    def listSubfolders(path):
        files_list = []
        path = os.scandir(path)
        for files in path:
            if not files.is_file():
                    files_list.append(files.name)
        return files_list

    def createSubfolders(path, destination):
        #fullPath = os.scandir(path)
        has_subfolder = False

        for files in path:
            if files == destination:
                has_subfolder = True
                
        if(not has_subfolder):
            os.mkdir(f"{path}/{destination}")

        return

    def moveFiles(path, file, destination):
        os.rename(f"{path}/{file}", f"{path}/{destination}/{file}")
        return    