import sys
import os
import glob
import shutil
import uuid

def sort_raw(dir: str) -> None:
    if not os.path.exists(dir):
        print(f"Directory does not exist: {dir}")
        return
    id = str(uuid.uuid4())
    os.mkdir(f'../data/{id}')
    os.mkdir(f'../data/{id}/images')
    os.mkdir(f'../data/{id}/labels')
    for f in glob.glob(dir + "/*"):
        if f.endswith(".jpeg"):
            shutil.move(f, f'../data/{id}/images/')
            print(f"moved {f} to -> ../data/{id}/images/")
        elif f.endswith(".txt"):
            shutil.move(f, f'../data/{id}/labels/')
            print(f"moved {f} to -> ../data/{id}/labels/")

if __name__ == "__main__":
    dir = sys.argv[1] if len(sys.argv) > 1 == 0 else '../raw/'
    sort_raw(dir)


