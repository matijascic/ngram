


import os

if __name__ == "__main__":

    DIR="./shakespeare-dataset/"
    rel_path_files = [DIR+file for file in os.listdir(DIR)]
    print(rel_path_files)

    