import logging
from telegram import Update, BotCommand, MenuButtonCommands
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from connect import Gchat

from dotenv import load_dotenv
import os

users_active = {}

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def set_bot_commands(application):
    commands = [
        BotCommand("start", "Begin chatting"),
        BotCommand("help", "Show available commands"),
        BotCommand("clear", "Clear conversation history"),
        BotCommand("exit", "End conversation")
    ]
    await application.bot.set_my_commands(commands)

async def set_bot_menu(application):
    menu_button = MenuButtonCommands()
    await application.bot.set_chat_menu_button(menu_button=menu_button)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
    user = update.effective_user
    users_active[user.id]=Gchat()
    await update.message.reply_text(f"Hey {user.first_name}! You can start conversation.")

async def helper(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
"""
Available Commands:
/start - Start the conversation
/clear - Clear chat memory
/exit - End conversation
/help - Show available commands
""")


async def handle_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if user.id not in users_active:
        await update.message.reply_text("First start the chat with '/start' command")
        return
    
    reply = users_active[user.id].reply(update.message.text)
    await update.message.reply_text(reply)

async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
    user = update.effective_user
    if user.id in users_active:
        users_active.pop(user.id)
    else:
        await update.message.reply_text("First start the chat. Click '/start' command")
        return
    
    await update.message.reply_text(f"Exited! \nClick/start to start chat.")

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
    user = update.effective_user
    if user.id in users_active:
        users_active[user.id].clear_conversation()
    else:
        await update.message.reply_text("First start the chat. Click '/start' command")
        return
    
    await update.message.reply_text(f"Conversation memory cleared!")

async def post_init(application):
    await set_bot_commands(application)
    await set_bot_menu(application)

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).post_init(post_init).build()

    application.add_handler(CommandHandler("start",start))
    application.add_handler(CommandHandler("clear",clear))
    application.add_handler(CommandHandler("exit",exit))
    application.add_handler(CommandHandler("help",helper))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_chat))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()



