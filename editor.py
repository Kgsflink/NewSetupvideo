import ffmpeg
import os

def edit_video(input_path, output_path):
    """Add padding, metadata, and a banner to a video, then save it to the output path."""
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

        # Run ffmpeg command using ffmpeg-python
        ffmpeg.input(input_path).output(
            output_path,
            vf=video_filter,
            vcodec='libx264',
            video_bitrate='5000k',
            acodec='aac',
            audio_bitrate='192k',
            movflags='+faststart',
            pix_fmt='yuv420p',
            preset='slow',
            metadata='title=Video created by kgsflink'  # Removed metadata_comment
        ).run()  # Calling run directly

        print(f"Video editing completed successfully! Edited video saved at: {output_path}")
    except ffmpeg.Error as e:
        print(f"Error during video processing: {e.stderr.decode()}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Define directories (adjusting to Linux file system)
    input_directory = '/home/shubhambind8423/Video_editing/video'
    output_directory = '/home/shubhambind8423/Video_editing/edited_video'

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Process each video in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):  # Check for video files
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)

            try:
                # Edit the video
                edit_video(input_path, output_path)
            except Exception as e:
                print(f"Failed to edit video {filename}: {e}")
