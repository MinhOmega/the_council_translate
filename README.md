# File Translation Workflow

This repository contains scripts to help with translating large text files while maintaining the same line count.

## Scripts Overview

- `split_file.py`: Splits a file into manageable chunks for translation
- `combine_files.py`: Combines translated chunks back into a single file

## Steps to Translate

1. **Split the file into chunks**:
   ```
   python split_file.py <file_path> [chunk_size]
   ```
   For example:
   ```
   python split_file.py document.txt 100
   ```
   This will:
   - Create a directory named after the file (without extension): `document`
   - Split the file into chunks of 100 lines each in that directory
   - Create a `translated_document` directory for the translated chunks

2. **Translate each chunk**:
   - Translate each file in the chunks directory
   - Save the translated files with the same filenames in the translated directory
   - Make sure to maintain the same number of lines in each translated file

3. **Combine the translated chunks**:
   ```
   python combine_files.py <folder_name> [--force]
   ```
   For example:
   ```
   python combine_files.py translated_document --force
   ```
   This will:
   - Combine all translated chunks from the specified folder into a single file
   - Remove empty lines from the combined content
   - Verify the line count using both Python and `wc -l`
   - Create a combined file named `<folder_name>_combined.txt`
   - Use the `--force` flag to override an existing output file if needed

## Important Notes

- **Maintain line count**: Each translated chunk must have the same number of lines as the original chunk
- **Preserve line breaks**: Do not add or remove line breaks during translation
- **File encoding**: All files use UTF-8 encoding
- **Dynamic folders**: The scripts create folders based on the filename without extension
- **Chunk size**: You can specify a custom chunk size (default is 100 lines)

## Troubleshooting

- If a file is not found, check that the path is correct
- If the line count doesn't match after translation, review the translated chunks
- Use the `--force` flag with `combine_files.py` to override an existing output file
- Ensure chunk files follow the naming convention `chunk_*.txt` for the combine script to work properly 