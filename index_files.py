import os
import glob

# Define the folder to index
INDEX_FOLDER = 'C:/your/folder'

# Get a list of all files in the folder and its subdirectories
files = sorted(glob.glob(os.path.join(INDEX_FOLDER, '*.*')))

# Save the index result to a .txt file
with open("file_index.txt", "w") as f:
    for file in files:
        base_name, extension = os.path.splitext(os.path.basename(file))
        line = f"{base_name}{extension}\n"
        f.write(line)

print("File index saved to 'file_index.txt'")
