# Create GSD footprint

## Step 1
<pre>C:\Exiftool\exiftool.exe -n -csv -filename -AbsoluteAltitude -FlightYawDegree -FocalLength -gpslatitude -gpslongitude D:\_RPA_Processing\Stage1\1-RGB\*.jpg > D:\_RPA_Processing\Stage1\exif_output.csv</pre>

## Step 2
Run python script named scripts/create_gsd_footprint.py

## Work in progress to assign run attribute
<pre>C:\Exiftool\exiftool.exe -n -csv -filename GPSImgDirection -AbsoluteAltitude -FlightYawDegree -FocalLength -gpslatitude -gpslongitude -DateTimeOriginal -FlightPitchDegree -FlightRollDegree -RelativeAltitude -FlightXSpeed -FlightYSpeed -FlightZSpeed D:\_RPA_Processing\Stage1\1-RGB\*.jpg > D:\_RPA_Processing\Stage1\csv\exif_output3.csv
</pre>
