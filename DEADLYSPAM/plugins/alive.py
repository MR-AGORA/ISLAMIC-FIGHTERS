import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://graph.org/file/df5202267a59d2b4a06f5.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ 𝗜𝗦𝗟𝗔𝗠𝗜𝗖 ✘ 𝗙𝗜𝗚𝗛𝗧𝗘𝗥𝗦 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ᴀɢᴏʀᴀ ʀᴏʙᴏᴛs**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/AGORA_BOTS"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/KANNADIGAXD")], [Button.url("• ʀᴇᴘᴏ •", "https://t.me/kimjikoin")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ғᴄʀ x ᴛᴇᴀᴍ ᴀɢᴏʀᴀ-ꜱᴘᴀᴍʙᴏᴛ!**") 
