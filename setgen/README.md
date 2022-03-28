# Data Set Generation & Manipulation

### Features to implement

- [x] Sort Raw Datasets
- [ ] Manipulation of Image and Label
- [ ] Verification
- [ ] Partition


------------
## Features

### Sort Raw Datasets

given a folder `./raw`, containing files of types jpeg(image) and txt(label). generate a new output folder named `{idx}` where idx is the version of the set containing 2 directories images and labels. Where images contains all images and labels all labels.

**Input:**
```
raw
│   01.jpeg
│   01.txt
│   02.jpeg
│   02.txt   
│   03.jpeg
│   03.txt   
│   04.jpeg
│   04.txt   
│   05.jpeg
│   05.txt   
... etc

```

**Produces:**
```
0.1
└───labels
|    │   01.txt
|    │   02.txt
|    │
|    |   ...etc
└───images
    │   01.jpeg
    │   02.jpeg
    |   ...etc
```

### Manipulation of Image & Label

Given an image ex: `img01.jpeg`, apply some manipulation/filter to it to produce another image `img01_rotated_60.jpeg`. 

For each image if possible apply same function for manipulation on labels.

Should be done in place and not create a whole new version of the data set.

### Verification 

Given an image `img01.jpeg` and its labels `img01.txt`. Plot the image and the bounding box for inspection.

### Partitioning

Given a folder containing images generate two `.txt` files: `val.txt`, `train.txt`. These files will contain a list of the **relative path** to a corresponding image in the `./images` folder. 

If it is a 90-10 split for training-validation. It should split the set of images and put 90% of paths into train.txt and the other 10 into val.txt

ex: 
```
# example of train.txt
./data/0.1/images/A2374EA1-6D3D-454B-AD78-953150A67DD1.jpeg
./data/0.1/images/D294EC3B-A01C-4052-9135-21172E28FF26.jpeg
./data/0.1/images/A40FBA0F-E71A-4AFF-B3DE-3159E3FB8CC0.jpeg
./data/0.1/images/6D0DFA4B-CE9E-49DD-9DBF-369A86F76280.jpeg
./data/0.1/images/5B930572-D15B-4CE2-AB47-633A2BC4BC43.jpeg
./data/0.1/images/DB3A51F4-B12A-4BEC-AD12-164AC56A3D64.jpeg
./data/0.1/images/F41301A9-9EBB-4A39-ABAC-959F5222E6FE.jpeg
./data/0.1/images/A8AA3BEB-A770-4EF1-B8AD-912516074171.jpeg
./data/0.1/images/100FF6D8-E4F7-433B-872E-8FA3362AC497.jpeg
./data/0.1/images/F901EF79-DEC4-4DD4-BF44-E4A257E3E71E.jpeg
./data/0.1/images/F12F6F48-3265-43A1-9C71-2F76CF9ECF67.jpeg
./data/0.1/images/9C71A6DA-8706-4F87-A10B-40EE5A9E697C.jpeg
./data/0.1/images/AD982DC1-F5C2-48D7-A512-2C24CA24B673.jpeg
./data/0.1/images/1698608D-0AD7-4C34-916E-6AC2F16DA75A.jpeg
./data/0.1/images/376D7799-D1DF-4004-A46C-EAD94BE20C1B.jpeg
./data/0.1/images/939323B4-1E34-4576-9061-213718334096.jpeg
```
