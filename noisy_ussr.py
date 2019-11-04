import discord
import time

TOKEN = 'YOUR TOKEN'

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print('ログインしました')
    print('------')


@client.event
async def on_message(message):
    #USSRが含まれたメンションが飛んできたら処理開始
    if client.user in message.mentions:
        if 'USSR' in message.content or 'CCCP' in message.content:
            target = message.author.voice.channel.id
            vc = await client.get_channel(target).connect()
            vc.play(discord.FFmpegPCMAudio('USSR.mp3'))
            #ここで再生時間を調整
            time.sleep(13)
        elif '音割れポッター' in message.content:
            target = message.author.voice.channel.id
            vc = await client.get_channel(target).connect()
            vc.play(discord.FFmpegPCMAudio('potter.mp3'))
            time.sleep(9)
        
        await vc.disconnect()

client.run(TOKEN)
            
