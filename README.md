# 🕵️ MetaSpy – Advanced Metadata Extractor Tool

MetaSpy is a powerful, multi-format metadata extractor built in Python. It supports various file types including images, audio, video, PDFs, DOCX, and binary files, making it ideal for digital forensics, file auditing, and ethical hacking investigations.

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

## 📦 Installation

```bash
pip install python-magic Pillow mutagen pymediainfo PyPDF2 python-docx hachoir
