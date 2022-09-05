from edamino import Bot, Context, logger
from edamino.objects import UserProfile
from edamino.api import File
import random

bot = Bot(email='ment---3zolJcUB9Hxb@wwjmp.com', password='!zetking1488', prefix="")


hellotxt = ['привет!', 'че как?', 'хай', 'здарова']
@bot.event()
async def on_ready(profile: UserProfile):
    logger.info(f'{profile.nickname} ready')
    

@bot.command('привет')
async def echo(ctx: Context):
    await ctx.reply(random.choice(hellotxt))
    
@bot.command('image')
async def on_image(ctx: Context):
    image = File.load('Hui.jpg')
    await ctx.send_image(image)


if __name__ == '__main__':
    bot.start()