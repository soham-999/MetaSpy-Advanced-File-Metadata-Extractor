import os
import sys
import json
import magic
from PIL import Image
from PIL.ExifTags import TAGS
from mutagen import File as MutagenFile
from pymediainfo import MediaInfo
from PyPDF2 import PdfReader
from docx import Document
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

def detect_file_type(filepath):
    try:
        mime = magic.from_file(filepath, mime=True)
        return mime
    except:
        return "unknown"

def get_image_metadata(filepath):
    try:
        img = Image.open(filepath)
        exif_data = img._getexif()
        if not exif_data:
            return {"info": "No EXIF metadata found."}
        return {TAGS.get(tag): val for tag, val in exif_data.items() if tag in TAGS}
    except Exception as e:
        return {"error": f"Image error: {e}"}

def get_audio_metadata(filepath):
    try:
        audio = MutagenFile(filepath)
        return dict(audio.tags or {})
    except Exception as e:
        return {"error": f"Audio error: {e}"}

def get_video_metadata(filepath):
    try:
        media_info = MediaInfo.parse(filepath)
        return {
            f"{track.track_type}_{i}": track.to_data()
            for i, track in enumerate(media_info.tracks)
        }
    except Exception as e:
        return {"error": f"Video error: {e}"}

def get_pdf_metadata(filepath):
    try:
        reader = PdfReader(filepath)
        return dict(reader.metadata or {})
    except Exception as e:
        return {"error": f"PDF error: {e}"}

def get_docx_metadata(filepath):
    try:
        doc = Document(filepath)
        core_props = doc.core_properties
        return {k: str(getattr(core_props, k)) for k in dir(core_props) if not k.startswith("_") and not callable(getattr(core_props, k))}
    except Exception as e:
        return {"error": f"DOCX error: {e}"}

def get_generic_metadata(filepath):
    try:
        parser = createParser(filepath)
        if not parser:
            return {"error": "Could not parse file for generic metadata."}
        metadata = extractMetadata(parser)
        if metadata is None:
            return {"info": "No metadata found."}
        return {item.name: item.value for item in metadata}
    except Exception as e:
        return {"error": f"Generic error: {e}"}

def extract_metadata(filepath):
    if not os.path.isfile(filepath):
        return {"error": "File not found."}
    
    mime = detect_file_type(filepath)
    print(f"[INFO] MIME type detected: {mime}")

    if mime.startswith("image"):
        return get_image_metadata(filepath)
    elif mime.startswith("audio"):
        return get_audio_metadata(filepath)
    elif mime.startswith("video"):
        return get_video_metadata(filepath)
    elif mime == "application/pdf":
        return get_pdf_metadata(filepath)
    elif mime in ("application/vnd.openxmlformats-officedocument.wordprocessingml.document",):
        return get_docx_metadata(filepath)
    else:
        return get_generic_metadata(filepath)

def print_metadata(metadata):
    print("\n--- METADATA ---")
    for key, value in metadata.items():
        print(f"{key}: {value}")

def export_json(metadata, output_path):
    with open(output_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    print(f"\n[INFO] Metadata exported to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python metaspy.py <file_path> [--json]")
        sys.exit(1)

    file_path = sys.argv[1]
    export = '--json' in sys.argv

    metadata = extract_metadata(file_path)
    print_metadata(metadata)

    if export:
        export_json(metadata, "metaspy_output.json")
