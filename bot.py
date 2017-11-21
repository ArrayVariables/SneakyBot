#Imports
import discord
from discord.ext import commands
import traceback


with open("token.txt", 'r') as f:
    token = f.read().strip('\n')

    
#Stuff
initial_extensions = ('cogs.Admin', 'cogs.fun')


                      
bot = commands.Bot(command_prefix='!', description='A bot for sneakys help server!')
bot.remove_command("help")

#The first step to a great bot! On ready events!

@bot.event
async def on_ready():
    print('\n\nLogged in as: {} - {}\nVersion: {}\n'.format(bot.user.name, bot.user.id, discord.__version__))
    await bot.change_presence(game=3(name='The server..'))
    
    
    
#Cog Loader


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}.'.format(extension))
            traceback.print_exc()
        print('Successfully logged in and booted...!')
    
#The super super super token that is locked away by ninjas and flying penguins?

bot.run(token)
