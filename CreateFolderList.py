import re

class CreateFolderList:
    def __init__(self):
        pass

    def folderList(list, prefix_suffix):
        
        folder_list = []

        pattern = r"(?P<prefix>_(.*))(?P<suffix>(.*)_)"
        

        if(prefix_suffix):
            pattern = r"_(.*)"
        else:
            pattern = r"(.*)_"
            extension = r"\.(.*)$"

        recompiled = re.compile(pattern)

        for files in list:
            shortener = recompiled.sub("", files)

            if shortener is None:
                folder_list.append("WithoutMatch")
            elif(prefix_suffix):
                folder_list.append(shortener)
            elif(not prefix_suffix):
                shortener = re.sub(extension, "", shortener)
                folder_list.append(shortener)


        return folder_list


