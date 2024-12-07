# **YouTube Downloader**  

A lightweight, user-friendly tool to seamlessly download YouTube videos and subtitles. Fetch multiple video formats and subtitles with ease, directly from YouTube.  

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) ![Stars](https://img.shields.io/github/stars/iamricky17/youtube-downloader)  ![Forks](https://img.shields.io/github/forks/iamricky17/youtube-downloader) ![Issues](https://img.shields.io/github/issues/iamricky17/youtube-downloader) ![Last Commit](https://img.shields.io/github/last-commit/iamricky17/youtube-downloader)

---

## **Real-Life Use Cases**  
- **Students & Researchers**: Download lecture videos and subtitles for offline study.  
- **Content Creators**: Access videos and subtitles to enhance creative projects.  
- **Travelers**: Download videos to watch without needing an internet connection.  

---

## **Key Features**  
- **Video Downloads**: Choose from various video qualities, including 1080p and 720p.  
- **Subtitle Support**: Fetch and download subtitles in TTML format effortlessly.  
- **User-Friendly Interface**: Simplified frontend for hassle-free navigation.  
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux systems.  

---

## **Installation**

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/iamricky17/youtube-downloader.git  
cd youtube-downloader  
```

### **Step 2: Backend Setup**  
Navigate to the backend directory:  
```bash
cd backend  
```

Install the required Python dependencies:  
```bash
pip install -r requirements.txt  
```

Start the backend server:  
```bash
python app.py  
```

### **Step 3: Frontend Setup**  
Open the `frontend/index.html` file in your browser to access the application.

---

## **Usage**  
1. Paste the YouTube video URL in the input field.  
2. Fetch available video quality and subtitle options.  
3. Select your desired options and click "Download."  
4. Enjoy offline viewing with downloaded videos and subtitles!

---

## **How It Works**  

1. **Input Processing**: Parses the YouTube URL to extract video information.  
2. **Video Format Detection**: Retrieves available video qualities using `yt-dlp`.  
3. **Subtitle Integration**: Detects and downloads subtitle files for the video.  
4. **Download Options**: Provides a tailored list of video and subtitle choices for download.  

---

## **Planned Enhancements**  
- **Audio-Only Downloads**: Support for MP3 and other audio formats.  
- **Multilingual Subtitles**: Download subtitles in various languages.  
- **Batch Processing**: Enable multiple video downloads simultaneously.  
- **Mobile Optimization**: Improve compatibility with mobile devices.  

---

## **Contributing**  
We welcome contributions, feedback, and feature suggestions! To contribute:  
1. Fork this repository.  
2. Create a feature branch.  
3. Submit a pull request with your proposed changes.

[View on GitHub](https://github.com/iamricky17/youtube-downloader)  

---
