import os
import requests
from urllib.parse import urlparse

def fetch_image(url, folder_name, downloaded_files):
    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises error for bad HTTP status codes

        # Check important HTTP headers before saving
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type:
            print(f"✗ Skipping: The URL does not contain an image ({url})")
            return

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Prevent duplicates
        if filename in downloaded_files:
            print(f"✗ Skipping duplicate: {filename}")
            return

        # Create folder if not exists
        os.makedirs(folder_name, exist_ok=True)

        # Save image in binary mode
        filepath = os.path.join(folder_name, filename)
        with open(filepath, "wb") as f:
            f.write(response.content)

        downloaded_files.add(filename)  # Record the downloaded file
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask for multiple URLs separated by commas
    urls = input("Enter one or more image URLs (separated by commas): ").split(",")

    folder_name = "Fetched_Images"
    downloaded_files = set()  # Track downloaded files to prevent duplicates

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url, folder_name, downloaded_files)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
