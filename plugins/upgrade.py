"""pr0fess0r99"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily Upload Limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily Upload  Limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload Limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month

	UPI 🆔 Details

        Google pay 📲 joynathnet4@oksbi
        Phonepe 📲 bijoy.nath@ybl
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👮 Admin", url = "https://t.me/pr0fess0r99")], 
        			[InlineKeyboardButton("Cancel ✖️", callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily Upload Limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily Upload  Limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload Limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month

	UPI 🆔 Details

        Google pay 📲 joynathnet4@oksbi
        Phonepe 📲 bijoy.nath@ybl
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👮 Admin", url = "https://t.me/pr0fess0r99")], 
        			[InlineKeyboardButton("Cancel ✖️", callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	
