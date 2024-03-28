import discord 
from discord.ext import comands
import dotenv

client = comands.Bot(command_prefix = "!")

@client.event()
async def on_ready() -> None:
    print("List your recommended films: ")
    print("---------------------")


@client.command()
async def hello(ctx) -> str:
    await ctx.send("Hello! How are you today\
How about watching a movie?\
                   ")
token = dotenv.load_dotenv()
token.getenv("TOKEN")

client.run(token.getenv("TOKEN"))
    
