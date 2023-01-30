import re

class ArgvListener():
    def __init__(self):
        pass

    def Listener(path):

        path[1] = re.sub(r"\\", "/", path[1])
        if(path[1] == "Prefix"):
            path[1] = True
        elif(path[1] == "Suffix"):
            path[1] = False
                
        return path
