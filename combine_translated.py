import os
import glob
import sys
import subprocess
import re

# Add a command-line argument for force replace
force_replace = False
if len(sys.argv) > 1 and sys.argv[1] == '--force':
    force_replace = True
    print("Force replace mode enabled.")

# Get all translated chunk files sorted by chunk number
translated_files = sorted(glob.glob('vi_translated/chunk_*.txt'), 
                         key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))

# Prepare the output file
output_file = 'vi_translated_combined.txt'
combined_content = ""  # Use a string instead of a list for easier newline handling

print(f"Found {len(translated_files)} files to combine:")
for file_path in translated_files:
    print(f"  - {file_path}")

# Read and combine all translated chunks
for i, file_path in enumerate(translated_files):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        # Remove trailing whitespace and ensure content ends with a newline
        file_content = file_content.rstrip() + "\n"
        
        # Add an extra newline between files (except for the first file)
        if i > 0:
            combined_content += "\n"
            
        combined_content += file_content
        
        # Count lines for reporting
        line_count = file_content.count('\n')
        print(f"Added {line_count} lines from {file_path}")

# Remove empty lines from the combined content
print("\nRemoving empty lines...")
# Use regex to replace multiple consecutive newlines with a single newline
combined_content = re.sub(r'\n\s*\n', '\n', combined_content)
print("Empty lines removed.")

# Write the combined content to the output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(combined_content)

# Get line count
total_lines = combined_content.count('\n')
print(f"\nCombined {len(translated_files)} files into {output_file}")
print(f"Total lines in combined file: {total_lines}")

# Also verify with wc -l for accuracy
def get_line_count(file_path):
    result = subprocess.run(['wc', '-l', file_path], capture_output=True, text=True)
    return int(result.stdout.strip().split()[0])

wc_line_count = get_line_count(output_file)
print(f"Line count verification (wc -l): {wc_line_count} lines")

print(f"\nSuccessfully created combined file: {output_file}") 