import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def fix_thumb(thumb, new_width=415, new_height=739):
    try:
        if thumb is not None:
            # Open the image and convert it to RGB
            img = Image.open(thumb).convert("RGB")
            # Resize the image to the new dimensions
            img = img.resize((new_width, new_height))
            # Save the resized image
            img.save(thumb, "JPEG")
    except Exception as e:
        print(e)
        thumb = None

    return new_width, new_height, thumb

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
        await fix_thumb(out_put_file_name)  # Call fix_thumb to resize
        return out_put_file_name
    return None
