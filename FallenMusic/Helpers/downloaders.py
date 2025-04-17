# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import logging

from yt_dlp import YoutubeDL

LOGGER = logging.getLogger("FallenMusic")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "logger": LOGGER,
    "encoding": "utf-8",
    "extract_flat": True,
    "ignoreerrors": True,
    "retries": 5,
    "socket_timeout": 60,
    "buffer_size": 1024 * 1024,
    "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
}

def audio_dl(url: str) -> str:
    try:
        ydl = YoutubeDL(ydl_opts)
        info = ydl.extract_info(url, download=False)
        if not info:
            raise Exception("Could not extract video information")
            
        video_id = info['id']
        file_path = os.path.join("downloads", f"{video_id}.mp3")
        
        if os.path.exists(file_path):
            LOGGER.info(f"File already exists: {file_path}")
            return file_path
            
        LOGGER.info(f"Downloading audio from: {url}")
        ydl.download([url])
        
        if not os.path.exists(file_path):
            raise Exception("Download failed - file not found")
            
        return file_path
        
    except Exception as e:
        LOGGER.error(f"Download error: {str(e)}")
        raise