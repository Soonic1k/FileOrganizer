


class ArgvListener():
    def __init__(self):
        pass

    def Listener(path):
        print("log")
        resultPath = path[1]
        fix = True

        if(path[2] == "Prefix"):
            resultPath[2] = True
        elif(path[2] == "Suffix"):
            resultPath[2] = False
                
        return resultPath
