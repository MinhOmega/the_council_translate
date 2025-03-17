import os

# Create a directory for chunks if it doesn't exist
if not os.path.exists('chunks'):
    os.makedirs('chunks')

# Create a directory for translated chunks if it doesn't exist
if not os.path.exists('translated_chunks'):
    os.makedirs('translated_chunks')

# Read the original file
with open('en/q4_loc_en_0.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define the number of lines per chunk
chunk_size = 100
total_lines = len(lines)

# Split the file into chunks
for i in range(0, total_lines, chunk_size):
    chunk_number = i // chunk_size + 1
    end_line = min(i + chunk_size, total_lines)
    
    chunk_filename = f'chunks/chunk_{chunk_number}.txt'
    
    with open(chunk_filename, 'w', encoding='utf-8') as f:
        f.writelines(lines[i:end_line])
    
    print(f'Created {chunk_filename} with lines {i+1}-{end_line}')

print(f'Total chunks created: {(total_lines + chunk_size - 1) // chunk_size}')
print(f'Total lines in original file: {total_lines}')
print('Now translate each chunk in the "chunks" directory and save the translated files with the same names in the "translated_chunks" directory.') 