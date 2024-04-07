import discord
from discord.ext import commands
import wavelink
import os
from dotenv import load_dotenv
import logging
import asyncio

load_dotenv()
TOKEN = os.getenv("TOKEN")

class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.all()
        intents.message_content = True

        discord.utils.setup_logging(level = logging.INFO)
        super().__init__(command_prefix = 'n#', intents = intents)

    async def setup_hook(self) -> None:
        nodes = [wavelink.Node(uri = "http://localhost:2929", password = "youshallnotpass")]
        await wavelink.Pool.connect(nodes = nodes, client = self, cache_capacity = 100)

        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                logging.info(f"Đã load được các tác vụ mở rộng: {filename}")

    async def on_ready(self) -> None:
        await self.change_presence(status= discord.Status.idle, activity= discord.Game(name="n# ở server Trại Cai nghiện!"))
        logging.info(f"Đang đăng nhập với {self.user} | {self.user.id}")
        print ("-------------------------------------------------------------------------------------------------")

    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload) -> None:
        logging.info(f"Wavelink Node đã kết nối với: {payload.node!r} | Resumed: {payload.resumed}")

    async def on_wavelink_track_start(self, payload: wavelink.TrackStartEventPayload) -> None:
        player: wavelink.Player | None = payload.player
        if not player:
            return

        original: wavelink.Playable | None = payload.original
        track: wavelink.Playable = payload.track

        embed: discord.Embed = discord.Embed(title = "Đang chơi")
        embed.description = f"**{track.title}** bởi `{track.author}`"

        if track.artwork:
            embed.set_image(url = track.artwork)

        if original and original.recommended:
            embed.description += f"\n\n`Bài này đã được đề xuất từ {track.source}`"

        if track.album.name:
            embed.add_field(name = "Album", value = track.album.name)

        await player.home.send(embed = embed)



bot: Bot = Bot()


@bot.command(name = "reload", aliases = ["rel"])
@commands.has_permissions(administrator=True)
async def reload(ctx: commands.Context, member:discord.Member = None) -> None:
    if member == None:
        member = ctx.author
    name = member.display_name
    logging.info (f"|SEND RELOAD|: Nhận lệnh n#reload và đang trả lời người dùng {name}.")

    embed = discord.Embed(
        title = f'Tôi là Bot Âm nhạc Rái - đơ!',
        url = "https://discord.com/api/oauth2/authorize?client_id=1179066608250015835&permissions=58273981529921&scope=bot",
        description= f"° Đã reload lại các tính năng cho {name}!",
        colour=discord.Color.red()
    )
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/917782807386914856/1179070052205604985/icon.png?ex=6578718e&is=6565fc8e&hm=034fa4a8bcb0a189dad401780a4d99cda3f309925ff18a9fb45dc85b75595e2b&")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.reload_extension(f"cogs.{filename[:-3]}")

    await ctx.reply(embed=embed)

async def main() -> None:
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())