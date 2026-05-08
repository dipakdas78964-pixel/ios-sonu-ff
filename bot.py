import json
import random
import string
import time
import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)

TOKEN = "7827262957:AAGp8QwlaGYM98fJJ3gFaOi5P76FUgxKdEg"

ADMIN_ID = 5585434832

REGISTER_LINK = "https://ios-sonu-ff.onrender.com"

DB_FILE = "database.json"

TEMP = {}

def load_db():

    if not os.path.exists(DB_FILE):

        return {
            "keys": {}
        }

    with open(DB_FILE, "r") as f:

        return json.load(f)

def save_db(data):

    with open(DB_FILE, "w") as f:

        json.dump(data, f, indent=4)

def random_key():

    chars = string.ascii_uppercase + string.digits

    return "IOS-SONU-FF-" + "".join(
        random.choice(chars) for _ in range(10)
    )

def main_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🔑 CREATE KEY",
                callback_data="create"
            )
        ],

        [
            InlineKeyboardButton(
                "📂 LIST KEYS",
                callback_data="list"
            )
        ],

        [
            InlineKeyboardButton(
                "🔍 CHECK KEY",
                callback_data="checkmenu"
            )
        ],

        [
            InlineKeyboardButton(
                "♻️ RESET KEY",
                callback_data="resetmenu"
            ),

            InlineKeyboardButton(
                "🗑 DELETE KEY",
                callback_data="deletemenu"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(
        keyboard
    )

    text = (

        "╔══════════════════╗\n"
        " 🔥 IOS SONU FF 🔥\n"
        "╚══════════════════╝\n\n"

        "👑 WELCOME TO IOS SONU FF RESELLER\n\n"

        "💎 PREMIUM RESELLER PANEL\n"
        "⚡ ULTRA FAST SYSTEM\n"
        "🔐 SECURE KEY DATABASE\n\n"

        "👤 OWNER:\n"
        "@SONUSELLOR11"
    )

    return text, reply_markup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text, reply_markup = main_menu()

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "back":

        text, reply_markup = main_menu()

        await query.edit_message_text(
            text,
            reply_markup=reply_markup
        )

    elif data == "create":

        keyboard = [

            [
                InlineKeyboardButton(
                    "⚡ 1 DAY VIP",
                    callback_data="1"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔥 7 DAYS PREMIUM",
                    callback_data="7"
                )
            ],

            [
                InlineKeyboardButton(
                    "💎 15 DAYS ULTRA",
                    callback_data="15"
                )
            ],

            [
                InlineKeyboardButton(
                    "👑 30 DAYS RESELLER",
                    callback_data="30"
                )
            ],

            [
                InlineKeyboardButton(
                    "⬅️ BACK",
                    callback_data="back"
                )
            ]

        ]

        reply_markup = InlineKeyboardMarkup(
            keyboard
        )

        await query.edit_message_text(
            "🔥 SELECT PREMIUM PLAN 🔥",
            reply_markup=reply_markup
        )

    elif data in ["1", "7", "15", "30"]:

        days = int(data)

        key = random_key()

        db = load_db()

        db["keys"][key] = {

            "days": days,

            "used": False,

            "created": int(time.time())
        }

        save_db(db)

        keyboard = [

            [
                InlineKeyboardButton(
                    "🌐 KEY REGISTER",
                    url=REGISTER_LINK
                )
            ],

            [
                InlineKeyboardButton(
                    "⬅️ BACK",
                    callback_data="back"
                )
            ]

        ]

        reply_markup = InlineKeyboardMarkup(
            keyboard
        )

        await query.edit_message_text(

            f"╔════════════════════╗\n"
            f"   🔥 IOS SONU FF 🔥\n"
            f"╚════════════════════╝\n\n"

            f"✅ PREMIUM KEY CREATED\n\n"

            f"🔑 KEY:\n"
            f"{key}\n\n"

            f"📅 PLAN:\n"
            f"{days} DAYS PREMIUM\n\n"

            f"🌐 REGISTER BELOW\n\n"

            f"⚡ STATUS: ACTIVE\n"
            f"👑 OWNER: @SONUSELLOR11",

            reply_markup=reply_markup
        )

app = Application.builder().token(
    TOKEN
).build()

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    CallbackQueryHandler(
        button
    )
)

print("🔥 IOS SONU FF PREMIUM PANEL RUNNING 🔥")

app.run_polling()
