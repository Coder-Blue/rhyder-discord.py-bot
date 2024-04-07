import discord
from discord.ext import commands
import logging

class Info(commands.Cog):
    def __init__(self, bot):
        super().__init__()

        discord.utils.setup_logging(level=logging.INFO)

    @commands.command()
    async def info(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info(f"|SEND INFO|: Nhận lệnh n#info và đang trả lời người dùng {name}.")
        embed = discord.Embed(
            title = f'Tôi là Bot Âm nhạc Rái - đơ!',
            url = "https://discord.com/api/oauth2/authorize?client_id=1179066608250015835&permissions=58273981529921&scope=bot",
            description="Được làm ra bởi Sh1ro\nTôi được tích hợp Wavelink bên trong để phát nhạc chất lượng cao trong Discord.\nTôi cũng có tính năng phụ là làm AI Chat Bot.",
            colour=discord.Color.red()
            )
        embed.set_footer(text = f"Viết bởi Sh1ro `Anh Quân`, viết với Discord.py và Wavelink.")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/917782807386914856/1179070052205604985/icon.png?ex=6578718e&is=6565fc8e&hm=034fa4a8bcb0a189dad401780a4d99cda3f309925ff18a9fb45dc85b75595e2b&")
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info (f'|SEND PING|: Nhận lệnh n#ping và đang trả lời người dùng {name}.')
        embed = discord.Embed(
            description= "° Tôi vẫn còn online nhé!",
            colour=discord.Color.red()
            )
        embed.set_author(name="Rhyder Music Bot")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/917782807386914856/1179070052205604985/icon.png?ex=6578718e&is=6565fc8e&hm=034fa4a8bcb0a189dad401780a4d99cda3f309925ff18a9fb45dc85b75595e2b&")
        await ctx.send(embed=embed)

    @commands.command()
    async def donate(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info(f'|SEND DONATE|: Nhận lệnh n#donate và đang trả lời người dùng {name}.')
        embed = discord.Embed(
            title = f"Cảm ơn bạn **{name}** đã gửi tiền cafe cho **ông Sh1ro**!",
            url= "https://www.facebook.com/noah.tran1109",
            colour=discord.Color.red()
            )
        embed.set_author(name="Từ Rhyder Music Bot,")
        embed.set_image(url="https://media.discordapp.net/attachments/910098562837278722/1171418348555350016/IMG_4049.jpg?ex=655c9b5a&is=654a265a&hm=94db44b054d329abe59536700681a969b4cc45b8678683aec9657948bcee65ee&=&width=468&height=468")
        embed.set_footer(text="Cảm ơn mọi người siêu nhiều vì sự ủng hộ!")
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))