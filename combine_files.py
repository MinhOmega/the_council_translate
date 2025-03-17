import os
import glob
import sys
import subprocess
import re

def combine_files(folder_name, force_replace=False):
    # Check if folder exists
    if not os.path.isdir(folder_name):
        print(f"Error: Folder '{folder_name}' does not exist.")
        sys.exit(1)
    
    # Get all chunk files sorted by chunk number
    translated_files = sorted(glob.glob(f'{folder_name}/chunk_*.txt'), 
                             key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))
    
    if not translated_files:
        print(f"Error: No chunk files found in '{folder_name}'.")
        sys.exit(1)
    
    # Prepare the output file
    output_file = f'{folder_name}_combined.txt'
    
    # Check if output file already exists and handle force replace
    if os.path.exists(output_file) and not force_replace:
        print(f"Output file '{output_file}' already exists. Use --force to overwrite.")
        sys.exit(1)
    
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
    wc_line_count = get_line_count(output_file)
    print(f"Line count verification (wc -l): {wc_line_count} lines")
    
    print(f"\nSuccessfully created combined file: {output_file}")

def get_line_count(file_path):
    result = subprocess.run(['wc', '-l', file_path], capture_output=True, text=True)
    return int(result.stdout.strip().split()[0])

if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 combine_files.py <folder_name> [--force]")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    force_replace = "--force" in sys.argv
    
    if force_replace:
        print("Force replace mode enabled.")
    
    combine_files(folder_name, force_replace) 