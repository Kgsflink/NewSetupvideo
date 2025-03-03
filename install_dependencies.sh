#!/bin/bash

# Update the system's package list
echo "Updating package list..."
sudo apt-get update

# Install ffmpeg if it's not already installed
echo "Installing ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "ffmpeg not found, installing..."
    sudo apt-get install -y ffmpeg
else
    echo "ffmpeg is already installed."
fi

# Install ffmpeg-python using pip if it's not installed in the current virtual environment
echo "Installing ffmpeg-python..."
if ! pip show ffmpeg-python &> /dev/null; then
    pip install ffmpeg-python
else
    echo "ffmpeg-python is already installed."
fi

# Check if the font file exists, if not, provide a message to download it
FONT_FILE="Debrosee-ALPnL.ttf"
if [ ! -f "$FONT_FILE" ]; then
    echo "Font file $FONT_FILE not found in the current directory. Please download it and place it here."
else
    echo "Font file $FONT_FILE is already present."
fi

# Provide a message that the script has finished
echo "Dependencies installation complete!"
