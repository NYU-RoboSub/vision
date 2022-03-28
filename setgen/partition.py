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
        title = os.path.splitext(os.path.basename(pathAndFilename))
        if counter == index_test:
            counter = 1
            file_val.write(f"{current_dir}/{title}.jpeg\n")
        else:
            file_train.write(f"{current_dir}/{title}.jpeg\n")
            counter = counter + 1
    file_train.close()
    file_val.close()

def print_usage() -> None:
    print("Usage: python partition.py <set*> <train_percentage> <val_percentage> \n")
    print("   -- <set> is the name of the set to partition")
    print("   -- <train_percentage> is the percentage of the set to be used for training (default = 90%)")
    print("   -- <val_percentage> is the percentage of the set to be used for validation (default = 10%)")


if __name__ == "__main__":
    if  len(sys.argv) <= 1:
        print_usage()
        sys.exit(1)
    elif sys.argv[1] == "--help":
        print_usage()
        sys.exit(1)

    set = sys.argv[1]

    partition(set)
