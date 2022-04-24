import sys
import os
import glob
import shutil
import uuid

def sort_raw(dir: str) -> str:
    if not os.path.exists(dir):
        print(f"Directory does not exist: {dir}")
        exit(1)
    # generate a random id
    id = str(uuid.uuid4())
    # make all the directories we need
    os.mkdir(f'../data/{id}')
    os.mkdir(f'../data/{id}/images')
    os.mkdir(f'../data/{id}/labels')
    # go through all files in the raw dir
    for f in glob.glob(dir + "/*"):
        if f.endswith(".jpg"):
            shutil.move(f, f'../data/{id}/images/')
            print(f"moved {f} to -> ../data/{id}/images/")
        elif f.endswith(".txt"):
            shutil.move(f, f'../data/{id}/labels/')
            print(f"moved {f} to -> ../data/{id}/labels/")
    return id

if __name__ == "__main__":
    dir = sys.argv[1] if len(sys.argv) > 1 == 0 else '../raw/'
    sort_raw(dir)


