import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# 1. Read the CSV file
csv_file = r"path_to_csv_file\exif_output.csv"  # Replace with your file path
df = pd.read_csv(csv_file)

# 2. Create geometry from X and Y columns
geometry = [Point(xy) for xy in zip(df['GPSLatitude'], df['GPSLongitude'])]

# 3. Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")  # WGS84 CRS

# 4. Save to a shapefile
output_file = r"path_to_shp_file\points.shp"
gdf.to_file(output_file)

print(f"Shapefile created: {output_file}")
