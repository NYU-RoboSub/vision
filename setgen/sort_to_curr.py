import sys
import os
import glob
import shutil

def sort_raw(dir: str):
    if not os.path.exists(dir):
        print(f"Directory does not exist: {dir}")
        exit(1)
    # generate a random id
    # make all the directories we need
    os.mkdir(f'../data/{id}')
    os.mkdir(f'../data/{id}/images')
    os.mkdir(f'../data/{id}/labels')
    # go through all files in the raw dir
    for f in glob.glob(dir + "/*"):
        if f.endswith(".jpeg"):
            shutil.move(f, f'../data/curr/images/')
            print(f"moved {f} to -> ../data/curr/images/")
        elif f.endswith(".txt"):
            shutil.move(f, f'../data/curr/labels/')
            print(f"moved {f} to -> ../data/curr/labels/")

if __name__ == "__main__":
    dir = sys.argv[1] if len(sys.argv) > 1 == 0 else '../raw/'
    sort_raw(dir)


