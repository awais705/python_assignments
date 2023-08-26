# create 3 folders
# folder_1
# folder_2
# folder_3
# such that folder_3 is inside folder_2 and folder_2 is inside folder_1
# i.e
# folder_1 > folder_2 > folder_3
# see the image folder_structure.png
#
# place some txt files in folder_1 and folder_3
# place your python program in folder_2 and in the program
#
# create 3 functions
# 1. open_folder(path, folder_name)
# 2. move_to_parent_folder(path)
# 3. display_files_and_folder(path)
#
# the task is to
# print all files of folder_3
# print all files of folder_1

# while calling open_folder function you can use hardcoded value for folder_name argument i.e folder_3
# hint: use os.path.join, os.path.abspath, os.getcwd, os.listdir
# no need to use loop


import os


def open_folder(path, folder_name):
    # print(path, folder_name)
    path = os.path.join(path, folder_name)
    abspath = os.path.abspath(path)
    # print(os.listdir(abspath))
    display_files_and_folder(abspath)


def move_to_parent_folder(path):
    path = os.path.join(path, "..")
    abspath = os.path.abspath(path)
    # print(os.listdir(abspath))
    display_files_and_folder(abspath)


def display_files_and_folder(path):
    print(os.listdir(path))


current_working_directory = os.getcwd()
# print(current_working_directory)

files_and_folder_in_dir = os.listdir()
# print(files_and_folder_in_dir)

open_folder(current_working_directory, "folder_3")
move_to_parent_folder(current_working_directory)
