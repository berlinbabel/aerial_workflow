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

Edit the following to include paths as described above in some text editor.
<pre>exiftool.exe -n -csv PATH_TO_IMAGES > PATH_TO_CSV_FILE\exif_output.csv</pre>

#### Step 3

Run the exif script that you edited above in CMD.

If you have not added Exiftool to PATH then you will need to include path in script like this;

C:\Exiftool\exiftool.exe -n ...

#### Step 4

Open python file named Scripts/get_photo_points.py and edit paths.

#### Step 5

Run python script named Scripts/get_photo_points.py

![Badge Description](https://img.shields.io/github/last-commit/berlinbabel/aerial_workflow)
