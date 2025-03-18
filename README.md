# File Translation Workflow

This repository contains tools and scripts for translating game text files while maintaining file structure and formatting.

## Tools Overview

### 1. File Splitting and Combining Scripts
Located in `/scripts/`:
- `split_file.py`: Splits large text files into manageable chunks
- `combine_files.py`: Combines translated chunks back into a single file

### 2. The Council CPK Tool
Located in `/fonts_and_textures/tools/The_Council_CPK_Tool_By_Delutto/`:
- Tool for extracting and importing game text files from CPK archives
- Created by Delutto (Tribo Gamer Brasil 2018)

## Translation Workflow

### 1. Extract Game Files
```bash
The_Council_CPK_Tool.exe -e Loca_en_Main_0.cpk Loca_en_Main_0_Files
```

### 2. Split Files for Translation
```bash
python scripts/split_file.py <file_path> [chunk_size]
```
Example:
```bash
python scripts/split_file.py document.txt 100
```

### 3. Translate Chunks
- Translate files in the generated chunks directory
- Save translations in the `translated_[filename]` directory
- Maintain the same line count and formatting

### 4. Combine Translated Chunks
```bash
python scripts/combine_files.py <folder_name> [--force]
```
Example:
```bash
python scripts/combine_files.py translated_document --force
```

### 5. Import Back to Game
```bash
The_Council_CPK_Tool.exe -i Loca_en_Main_0.cpk Loca_en_Main_0_Files
```
- Creates a new file: `Loca_en_Main_0.cpk.NEW`

## Important Guidelines

1. **Line Count**: Maintain the same number of lines between original and translated files
2. **Formatting**: Preserve all line breaks and special formatting
3. **File Encoding**: Use UTF-8 for all text files
4. **Chunk Management**: Default chunk size is 100 lines, but can be customized
5. **CPK Import**: Only modified files need to be in the folder for importing

## Troubleshooting

- Verify file paths when files are not found
- Check line counts if combining fails
- Use `--force` flag to override existing combined files
- Ensure chunk files follow the naming pattern: `chunk_*.txt`
