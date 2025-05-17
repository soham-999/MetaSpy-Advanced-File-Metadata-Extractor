# 🕵️ MetaSpy – Advanced Metadata Extractor Tool

MetaSpy is a powerful, multi-format metadata extractor built in Python. It supports various file types including images, audio, video, PDFs, DOCX, and binary files, making it ideal for digital forensics, file auditing, and ethical hacking investigations.

Developed by Soham

---

## 🔍 Features

- ✅ MIME type auto-detection using `python-magic`  
- 🖼️ EXIF extraction from images (JPEG, PNG)  
- 🎵 ID3 tag reading for MP3/FLAC/etc.  
- 🎥 Video metadata from MP4, MKV, AVI using `pymediainfo`  
- 📄 PDF and DOCX metadata  
- 🛠️ Binary file parsing via Hachoir  
- 📤 Optional JSON export  
- 💻 Clean CLI interface  

---

## 📦 Installation & Usage Guide

### 🧰 Requirements

- Python 3.8+

### 🛠️ Required Python Libraries

Install all dependencies via pip:

```bash
pip install python-magic Pillow mutagen pymediainfo PyPDF2 python-docx hachoir
```

---

## 📦 Installation & Usage Guide

## 🧱 System Dependencies

## Linux (Debian/Ubuntu)
- Install the following packages to support MIME detection and media metadata extraction:

```bash
sudo apt update
sudo apt install -y libmagic1 mediainfo
```
## Windows
- 1. MediaInfo CLI:
- Download from MediaInfo official site and add it to your system PATH environment variable.

- 2. libmagic binaries:
- Download Windows binaries for libmagic from here and ensure they are accessible.

- 3. Alternatively, use the Python package bundling libmagic for Windows:

---

## 🚀 Running MetaSpy

- Run from the command line:

```bash
python metaspy.py <file_path> [--json]
```
- Examples:
```bash
python metaspy.py sample.jpg
python metaspy.py document.pdf
python metaspy.py video.mp4 --json
```