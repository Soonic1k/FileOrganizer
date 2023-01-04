from ManipulateFiles import ManipulateFiles

folder = ManipulateFiles('./')

print("Files:")
for files in folder.listFiles():
    print(files)
print("\n")
print("Folders:")
for files in folder.listSubfolders():
    print(files)