import os
import shutil
from PIL import Image

def separate_images_and_videos(root_folder, image_folder, video_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            # Check if the file is an image
            try:
                img = Image.open(file_path)
                img.close()
                shutil.move(file_path, os.path.join(image_folder, filename))
            except (IOError, OSError):
                # If it's not an image, check if it's a video (you may need to customize this check)
                video_extensions = ['.mp4', '.avi', '.mkv', '.m4v', '.mov']
                if any(filename.lower().endswith(ext) for ext in video_extensions):
                    shutil.move(file_path, os.path.join(video_folder, filename))

# Input folders from the user
root_folder = input("Root folder: ")
image_folder = input("Enter the image folder path: ")
video_folder = input("Enter the video folder path: ")

# Make sure the folders exist
os.makedirs(image_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)

separate_images_and_videos(root_folder, image_folder, video_folder)
