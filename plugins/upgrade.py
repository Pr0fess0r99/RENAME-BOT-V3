"""pr0fess0r99"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters


@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily Upload Limit 2GB
	Price 0
	
	**🪙 VIP 1 🪙 **
        Daily Upload  Limit 10GB
        Price Evc 0.5   So /🌎 0.8$  per Month
	
	**💎 VIP 2 💎**
        Daily Upload Limit 50GB
        Price Evc 1.0  So /🌎 1.2$  per Mont


	Pay Using Upi I'd ```7808912076@paytm```
       	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👮 Admin", url = "https://t.me/Viizet")], 
        			[InlineKeyboardButton("Cancel ✖️", callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily Upload Limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily Upload  Limit 10GB
	Price  🇸🇴 0.67$  per Month
	
	**VIP 2 **
	Daily Upload Limit 50GB
	Price  🇸🇴 0.97$  per Month

	UPI 🆔 Details

        Contect 📲 tg @VIIZET
        Phone.  📲 WAAFI
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👮 Admin", url = "https://t.me/viizet")], 
        			[InlineKeyboardButton("Cancel ✖️", callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
	
