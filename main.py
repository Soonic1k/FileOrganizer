import sys

from ManipulateFiles import ManipulateFiles
from CreateFolderList import CreateFolderList
from ArgvListener import ArgvListener

def main():

    path = ArgvListener.Listener(sys.argv)

    files = ManipulateFiles.listFiles(path[1])
    folders = CreateFolderList.folderList(files, path[2])

    for folder in folders:
        ManipulateFiles.createSubfolders(path[1], folder)

    for file, folder in zip(files, folders):
        ManipulateFiles.moveFiles(path[1], file, folder)


if __name__ == "__main__":
    main()