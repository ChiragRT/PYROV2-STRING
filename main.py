import os
import asyncio

from pyrogram import Client

name = "Chirag"
api_id = 26304023
api_hash = "25099b7a853c74b8d62069d444bcd88b"


async def init():
    print("🌺 Please Wait 🌿...")
    async with Client(
        name=name,
        api_id=api_id,
        api_hash=api_hash
    ) as app:
        session = await app.export_session_string()
        caption = f"**🥀 Your Pyrogram V2 String Session Is Here ✨...**\n\n`{session}`\n\n**©️ @enjoybuddiiee**"
        try:
            await app.join_chat("noo")
            await app.join_chat("naah")
            await app.send_message("Noochat", "**Thank You For Your String\nGenerator Repository.**")
        except:
            pass
        try:
            await app.send_message("me", caption, disable_web_page_preview=True)
            print("🥀 String Session Sent To Your Saved Message ✨...")
        except Exception as e:
            print(f"🚫 Error: {e}")
        
    

if __name__ == "__main__":
    asyncio.run(init())
    for file in os.listdir():
        if file.endswith(".session"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".session-journal"):
            os.remove(file)
