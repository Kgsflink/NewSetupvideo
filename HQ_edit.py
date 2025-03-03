import ffmpeg
import os
import json

def edit_video(input_path, output_path):
    """Add padding, metadata, and a banner to a video, then save it to the output path with high quality and 60fps."""
    # Check if the input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input video file does not exist: {input_path}")

    try:
        # Construct video filters
        video_filter = (
            "pad=iw+50:ih+50:25:25:black,"  # Padding
            "drawtext=fontfile=Debrosee-ALPnL.ttf:"  # Font file path (Linux)
            "text='KGSFLINK':fontsize=12:fontcolor=white:"  # Banner text
            "x=(main_w-text_w)/2:y=main_h-50:box=1:"  # Text position
            "boxcolor=black@0.5:boxborderw=5"  # Box settings
        )

        # Run ffmpeg command using ffmpeg-python for high-quality video output at 60 fps
        ffmpeg.input(input_path).output(
            output_path,
            vf=video_filter,
            vcodec='libx264',  # High-quality video codec
            video_bitrate='8000k',  # Increased bitrate for higher quality
            acodec='aac',
            audio_bitrate='320k',  # Higher audio bitrate for quality
            movflags='+faststart',
            pix_fmt='yuv420p',
            preset='slow',
            r=60,  # Set the video frame rate to 60 fps
            metadata='title=Video created by kgsflink'  # Metadata title
        ).run()  # Calling run directly

        print(f"Video editing completed successfully! Edited video saved at: {output_path}")
    except ffmpeg.Error as e:
        print(f"Error during video processing: {e.stderr.decode()}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def load_processed_videos(config_file):
    """Load the list of processed videos from the config file."""
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            return json.load(file)
    else:
        return []

def save_processed_videos(config_file, processed_videos):
    """Save the list of processed videos to the config file."""
    with open(config_file, 'w') as file:
        json.dump(processed_videos, file)

if __name__ == "__main__":
    # Define directories (adjusting to Linux file system)
    input_directory = '/home/shubhambind8423/Video_editing/video'
    output_directory = '/home/shubhambind8423/Video_editing/edited_video'
    config_file = 'processed_videos.json'  # Config file to store processed video names

    # Load the list of processed videos from the config file
    processed_videos = load_processed_videos(config_file)

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Process each video in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):  # Check for video files
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)

            # Skip processing if the video has already been processed
            if filename in processed_videos:
                print(f"Skipping already processed video: {filename}")
                continue

            try:
                # Edit the video
                edit_video(input_path, output_path)
                
                # Add the video to the list of processed videos
                processed_videos.append(filename)
                save_processed_videos(config_file, processed_videos)  # Save the updated list
            except Exception as e:
                print(f"Failed to edit video {filename}: {e}")
