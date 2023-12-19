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
	await message.reply_text(f"👥 Total Users:- {total_user()}\n🤖 Bot Name: Rename Bot\n👨‍💻 Developer: @viizet\n㊗️ Language: Python3\n🛠️ Library: Pyrogram 2.0\n📡 Server: Heroku\n📝 Total Renamed File :-{total_rename}\n💾 Total Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
