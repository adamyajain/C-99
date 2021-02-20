import os
import shutil

''' 
Write The Name Of Directory
that has to be sorted
'''
path = input("Enter the name of directory to be sorted :- ")

''' 
This will create an Organized
list with all the filenames
there in the directory
'''
list_of_files = os.listdir(path)

#this will go through each file
for file in list_of_files:
    name, ext = os.path.splitext(file)

    ext = ext[1:]

    if ext == '' :
        continue

    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file + '/' + ext + '/' + file)

    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/' + file)
