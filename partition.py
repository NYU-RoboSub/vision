import glob
import os
import sys

def partition(set: str) -> None:
    current_dir = f"./data/{set}/images"
    split_pct = 10;
    file_train = open(f"data/{set}/train.txt", "w")  
    file_val = open(f"data/{set}/val.txt", "w")  
    counter = 1  
    index_test = round(100 / split_pct)  
    for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpeg")):  
            title, ext = os.path.splitext(os.path.basename(pathAndFilename))
            if counter == index_test:
                    counter = 1
                    file_val.write(current_dir + "/" + title + '.jpeg' + "\n")
            else:
                    file_train.write(current_dir + "/" + title + '.jpeg' + "\n")
                    counter = counter + 1
    file_train.close()
    file_val.close()

if __name__ == "__main__":
    set = sys.argv[1]
    partition(set)
