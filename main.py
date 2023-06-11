import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user} и я помогу вам следить за экологией!')
    await ctx.send("Чтобы держать мир в чистоте нужно соблюдать очень простые правила!")
    await ctx.send("Введите команду $nature, чтобы получить информацию.")


bot.run("MTExNzQ1MDYzNDU4OTg5NjcyNA.GWpzSJ.zYKmF92Exw5WusrDDAJ6o6dz2J1FPKatkblhS8")







