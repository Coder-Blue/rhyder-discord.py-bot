import discord
from discord.ext import commands
import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

load_dotenv()
KEY = os.getenv("GOOGLE_API")

genai.configure(api_key = KEY)

class Gemini(commands.Cog):
    def __init__(self, bot):
        super().__init__()

        discord.utils.setup_logging(level = logging.INFO)

    @commands.command(name = "ask", aliases = ["a", "hoi"])
    async def ask(self, ctx: commands.Context, *, prompt, member:discord.Member = None):
        if member == None:
            member = ctx.author
            name = member.display_name
            logging.info (f"|SEND ASK|: Nhận lệnh n!ask và đang trả lời người dùng {name}.")
            await ctx.send (f"Gemini đang nhận câu hỏi **{prompt}** của bạn **{name}**, chờ trong giây lát!")

        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 1024,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)

        convo = model.start_chat(history = [])

        chat_history = []
        chat_history.append(prompt)
        questions = "\n".join(chat_history)

        convo.send_message(questions)
        await ctx.reply(f"° Câu trả lời từ **Gemini**:\n{convo.last.text}")

async def setup(bot):
    await bot.add_cog(Gemini(bot))