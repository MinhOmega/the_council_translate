# The Council CPK Tool
**Coded by Delutto - Tribo Gamer Brasil 2018**  
www.tribogamer.com

## 1. Usage

### 1.1 Parameters
`[option] <File.cpk> <Output Folder>`

Options:
- `-e` = Export Files
- `-i` = Import Files  
- `-h` = This Help

Or just run the tool from executable, a dialog option will be showed.

### 1.2 Export: -e
`The_Council_CPK_Tool.exe -e Loca_en_Main_0.cpk Loca_en_Main_0_Files`

### 1.3 Import: -i (Point to original file)
`The_Council_CPK_Tool.exe -i Loca_en_Main_0.cpk Loca_en_Main_0_Files`  
Will be created a "Loca_en_Main_0.cpk.NEW" file.

## 2. Notes

### 2.1
On importing files, you can leave only the modificated files on folder.
The tool check if file exist, and in case they not find, the tool copy
data from original file.

### 2.2
Both options use the same parameters order, because the tool need
some unknown infos from original CPK file to create a new one.