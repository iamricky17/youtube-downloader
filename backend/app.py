from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Folder to store downloads
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/fetch-info', methods=['POST'])
def fetch_info():
    youtube_url = request.json.get('url')
    if not youtube_url:
        return jsonify({'error': 'No URL provided'}), 400

    command = f"yt-dlp -F {youtube_url}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    if result.returncode != 0:
        return jsonify({'error': 'Failed to fetch video information'}), 500
    
    return jsonify({'formats': result.stdout})

@app.route('/download', methods=['POST'])
def download():
    youtube_url = request.json.get('url')
    quality = request.json.get('quality')
    if not youtube_url or not quality:
        return jsonify({'error': 'URL or quality missing'}), 400

    # Command to download video and subtitles
    command = (
        f"yt-dlp -f {quality} --write-subs --sub-lang en "
        f"--sub-format ttml --output {DOWNLOAD_FOLDER}/'%(title)s.%(ext)s' {youtube_url}"
    )
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        return jsonify({'error': 'Download failed'}), 500
    
    return jsonify({'message': 'Download completed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
