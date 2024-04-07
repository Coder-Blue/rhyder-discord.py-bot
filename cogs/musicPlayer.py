import discord
from discord.ext import commands
import wavelink
import logging
from typing import cast

class Music(commands.Cog):
    def __init__(self, bot):
        super().__init__()

        discord.utils.setup_logging(level = logging.INFO)

    @commands.command(name= "play", aliases = ["p", "choi"])
    async def play(self, ctx: commands.Context, *, query: str, member:discord.Member = None) -> None:
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info(f"|SEND PLAY|: Nhận lệnh lệnh n#play và đang trả lời {name}.")

        if not ctx.guild:
            return

        player: wavelink.Player
        player = cast(wavelink.Player, ctx.voice_client)

        if not player:
            try:
                player = await ctx.author.voice.channel.connect(cls = wavelink.Player, self_mute = False, self_deaf = True)
            except AttributeError:
                logging.info("|SEND PLAY|: Lỗi chưa kết nối phòng.")
                await ctx.send("Hãy vào phòng trước khi sử dụng lệnh này.")
                return
            except discord.ClientException:
                logging.info("|SEND PLAY|: Lỗi không thể vào phòng")
                await ctx.send("Tôi chưa thể hoặc không thể vào phòng này, hãy thử lại.")
                return

        player.autoplay = wavelink.AutoPlayMode.enabled

        if not hasattr(player, "home"):
            player.home = ctx.channel
        elif player.home != ctx.channel:
            await ctx.send(f"Bạn chỉ có thể chơi nhạc ở trong {player.home.mention}, nếu như bot đã có sẵn trong đó.")
            return

        tracks: wavelink.Search = await wavelink.Playable.search(query)

        if not tracks:
            await ctx.send(f"{ctx.author.mention} - Không tìm ra bài nào có tên như vậy, hãy thử lại.")
            return

        if isinstance(tracks, wavelink.Playlist):
            added: int = await player.queue.put_wait(tracks)
            await ctx.send(f"Thêm được playlist **`{tracks.name}`** ({added} songs) vào hàng chờ.")
        else:
            track: wavelink.Playable = tracks[0]
            await player.queue.put_wait(track)
            await ctx.send(f"Thêm được **`{track}`** vào hàng chờ.")

        if not player.playing:
            await player.play(player.queue.get(), volume = 30)

        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass

    @commands.command(name = "nightcore", aliases = ["nc", "N", "n", "alime"])
    async def nightcore(self, ctx: commands.Context) -> None:
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info(f"|SEND NIGHTCORE|: Nhận lệnh lệnh n#nightcore và đang trả lời {name}.")
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        filters: wavelink.Filters = player.filters
        filters.timescale.set(pitch = 1.2, speed = 1.2, rate = 1)
        await player.set_filters(filters)

        await ctx.message.add_reaction("\u2705")

    @commands.command(name = "skip", aliases = ["s", "boqua"])
    async def skip(self, ctx: commands.Context, member:discord.Member = None) -> None:
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info(f"|SEND SKIP|: Nhận lệnh lệnh n#skip và đang trả lời {name}.")
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        await player.skip(force = True)
        await ctx.message.add_reaction("\u2705")

    @commands.command(name = "disconnect", aliases = ["dc", "leave", "l", "cut"])
    async def disconnect(self, ctx: commands.Context, member:discord.Member = None) -> None:
        if member == None:
            member = ctx.author
        name = member.display_name
        logging.info(f"|SEND disconnect|: Nhận lệnh n#disconnect và đang trả lời {name}.")
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        await player.disconnect()
        await ctx.message.add_reaction("\u2705")


async def setup(bot):
    await bot.add_cog(Music(bot))