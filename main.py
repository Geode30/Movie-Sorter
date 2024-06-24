import os
import shutil

try:
    folder_path = 'D:\MOVIES'
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and (f.endswith('.mp4') or f.endswith('.mkv'))]
    for file_name in file_names:
        movie_name = os.path.splitext(file_name)[0]
        file_path = os.path.join(folder_path, file_name)
        destination_folder = os.path.join(folder_path, movie_name)
        os.makedirs(destination_folder)
        shutil.move(file_path, destination_folder)
except Exception as e:
    print(f"An error occurred {e}")
else:
    if not file_names:
        print("No files found")
    else:
        print(f"Files ({len(file_names)}) have been successfully organized into their own folders")