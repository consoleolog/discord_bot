import os
from typing import Any
import discord
from discord import Intents
from config import *
from service.ai_service import DeepLService, AIService

CHANNEL_ID = int(os.environ["CHANNEL_ID"])  # 채널 ID는 정수로 변환해야 함

deepl_service = DeepLService()
ai_service = AIService()

class MyClient(discord.Client):

    def __init__(self, *, intents: Intents, **options: Any):
        super().__init__(intents=intents, **options)
        self.img_size = {
            "small": "256x256",
            "medium": "512x512",
            "large": "1024x1024",
            "wide": "1792x1024",
            "tall": "1024x1792"
        }

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        await self.change_presence(status=discord.Status.online, activity=discord.Game(""))

    async def on_message(self, message):
        # 메시지가 봇 자신의 메시지인지 확인하고, 그렇다면 무시
        if message.author == self.user:
            return

        # 특정 채널에서만 메시지를 처리
        if message.channel.id == int(TEST_CHANNEL_ID):
            # 메시지 내용 처리 (유저 이름 확인)
            print(f'Message from {message.author}: {message.content}')
            if message.author == "cheayull":  # message.author.name 사용
                translate_content = deepl_service.translate({
                    "content": message.content,
                    "target_lang": "EN-US"
                })
                print(translate_content)

                url = ai_service.handling_image({
                    "job": "GENERATE",
                    "content": translate_content,
                    "size": self.img_size["wide"]
                })
                print(url)

                ai_service.download_image({
                    "url": url,
                    "image_name": "test.jpg"
                })
                await message.channel.send(url)


# Intents 설정
intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
