import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def fix_thumb(thumb):
    target_height = 739
    target_width = 415

    try:
        if thumb is not None:
            # Open the image and convert it to RGB
            img = Image.open(thumb).convert("RGB")
            width, height = img.size

            # Calculate new width to maintain aspect ratio
            aspect_ratio = width / height
            new_width = int(target_height * aspect_ratio)

            # Resize and save the image
            img = img.resize((new_width, target_height))
            img.save(thumb, "JPEG")

            # Update width and height variables
            width, height = new_width, target_height
    except Exception as e:
        print(e)
        thumb = None
        width, height = 0, 0

    return width, height, thumb
    
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
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None
