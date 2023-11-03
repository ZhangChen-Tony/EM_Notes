import os
import re

# Step 1: Get all .md files in the current directory
md_files = [f for f in os.listdir() if f.endswith('.md')]

# Step 2: Filter files that start with a number
num_files = [f for f in md_files if re.match(r'^\d', f)]

# Step 3: Sort the files
num_files.sort(key=lambda f: int(re.match(r'^\d+', f).group()))

# Step 4: Open each file and read the content
all_content = ""
for file in num_files:
    with open(file, 'r', encoding='utf-8') as f:  # Specify the encoding here
        all_content += f.read() + "\n\n"

# Step 5: Write the content to a new file "SUM.md"
with open("SUM.md", 'w', encoding='utf-8') as f:  # Specify the encoding here
    f.write(all_content)