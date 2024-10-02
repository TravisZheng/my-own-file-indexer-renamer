import os
import re

def rename_files(file_path, txt_path):
    # Read the txt file line by line
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        # Remove BOM if present
        if lines[0].startswith('\ufeff'):
            lines[0] = lines[0][3:]
    new_names = {int(line.split('_')[0]): line for line in lines}

    for filename in os.listdir(file_path):
        if not filename.startswith('.'): # Ignore hidden files/directories on mac
            prefix_number = int(re.search(r'\d+', filename).group())
            if prefix_number in new_names:  # If a matching entry exists in the txt file
                old_name = os.path.join(file_path, filename)
                new_name = os.path.join(file_path, f"{new_names[prefix_number]}{filename[-4:]}") # -4 to get extension including dot
                os.rename(old_name, new_name)
                print(f'Renamed {old_name} -> {new_name}')   # Print the operation for verification

# Provide the path of directory where files are located and the txt file here
rename_files('P:/12', 'file_index_utf8.txt')
