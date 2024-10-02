import os


def add_prefix_to_file_names(folder_path: str) -> None:
    """
    Add a prefix to the name of each file in a pre-defined folder.

    Args:
        folder_path (str): The path to the folder containing the files.
    """

    # Get a list of all files in the folder
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Initialize the prefix counter
    prefix_counter = 1

    # Iterate over each file and add the prefix to its name
    for i, file_name in enumerate(file_names):
        new_file_name = f"{prefix_counter:04}_{file_name}"

        # Rename the file to its new name
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

        # Increment the prefix counter only after renaming a file
        prefix_counter += 1


if __name__ == "__main__":
    folder_path = "C:/your/folder"

    add_prefix_to_file_names(folder_path)
