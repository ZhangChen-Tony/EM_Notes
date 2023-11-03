import os
import re
import requests
from urllib.parse import urlparse
from pathlib import Path

# Step 1: Traverse all .md files in the current directory
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r+', encoding='utf-8') as f:  # Specify the encoding here
                content = f.read()

                # Step 2: Find all image links
                img_tuples = re.findall(r'!\[.*?\]\((.*?)\)|<img src="(.*?)"', content)
                img_urls = [url for tup in img_tuples for url in tup if url]  # Flatten the list and remove empty matches
                print(f"Found {len(img_urls)} images in {file}")

                for url in img_urls:
                    # Check if the url is a full url
                    if url.startswith('http://') or url.startswith('https://'):
                        # Parse the url to get the image name
                        a = urlparse(url)
                        img_name = os.path.basename(a.path)

                        # Create the directory if it doesn't exist
                        img_dir = f"./images/{os.path.splitext(file)[0]}"
                        Path(img_dir).mkdir(parents=True, exist_ok=True)

                        # Step 3: Download and save the image
                        response = requests.get(url)
                        with open(f"{img_dir}/{img_name}", 'wb') as img_f:
                            img_f.write(response.content)
                        print(f"Downloaded image {img_name} from {url}")

                        # Step 4: Replace the image link with the local path
                        content = content.replace(url, f"{img_dir}/{img_name}")
                        print(f"Replaced {url} with {img_dir}/{img_name} in {file}")

                # Write the updated content back to the file
                f.seek(0)
                f.write(content)
                f.truncate()