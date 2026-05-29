import os

def rename_files(folder_path, prefix):
    files = os.listdir(folder_path)
    count = 1
    for file in files:

        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file)

        new_name = f"{prefix}_{count}{extension}"

        new_path = os.path.join(folder_path, new_name)

        os.rename(file_path, new_path)

        count += 1
    print("Files renamed successfully!")
    print("\nFiles after renaming:")

