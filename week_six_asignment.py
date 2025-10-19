import os
import requests

# Prompt user for an image URL
url = input("Enter the image URL: ")

# Directory to store downloaded images
folder_name = "Fetched_Images"

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

try:
    print("Downloading image...")

    # Fetch the image from the web
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)

    # Extract filename from the URL or use a default one
    filename = url.split("/")[-1] or "downloaded_image.jpg"

    # Full path where the image will be saved
    file_path = os.path.join(folder_name, filename)

    # Save image in binary mode
    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"Image successfully saved as '{file_path}'")

except requests.exceptions.MissingSchema:
    print("Invalid URL format. Please include http:// or https://")

except requests.exceptions.ConnectionError:
    print("Network error! Please check your internet connection.")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")