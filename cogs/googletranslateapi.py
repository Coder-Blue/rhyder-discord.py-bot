import discord
from discord.ext import commands
import googletrans
from googletrans import Translator
import logging

class GGTranslate(commands.Cog):
    def __init__(self, cilent):
        super().__init__()

        discord.utils.setup_logging(level=logging.INFO)

    @commands.command(name = "dich", aliases = ["translate", "trans", "d", "t"])
    async def dich(self, ctx, *, quest, member:discord.Member = None):
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info (f"|SEND DICH|: Nhận lệnh n!dich và đang trả lời người dùng {name}.")
        await ctx.send (f"Tôi đang nhận câu nói tiếng Việt: **{quest}** của bạn **{name}** để dịch sang tiếng Anh, chờ trong giây lát!")
        tools = Translator()
        answer = tools.translate(quest, src = "vi", dest = "en")
        dichans = answer.text
        embed = discord.Embed(
            title = 'Từ Google Dịch,',
            description = dichans,
            colour = discord.Colour.blue()
        )
        embed.set_footer(text="Giao tiếp với API bằng RHYDER!")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/910098562837278722/1177936879836991588/Google_Translate_logo.svg.png?ex=65745235&is=6561dd35&hm=476860e9e8c5f123a2bbf260c1793d16f3aea228b5e373fde650aa4bded24fff&=&format=webp&width=468&height=468")
        await ctx.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(GGTranslate(bot))