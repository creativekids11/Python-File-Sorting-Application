import os,shutil

folders={
    'videos':[".mp4", ".avi", ".mpeg4", ".3gp", ".gifv", ".ogg", ".webm", ".mkv", ".flv"],
    'audios':[".amr", ".mp3", ".wav", ".m4a", ".wv", ".ape"],
    'images':[".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".webp", ".svg"],
    'documents':[".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".xml", ".pdf", ".rtf", ".txt", ".odt", ".htm", ".html", ".sxw", ".tex", ".wpd", ".zip", ".rar", ".7z", ".7zip"],
    'app':[".exe", ".msi", ".dmg", ".cmd", ".bat", ".jar"],
    }

"""print(folders)
for folder_name in folders:
    print(folder_name, folders[folder_name])
"""


def rename_folder():
    for folder in os.listdir(directry):
        if os.path.isdir(os.path.join(directry,folder))==True:
            os.rename(os.path.join(directry,folder),os.path.join(directry,folder.lower()))

def create_move(ext,file_name):
    find=False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            #print("found", folder_name)
            if folder_name not in os.listdir(directry):
                os.mkdir(os.path.join(directry,folder_name))
            shutil.move(os.path.join(directry,file_name),os.path.join(directry,folder_name))
            find=True
            break
    if find!=True:
        if other_name not in os.listdir(directry):
            os.mkdir(os.path.join(directry,other_name))
        shutil.move(os.path.join(directry,file_name),os.path.join(directry,other_name))

directry=input("loc:")
other_name=input("o:")
rename_folder()
all_files=os.listdir(directry)
length=len(all_files)
count=1
#print(all_files)


for i in all_files:
    #print(i)
    if os.path.isfile(os.path.join(directry,i))==True:
        #print("yes")
        create_move(i.split(".")[-1],i)
    print(f"Total Files: {length} | Done: {count} | Left: {length-count}")
    count+=1

