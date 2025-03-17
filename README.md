# File Translation Workflow

This repository contains scripts to help with translating large text files while maintaining the same line count.

## Scripts Overview

- `split_file.py`: Splits a file into manageable chunks based on command-line arguments
- `combine_translated.py`: Combines translated chunks back into a single file
- `split_and_combine.py`: Legacy script with hardcoded paths (maintained for backward compatibility)

## Steps to Translate

1. **Split the file into chunks**:
   ```
   python split_file.py <file_path> [chunk_size]
   ```
   For example:
   ```
   python split_file.py vi/q4_loc_en_0.txt 100
   ```
   This will:
   - Create a directory named after the file (without extension): `q4_loc_en_0`
   - Split the file into chunks of 100 lines each in that directory
   - Create a `translated_q4_loc_en_0` directory for the translated chunks

   Alternatively, you can use the legacy script with hardcoded paths:
   ```
   python split_and_combine.py
   ```

2. **Translate each chunk**:
   - Translate each file in the chunks directory
   - Save the translated files with the same filenames in the translated directory
   - Make sure to maintain the same number of lines in each translated file

3. **Combine the translated chunks**:
   ```
   python combine_translated.py [--force]
   ```
   This will:
   - Combine all translated chunks into a single file
   - Remove empty lines from the combined content
   - Verify the line count using both Python and `wc -l`
   - Create a combined file named `vi_translated_combined.txt`
   - Use the `--force` flag to override safety checks if needed

## Important Notes

- **Maintain line count**: Each translated chunk must have the same number of lines as the original chunk
- **Preserve line breaks**: Do not add or remove line breaks during translation
- **File encoding**: All files use UTF-8 encoding
- **Dynamic folders**: The new scripts create folders based on the filename without extension
- **Chunk size**: You can specify a custom chunk size (default is 100 lines)

## Troubleshooting

- If a file is not found, check that the path is correct
- If the line count doesn't match after translation, review the translated chunks
- Use the `--force` flag with `combine_translated.py` to override safety checks when necessary
- For any issues with the new scripts, ensure you're using the correct command-line arguments 