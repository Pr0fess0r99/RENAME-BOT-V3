import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def fix_thumb(thumb):
    try:
        if thumb is not None:
            metadata = extractMetadata(createParser(thumb))
            if metadata and metadata.has("width") and metadata.has("height"):
                width = metadata.get("width")
                height = metadata.get("height")

                with Image.open(thumb) as img:
                    img.convert("RGB").save(thumb, "JPEG")

                    # Maintain aspect ratio
                    aspect_ratio = height / width
                    new_height = int(415 * aspect_ratio)

                    img = img.resize((415, new_height))
                    img.save(thumb, "JPEG")

                return 415, new_height, thumb
    except Exception as e:
        print(f"Error in fix_thumb: {e}")
    
    return None, None, None
    
async def take_screen_shot(video_file, output_directory, ttl):
    out_put_file_name = f"{output_directory}/{time.time()}.jpg"
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        out_put_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    if stderr:
        print(f"Error in take_screen_shot: {stderr.decode().strip()}")
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None
