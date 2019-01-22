import os
import subprocess
folders = os.listdir(".")

for folder in folders:
    if not os.path.isfile(folder) and folder != "venv" and folder != ".idea" and folder != ".git":
        nested_folders = os.listdir(folder)
        for nested_folder in nested_folders:
            subprocess.call(["python", folder + os.sep + nested_folder + os.sep + "test" + ".py"])
