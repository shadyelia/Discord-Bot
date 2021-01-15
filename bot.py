import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='~')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
