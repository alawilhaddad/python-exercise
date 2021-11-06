import os
if __name__ == "__main__":
    file_path = '89_char_count.txt'

    if os.path.isfile(file_path):
        print(f"The file {file_path} exists")
    else:
        print(f"The file {file_path} doesn't exist")
