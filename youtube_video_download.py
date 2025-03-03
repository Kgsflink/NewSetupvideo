import os
import yt_dlp
from pathlib import Path

def download_youtube_video(url: str, download_folder: str):
    """
    Download a single YouTube video and save it in the specified download folder.
    """
    # Ensure the download folder exists
    Path(download_folder).mkdir(parents=True, exist_ok=True)
    
    # Define the ydl_opts for yt-dlp
    ydl_opts = {
        'format': 'bestvideo[height>=1080]+bestaudio/best',  # Highest quality video above 1080p and best audio
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save to the specified folder with video title as filename
        'noplaylist': True,  # Do not download playlists
        'quiet': False,  # Set to True if you want less output
        'merge_output_format': 'mp4',  # Ensure video and audio are merged into a single mp4 file
    }

    # Download the video using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Download the video and save it to the specified folder
            print(f"Downloading video from {url}...")
            ydl.download([url])
            print(f"Download complete! Saved to {download_folder}")
        except Exception as e:
            print(f"An error occurred: {e}")

def download_videos_from_file(file_path: str, download_folder: str):
    """
    Download multiple YouTube videos from a file containing links.
    """
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            # Strip newlines and empty spaces from URLs
            urls = [url.strip() for url in urls if url.strip()]
            if not urls:
                print("No URLs found in the file.")
                return
            # Download each video in the list
            for url in urls:
                download_youtube_video(url, download_folder)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while downloading from the file: {e}")

def main():
    """
    Main function to prompt the user for input and handle downloading.
    """
    # Ask the user whether to download a single video or from a list in the file
    choice = input("Do you want to download a single video (S) or videos from a list in 'links.txt' (L)? (S/L): ").strip().lower()

    # Set the default download folder to the specified path
    download_folder = '/home/shubhambind8423/Video_editing/video'  # Update this path as necessary

    if choice == 's':
        # Ask for the single YouTube Shorts URL
        url = input("Enter the URL of the YouTube Shorts video to download: ").strip()
        if url:
            download_youtube_video(url, download_folder)
        else:
            print("Invalid URL entered. Please provide a valid YouTube Shorts URL.")
    elif choice == 'l':
        # Ask for the file path containing multiple URLs
        file_path = input("Enter the path to the links.txt file: ").strip()
        download_videos_from_file(file_path, download_folder)
    else:
        print("Invalid choice. Please enter 'S' for a single video or 'L' for multiple videos from a file.")

if __name__ == "__main__":
    main()
