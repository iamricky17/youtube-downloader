# **YouTube Downloader**  
Seamlessly download YouTube videos and subtitles in just a few clicks. This lightweight, user-friendly tool is designed to fetch video formats, subtitle files, and offer effortless downloads directly from YouTube.  

[View on GitHub](https://github.com/iamricky17/youtube-downloader)  
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Stars](https://img.shields.io/github/stars/iamricky17/youtube-downloader)](https://github.com/iamricky17/youtube-downloader/stargazers)  
[![Issues](https://img.shields.io/github/issues/iamricky17/youtube-downloader)](https://github.com/iamricky17/youtube-downloader/issues)  

[![Downloads](https://pepy.tech/badge/flexible-requirements)](https://pepy.tech/project/flexible-requirements)  
[![Downloads](https://pepy.tech/badge/flexible-requirements/month)](https://pepy.tech/project/flexible-requirements)  
[![Downloads](https://pepy.tech/badge/flexible-requirements/week)](https://pepy.tech/project/flexible-requirements)  

---

## **Real-Life Use Cases**  
Perfect for:  
- **Students & Researchers**: Quickly grab lecture videos and accompanying subtitles.  
- **Content Creators**: Access videos and subtitles for inspiration or editing.  
- **Travelers**: Download videos to watch offline when internet connectivity is limited.  

---

## **Features**  
- 🎥 **Video Downloads**: Choose from multiple video quality options (1080p, 720p, etc.).  
- 📝 **Subtitle Support**: Automatically fetch and download subtitles in TTML format.  
- 🚀 **Simple Interface**: Easy-to-use frontend for hassle-free interaction.  
- 🔄 **Cross-Platform**: Works on Windows, macOS, and Linux.  

---

## **Installation**  

### **1. Clone the Repository**  
git clone https://github.com/iamricky17/youtube-downloader.git  
cd youtube-downloader  
### **2. Backend Setup**
Navigate to the backend directory:


cd backend  
Install the required Python dependencies:


pip install -r requirements.txt  
Start the backend server:


python app.py  
### **3. Frontend Setup**
Open the frontend/index.html file in your browser for access.
Usage
Paste a valid YouTube URL in the input field.
Fetch available video and subtitle options.
Select your preferences and hit Download.
Enjoy your downloaded video and subtitles offline!
How It Works
Input Processing: Extracts video details from the provided YouTube URL.
Video Quality Fetching: Fetches available formats via yt-dlp.
Subtitle Integration: Checks and retrieves subtitle files for the video.
Download Options: Provides a tailored list of video and subtitle download choices.
Future Enhancements
🎵 Audio Downloads: Add support for audio-only formats like MP3.
🌍 Subtitle Languages: Support multiple languages for subtitles.
⚡ Batch Processing: Allow users to download multiple videos at once.
📱 Mobile Compatibility: Optimize UI for smartphones and tablets.
Contributing
Contributions, feedback, and feature requests are welcome! Fork the repository, create a branch, and submit a pull request.

License
This project is licensed under the MIT License.
