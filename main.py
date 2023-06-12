import discord
import os
from discord.ext import commands
from random import choice

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
    await ctx.send("Введите команду $garbage, чтобы увидеть картинки свалок и мусора.")

@bot.command()
async def nature(ctx):
    await ctx.send('Как спасти природу: 8 шагов, которые может сделать каждый:')
    await ctx.send('1.ЭКОНОМЬТЕ РЕСУРСЫ')
    await ctx.send('2.РАЗДЕЛЯЙТЕ МУСОР')
    await ctx.send('3.СДАВАЙТЕ ВТОРСЫРЬЁ')
    await ctx.send('4.ВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ')
    await ctx.send('5.ИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ')
    await ctx.send('6.ВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ')
    await ctx.send('7.ОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ')
    await ctx.send('8.ПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА')

@bot.command()
async def garbage(ctx):
    with open('images1/garbage2.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('"Введите команду $nature, чтобы получить информацию.')


bot.run("")
