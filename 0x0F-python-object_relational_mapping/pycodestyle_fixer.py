#!/usr/bin/python3
import pycodestyle
import autopep8
import sys
import os

# Set the path to the directory containing the Python files to be checked
path = 'path/to/directory'

# Define a function to check the coding style of a file and fix the mistakes
def check_and_fix_file(filename):
    # Check the coding style of the file and get a report
    style_guide = pycodestyle.StyleGuide()
    report = style_guide.check_files([filename])

    # If the report has errors, fix them using autopep8
    if report.total_errors > 0:
        print(f"Fixing style errors in {filename}...")
        autopep8.fix_file(filename, options={'aggressive': 2, 'max_line_length': 120})
    else:
        print(f"No style errors found in {filename}")

# Loop through all the Python files in the specified directory and check their style
for filename in os.listdir(path):
    if filename.endswith('.py'):
        full_path = os.path.join(path, filename)
        check_and_fix_file(full_path)

print("Done!")
