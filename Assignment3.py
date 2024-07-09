import os
import shutil

source_folder = "C:/Users/Atharva/Desktop/Newfolder"
dest_folder = "C:/Users/Atharva/Desktop/Newfolder/dest2"


if not os.path.exists(source_folder):
    print("source folder not exist")
    exit()

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)
    print("Destination folder not exist so created one")

for file in os.listdir(source_folder):
    source_file = os.path.join(source_folder, "test.txt")
    dest_file = os.path.join(dest_folder, "test.txt")

    try:
        shutil.copy2(source_file, dest_file)
    except OSError as e:
        print(f"Error {e}")
