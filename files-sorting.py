# script to sort the file folderwise
# I once had a issue with my download folder for sorting the files in their respective folders, so i created this script

import os
import glob
import shutil

# global variables
basepath = os.getcwd() + "/"
filenames = glob.glob(basepath + "*")

# main folders
document_folder = basepath + "Documents"
media_folder = basepath + "Media"
video_folder = basepath + "Media/Videos"
images_folder = basepath + "Media/Images"
music_folder = basepath + "Media/Music"
setup_folder = basepath + "Setups"
webfiles_folder = basepath + "Web Files"
compressed_folder = basepath + "Compressed"
main_folders = [document_folder, media_folder, video_folder, images_folder, music_folder, setup_folder, webfiles_folder, compressed_folder]

#files lists
documents_list = ['.doc', '.docx', '.pdf', '.pptx', '.txt']
videos_list = ['.mp4', '.3gp', '.mkv']
music_list = ['.mp3']
images_list = ['.jpeg', '.jpg', '.gif', '.svg', '.jfif', '.png', '.brd']
setups_list = ['.exe', '.apk', '.msi']
webfiles_list = ['.html', '.css', '.js', '.php', '.csv']
compressed_list = ['.zip', '.rar', '.giz']

# making main folders
def make_main_folders():
    for main_folder in main_folders:
        if(os.path.exists(main_folder) == False):
            os.mkdir(main_folder)
    
    # Task Complete
    print("folders created succesfully")

# rename and move files into folders
def move_file_into_folders(folderpath, filename):
    count = 0
    if(os.path.exists(folderpath + "/" + os.path.basename(filename))):
        newfilename = os.path.basename(filename)
        while(os.path.exists(folderpath + "/" + newfilename)):
            count += 1
            if(count >= 2):
                temp = os.path.splitext(newfilename)[0]
                newfilename = temp[:-3] +  "(" + str(count) + ")" + os.path.splitext(newfilename)[1]
            else:
                newfilename = os.path.splitext(newfilename)[0] + "-copy(" + str(count) + ")" + os.path.splitext(newfilename)[1]
        os.rename(filename, basepath + newfilename)
        shutil.move(newfilename, folderpath)
    else:
        shutil.move(filename, folderpath)

# make main folders(function call) 
make_main_folders()

for filename in filenames:
    # Documents
    if(os.path.splitext(filename)[1] in documents_list):
        move_file_into_folders(main_folders[0], filename)

    # Videos
    elif(os.path.splitext(filename)[1] in videos_list):
        move_file_into_folders(main_folders[2], filename)

    # Images
    elif(os.path.splitext(filename)[1] in images_list):
        move_file_into_folders(main_folders[3], filename)

    # Music
    elif(os.path.splitext(filename)[1] in music_list):
        move_file_into_folders(main_folders[4], filename)

    # Setups
    elif(os.path.splitext(filename)[1] in setups_list):
        move_file_into_folders(main_folders[5], filename)

    # Web Files
    elif(os.path.splitext(filename)[1] in webfiles_list):
        move_file_into_folders(main_folders[6], filename)

    # Compressed
    elif(os.path.splitext(filename)[1] in compressed_list):
        move_file_into_folders(main_folders[7], filename)

#complete
print("complete")
