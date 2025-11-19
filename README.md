# Aerial Workflow
Tips and tricks for processing aerial aquired images.

## Create photopoints from photo exif data

The following workflow will create a point shape file from the image exif data.

### Prerequisites
<pre>
Python
Exiftool (https://exiftool.org/)
</pre>

#### Step 1

PATH_TO_IMAGES - Location of images

PATH_TO_CSV_FILE - Location to write csv file

C:\Exiftool\exiftool.exe -n -csv PATH_TO_IMAGES > PATH_TO_CSV_FILE\exif_output.csv

#### Step 2

Open python file named Scripts/get_photo_points.py and edit paths.

#### Step 3

Run python script named Scripts/get_photo_points.py

![Badge Description](https://img.shields.io/github/last-commit/berlinbabel/aerial_workflow)
