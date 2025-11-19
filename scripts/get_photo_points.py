import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# 1. Read the CSV file
csv_file = r"PATH_TO_CSV_FILE\exif_output.csv"  # Replace with your file path
df = pd.read_csv(csv_file)

# 2. Create geometry from X and Y columns
geometry = [Point(xy) for xy in zip(df['GPSLatitude'], df['GPSLongitude'])]

# 3. Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")  # WGS84 CRS

# 4. Save to a shapefile
output_file = r"PATH_TO_SHP_FILE\points.shp"
gdf.to_file(output_file)

print(f"Shapefile created: {output_file}")
