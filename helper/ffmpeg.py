import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def chunk_size(length: int):
    return 2 ** max(min(math.ceil(math.log2(length / 1024)), 10), 2) * 1024


async def offset_fix(offset, chunksize):
    offset -= offset % chunksize
    return offset


async def fix_thumbnail(thumb_path: str):
    metadata = extractMetadata(createParser(thumb_path))
    if metadata.has("height"):
        height = metadata.get("height")
    else:
        height = 0
    Image.open(thumb_path).convert("RGB").save(thumb_path)
    img = Image.open(thumb_path)
    img.resize((320, height))
    img.save(thumb_path, "JPEG")
    return thumb_path
