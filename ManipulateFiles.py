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
        subfolders_list = []
        path = os.scandir(path)
        for subfolders in path:
            if not subfolders.is_file():
                    subfolders_list.append(subfolders.name)
        return subfolders_list

    def createSubfolders(path, destination):
        has_subfolder = False        
        subfolders = ManipulateFiles.listSubfolders(path)

        for objects in subfolders:            
            if objects == destination:
                has_subfolder = True
                
        if(not has_subfolder):
            os.mkdir(f"{path}/{destination}")

        return

    def moveFiles(path, file, destination):
        os.rename(f"{path}/{file}", f"{path}/{destination}/{file}")
        return    