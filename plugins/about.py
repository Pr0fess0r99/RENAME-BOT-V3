import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"š„ Total Users:- {total_user()}\nš¤ Bot Name: Rename Bot\nšØāš» Developer: @pr0fess0r99\nćļø Language: Python3\nš ļø Library: Pyrogram 2.0\nš” Server: Heroku\nš Total Renamed File :-{total_rename}\nš¾ Total Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
