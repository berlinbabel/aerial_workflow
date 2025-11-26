import pandas as pd
import shutil
import os

# Paths for source and destination folders
source_folder = r"D:\_RPA_Processing\Stage1\1-RGB"
destination_folder = r"D:\_RPA_Processing\Stage2\WECW010026-5\img"

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Read the CSV file
csv_file = r"D:\_RPA_Processing\Stage2\WECW010026\cornwall-5.csv"
df = pd.read_csv(csv_file)

# Extract the FileName column
file_names = df['FileName'].dropna().tolist()

# Initialize counters
copied_count = 0
missing_files = []

# Copy files from source to destination
for file_name in file_names:
    src_path = os.path.join(source_folder, file_name)
    dest_path = os.path.join(destination_folder, file_name)
    
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        copied_count += 1
    else:
        missing_files.append(file_name)

# Print summary
print(f"Total files to copy: {len(file_names)}")
print(f"Successfully copied: {copied_count}")
print(f"Missing files: {len(missing_files)}")

# Save missing files list to a text file
with open("missing_files.txt", "w") as f:
    for mf in missing_files:
        f.write(mf + "\n")
