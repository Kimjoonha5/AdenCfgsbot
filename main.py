import discord
from discord.ext import commands

TOKEN = 'MTM4NjI2ODk5OTA4NzY4NTYzMg.GoGWnk.zuxyOwMVrv_DeZsm5-59s2PNvbqvN9QGJ213LQ'
OWNER_ID = 1307300556548866161  

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def tb(ctx, member: discord.Member):
    if ctx.author.id != OWNER_ID:
        await ctx.send(" Only the owner can use this command.")
        return
    try:
        with open(r'C:\Users\김대혁\Downloads\tb\NNNTB.json', 'rb') as f:
            await member.send("Thank you for your purchase!", file=discord.File(f, 'NNNTB.json'))
        await ctx.send(f" Successfully sent to {member.mention}")
    except Exception as e:
        await ctx.send(f" Failed to send: {e}")

bot.run(TOKEN)
