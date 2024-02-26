#!/bin/bash

# Define the source and destination paths
source_path="$HOME/Downloads/apache-access.log"
destination_path="./apache-access.log"

# Check if the file exists in the Downloads directory
if [ -f "$source_path" ]; then
    # Copy the file to the current directory
    cp "$source_path" "$destination_path"
    echo "File copied successfully!"
else
    echo "Error: File not found in Downloads directory."
fi

