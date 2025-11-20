# Create GSD footprint

## Step 1
<pre>C:\Exiftool\exiftool.exe -n -csv -filename -AbsoluteAltitude -FlightYawDegree -FocalLength -gpslatitude -gpslongitude D:\_RPA_Processing\Stage1\1-RGB\*.jpg > D:\_RPA_Processing\Stage1\exif_output.csv</pre>

## Step 2
Run python script named scripts/create_gsd_footprint.py
