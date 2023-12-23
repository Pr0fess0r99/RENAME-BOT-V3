import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.progress import humanbytes

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"")
import datetime
from datetime import date as date_
STRING = os.environ.get("STRING","")
log_channel = int(os.environ.get("LOG_CHANNEL",""))
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_text(text =f"""Hello 👋 {message.from_user.first_name},\n\nI'm File Rename Bot, Please Sent Me Any Telegram Document Or Video And Enter New Filename To Rename It.""",
	reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[
	   InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/viizet") 
           ],[
           InlineKeyboardButton("🔗 Support", url="https://t.me/File_Renamernotchat"),
           InlineKeyboardButton("📢 Updates", url="https://t.me/File_Renamernot")]]))
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,"Your Friend Already Using Our Bot")
	            await message.reply_text(text =f"""Hello 👋 {message.from_user.first_name},\n\nI'm File Rename Bot, Please Sent Me Any Telegram Document Or Video And Enter New Filename To Rename It.""",    
        reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[
	   InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/viizet") 
           ],[
           InlineKeyboardButton("🔗 Support", url="https://t.me/File_Renamernotchat"),
           InlineKeyboardButton("📢 Updates", url="https://t.me/File_Renamernot")]]))
	        except:
	             return
	    else:
	         await client.send_message(id,"Congrats! You Won 100MB Upload limit")
	         _user_= find_one(int(id))
	         limit = _user_["uploadlimit"]
	         new_limit = limit + 104857600
	         uploadlimit(int(id),new_limit)
	         await message.reply_text(text =f"""Hello 👋 {message.from_user.first_name},\n\nI'm File Rename Bot, Please Sent Me Any Telegram Document Or Video And Enter New Filename To Rename It.""",
	reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[
	   InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/viizet") 
           ],[
           InlineKeyboardButton("🔗 Support", url="https://t.me/File_Renamernotchat"),
           InlineKeyboardButton("📢 Updates", url="https://t.me/File_Renamernot")]]))
	         



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**You Are Not Subscribed My Updates Channel**",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("🔔 SUBSCRIBE 🔔" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       try:
           bot_data = find_one(int(botid))
           prrename = bot_data['total_rename']
           prsize = bot_data['total_size']
           user_deta = find_one(user_id)
       except:
           await message.reply_text("Use About Command First /about")
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       	user_type = user_deta["usertype"]
       except:
           await message.reply_text("DataBase Has Been Cleared Click On /start And Send Me Document/Video Again")
           return
           
           
       c_time = time.time()
       
       if user_type=="Free":
           LIMIT = 600
       else:
           LIMIT = 50
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```Sorry Dude I Am Not Only For YOU \n Flood Control Is Active  So Please Wait For {ltime}```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
           	 
	       
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"Sorry! I Can't Upload Files That Are Larger Than {humanbytes(limit)}. File Size Detected {humanbytes(file.file_size)}\nUsed Daly Limit {humanbytes(used)} If U Want To Rename Large File Upgrade Your Plan",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("💰Upgrade 💰",callback_data = "upgrade") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f"You Can't Upload More Then {humanbytes(limit)} Used Daly Limit {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""What Do You Want Me To Do With This File ?\n**File Name**: {filename}\n**File Size**: {humanize.naturalsize(file.file_size)}\n**Dc ID**: {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            uploadlimit(message.from_user.id,6442450944)
       		            usertype(message.from_user.id,"Free")
	
       		            await message.reply_text(f'Your Plane Expired On 📅 {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("You Can't Upload File Bigger Than 2GB")
       		          	return
       		else:
       		    if buy_date:
       		        pre_check = check_expi(buy_date)
       		        if pre_check == False:
       		            uploadlimit(message.from_user.id,6442450944)
       		            usertype(message.from_user.id,"Free")
       		        
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""**🗂️ What Do You Want Me To Do With This File ?**\n\n**◈ File Name :-** {filename}\n**◈ File Size :-** {filesize}\n**◈ Dc ID :-** {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("❎ Cancel ",callback_data = "cancel"),
       		InlineKeyboardButton("Rename 📝",callback_data = "rename")  ]]))
       		
