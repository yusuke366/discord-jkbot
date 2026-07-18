import os

import discord
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client_ai = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

PERSONA_SAVE_FILE = "channel_personas.json"
MODEL_SAVE_FILE = "channel_models.json"

chance_for_all = 0.2
AVATAR_BASE_URL = (
    "https://storage.googleapis.com/denkitv/jkbot"
)
PERSONA_FILES = {
    "全員": [
        {
            "name": "みさき",
            "file": "misaki.txt",
            "avatar": f"{AVATAR_BASE_URL}/misaki.png",
            "chance": chance_for_all
        },
        {
            "name": "あや",
            "file": "aya.txt",
            "avatar": f"{AVATAR_BASE_URL}/aya.png",
            "chance": chance_for_all
        },
        {
            "name": "りん",
            "file": "rin.txt",
            "avatar": f"{AVATAR_BASE_URL}/rin.png",
            "chance": chance_for_all
        },
        {
            "name": "ゆい",
            "file": "yui.txt",
            "avatar": f"{AVATAR_BASE_URL}/yui.png",
            "chance": chance_for_all
        },
        {
            "name": "なぎさ",
            "file": "nagisa.txt",
            "avatar": f"{AVATAR_BASE_URL}/nagisa.png",
            "chance": chance_for_all
        },
        {
            "name": "ことね",
            "file": "kotone.txt",
            "avatar": f"{AVATAR_BASE_URL}/kotone.png",
            "chance": chance_for_all
        },
        {
            "name": "はる",
            "file": "haru.txt",
            "avatar": f"{AVATAR_BASE_URL}/haru.png",
            "chance": chance_for_all
        },
        {
            "name": "かなで",
            "file": "kanade.txt",
            "avatar": f"{AVATAR_BASE_URL}/kanade.png",
            "chance": chance_for_all
        },
        {
            "name": "めぐ",
            "file": "megu.txt",
            "avatar": f"{AVATAR_BASE_URL}/megu.png",
            "chance": chance_for_all
        },
        {
            "name": "みお",
            "file": "mio.txt",
            "avatar": f"{AVATAR_BASE_URL}/mio.png",
            "chance": chance_for_all
        }
    ],
    "アシスタント": [
        {
            "name": "あや",
            "file": "assistant.txt",
            "avatar": f"{AVATAR_BASE_URL}/aya.png",
            "chance": 1.0
        }
    ],
    "ソフトウェアエンジニア": [
        {
            "name": "りん",
            "file": "engineer.txt",
            "avatar": f"{AVATAR_BASE_URL}/rin.png",
            "chance": 1.0
        }
    ],
    "みさき": [
        {
            "name": "みさき",
            "file": "misaki.txt",
            "avatar": f"{AVATAR_BASE_URL}/misaki.png",
            "chance": 1.0
        }
    ],
    "あや": [
        {
            "name": "あや",
            "file": "aya.txt",
            "avatar": f"{AVATAR_BASE_URL}/aya.png",
            "chance": 1.0
        }
    ],
    "りん": [
        {
            "name": "りん",
            "file": "rin.txt",
            "avatar": f"{AVATAR_BASE_URL}/rin.png",
            "chance": 1.0
        }
    ],
    "ゆい": [
        {
            "name": "ゆい",
            "file": "yui.txt",
            "avatar": f"{AVATAR_BASE_URL}/yui.png",
            "chance": 1.0
        }
    ],
    "なぎさ": [
        {
            "name": "なぎさ",
            "file": "nagisa.txt",
            "avatar": f"{AVATAR_BASE_URL}/nagisa.png",
            "chance": 1.0
        }
    ],
    "ことね": [
        {
            "name": "ことね",
            "file": "kotone.txt",
            "avatar": f"{AVATAR_BASE_URL}/kotone.png",
            "chance": 1.0
        }
    ],
    "はる": [
        {
            "name": "はる",
            "file": "haru.txt",
            "avatar": f"{AVATAR_BASE_URL}/haru.png",
            "chance": 1.0
        }
    ],
    "かなで": [
        {
            "name": "かなで",
            "file": "kanade.txt",
            "avatar": f"{AVATAR_BASE_URL}/kanade.png",
            "chance": 1.0
        }
    ],
    "めぐ": [
        {
            "name": "めぐ",
            "file": "megu.txt",
            "avatar": f"{AVATAR_BASE_URL}/megu.png",
            "chance": 1.0
        }
    ],
    "みお": [
        {
            "name": "みお",
            "file": "mio.txt",
            "avatar": f"{AVATAR_BASE_URL}/mio.png",
            "chance": 1.0
        }
    ]
}
