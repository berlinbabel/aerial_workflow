import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
from shapely.affinity import rotate

# --- Constants ---
IMAGE_WIDTH = 5280  # pixels
IMAGE_HEIGHT = 3956  # pixels
SENSOR_WIDTH_MM = 13.2  # mm (DJI typical sensor width)
EPSG_CODE = 28350  # GDA94 / MGA Zone 50

# --- Load CSV ---
df = pd.read_csv(r"D:\_RPA_Processing\Stage1\csv\exif_output3.csv")

# Remove rows without GPS coordinates
df = df.dropna(subset=["GPSLatitude", "GPSLongitude"])

# --- Calculate GSD ---
# 0.3048 converts to metres!
pixel_size_m = (SENSOR_WIDTH_MM / IMAGE_WIDTH) / 1000
df["GSD"] = ((df["AbsoluteAltitude"] * 0.3048) * pixel_size_m) / df["FocalLength"]

# --- Compute real-world footprint dimensions ---
df["FootprintWidth_m"] = IMAGE_WIDTH * df["GSD"]
df["FootprintHeight_m"] = IMAGE_HEIGHT * df["GSD"]

# --- Create polygons ---
polygons = []
points = []
for _, row in df.iterrows():
    lon, lat = row["GPSLongitude"], row["GPSLatitude"]
    yaw = row["FlightYawDegree"]
    width = row["FootprintWidth_m"] * 1000
    height = row["FootprintHeight_m"] * 1000

    # Convert center point to projected coordinates
    center_gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lon], [lat]), crs="EPSG:4326").to_crs(epsg=EPSG_CODE)
    cx, cy = center_gdf.geometry.iloc[0].x, center_gdf.geometry.iloc[0].y

    # Create rectangle footprint
    half_w, half_h = width / 2, height / 2
    rect = Polygon([
        (cx - half_w, cy - half_h),
        (cx + half_w, cy - half_h),
        (cx + half_w, cy + half_h),
        (cx - half_w, cy + half_h)
    ])

    # Rotate rectangle by yaw
    rotated_rect = rotate(rect, yaw, origin=(cx, cy), use_radians=False)
    polygons.append(rotated_rect)
    points.append(center_gdf.geometry.iloc[0])  # Store center point

# --- Build GeoDataFrames ---
gdf_polygons = gpd.GeoDataFrame(
    df[["SourceFile", "FileName", "AbsoluteAltitude", "FocalLength", "FlightYawDegree", "GSD", "FootprintWidth_m", "FootprintHeight_m"]],
    geometry=polygons,
    crs=f"EPSG:{EPSG_CODE}"
)

gdf_points = gpd.GeoDataFrame(
    df[["SourceFile", "FileName", "AbsoluteAltitude", "FocalLength", "FlightYawDegree"]],
    geometry=points,
    crs=f"EPSG:{EPSG_CODE}"
)

# --- Save both layers to GeoPackage ---
out_path = r"D:\_RPA_Processing\Stage1\out\image_footprints10.gpkg"
gdf_polygons.to_file(out_path, layer="footprints", driver="GPKG")
gdf_points.to_file(out_path, layer="image_centers", driver="GPKG")

print("GeoPackage created with two layers: footprints and image_centers")
