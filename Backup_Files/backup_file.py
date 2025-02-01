# Problem statement:
# Backup all the files in given directory with format <filename>-YYYY-MM-DD.txt
# Eg: abc.txt should be renamed as abc-2010-12-01.txt

import os
from datetime import datetime
import sys

directory = 'files'
date_format = datetime.now().strftime('%Y-%m-%d')

try:
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    file_names = os.listdir(directory)
    if not file_names:
        print(f"No files found in directory '{directory}'. Exiting the code.")
        sys.exit()

    for filename in file_names:
        absolute_file_path = os.path.join(directory, filename)

        if os.path.isdir(absolute_file_path):
            print(f"Skipping '{filename}' (not a file).")
            continue

        new_file_name = f"{filename[:-4]}-{date_format}.txt"
        new_absolute_file_path = os.path.join(directory, new_file_name)

        try:
            os.rename(absolute_file_path, new_absolute_file_path)
            print(f"Renamed '{filename}' -> '{new_file_name}'")
        except OSError as e:
            print(f"Error renaming file {absolute_file_path} : {e}")

except FileNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
