import os
import sys

def split_file(file_path, chunk_size=100):
    # Extract the base filename without extension to use as folder name
    base_name = os.path.basename(file_path)
    folder_name = os.path.splitext(base_name)[0]
    
    # Create a directory for chunks if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Create a directory for translated chunks if it doesn't exist
    translated_folder = f'translated_{folder_name}'
    if not os.path.exists(translated_folder):
        os.makedirs(translated_folder)
    
    # Read the original file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    
    # Split the file into chunks
    for i in range(0, total_lines, chunk_size):
        chunk_number = i // chunk_size + 1
        end_line = min(i + chunk_size, total_lines)
        
        chunk_filename = f'{folder_name}/chunk_{chunk_number}.txt'
        
        with open(chunk_filename, 'w', encoding='utf-8') as f:
            f.writelines(lines[i:end_line])
        
        print(f'Created {chunk_filename} with lines {i+1}-{end_line}')
    
    print(f'Total chunks created: {(total_lines + chunk_size - 1) // chunk_size}')
    print(f'Total lines in original file: {total_lines}')
    print(f'Now translate each chunk in the "{folder_name}" directory and save the translated files with the same names in the "{translated_folder}" directory.')

if __name__ == "__main__":
    # Check if file path is provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python split_file.py <file_path> [chunk_size]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
    # Optional chunk size argument
    chunk_size = 100  # Default chunk size
    if len(sys.argv) > 2:
        try:
            chunk_size = int(sys.argv[2])
        except ValueError:
            print("Error: Chunk size must be an integer.")
            sys.exit(1)
    
    split_file(file_path, chunk_size)