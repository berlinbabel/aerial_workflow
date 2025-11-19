# Create Photo Points

The following workflow will create a point shape file from the image exif data.

### Prerequisites

1. Python

2. Exiftool https://exiftool.org


#### Step 1

Copy and edit the following to include paths as described above in some text editor.
<pre>exiftool.exe -n -csv PATH_TO_IMAGES > PATH_TO_CSV_FILE\exif_output.csv</pre>

#### Step 2

Run the exif script that you edited above in CMD.

If you have not added Exiftool to PATH, then you will need to include path (in text string from above) like this;

C:\Exiftool\exiftool.exe -n ...

#### Step 3

Open python file named scripts/get_photo_points.py and edit paths.

#### Step 4

Run python script named scripts/get_photo_points.py

#### Step 5
View results in GIS!

![Badge Description](https://img.shields.io/github/last-commit/berlinbabel/aerial_workflow)
