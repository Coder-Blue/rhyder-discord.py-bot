import discord
from discord.ext import commands
import wikipedia as wiki
import logging

class WikiVN(commands.Cog):
    def __init__(self, cilent):
        super().__init__()

        discord.utils.setup_logging(level=logging.INFO)

    @commands.command(name = "search", aliases = ["wiki", "wi"])
    async def search(self, ctx, *, quest, member:discord.Member = None):
        wiki.set_lang('vi')
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info (f"|SEND SEARCH|: Nhận lệnh n!search và đang trả lời người dùng {name}.")
        await ctx.send(f'Hãy chờ đợi kết quả! **"{name}"**.\nĐang tìm kiếm cho từ khóa **"{quest}"** trên Wikipedia!')
        ans = wiki.summary(quest, sentences=5)
        page = wiki.page(quest)
        urlans = page.url
        await ctx.reply(f"° {ans}\n\n° **Bài viết gốc trên Wikipedia tiếng Việt:** {urlans}")

async def setup(bot):
    await bot.add_cog(WikiVN(bot))