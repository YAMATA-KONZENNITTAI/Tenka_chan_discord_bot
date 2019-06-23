import discord
import random
import asyncio
import Tenka_random_serihu as trs
import Tenka_commands as tc
from bot_Tokens import tenka_Token
from identifications import *
import Images
import Voice_Lines as vl

client = discord.Client()

#テキストチャンネルのIDを
CH_ID = None
#ボイスチャンネルのIDを
voice_ID = None


#好感度管理する　辞書型
global likeability

#起動時に関する処理
@client.event
async def on_ready():
    channel = client.get_channel(CH_ID)
    global likeability
    #ユーザに対応した辞書型の好感度管理変数
    likeability = {str(i):0 for i in client.users}
    #起動確認
    print("甜花……頑張りましゅ！　あ、頑張ります……！")
    await channel.send(trs.greetings[random.randint(0,len(trs.greetings)-1)])

#メッセージを処理
@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    #タッチよくない
    if message.content == tc.touch[0]:
        await message.channel.send(trs.touch_bad[random.randint(0,len(trs.touch_bad)-1)])

    #たっち
    if message.content == tc.touch[1]:
        await message.channel.send(trs.touch_good[random.randint(0,len(trs.touch_good)-1)])

    #朝の挨拶
    if message.content in tc.morning:
        await message.channel.send(trs.greetings[random.randint(0,len(trs.greetings)-1)])

    #挨拶
    if message.content in tc.greet:
        await message.channel.send(trs.greetings[random.randint(0,len(trs.greetings)-1)])
    
    #おやすみ
    if message.content in tc.good_night:
        await message.channel.send(Images.Oyasuminasai)
    
    #なーちゃん
    if message.content in tc.to_amana:
        await message.channel.send(trs.against_amana[random.randint(0,len(trs.against_amana)-1)])

    #ひぃん
    if message.content in tc.hiin:
        print(vl.hiin)
        channel = client.get_channel(voice_ID)
        if message.guild.voice_client is None:
            vc = await channel.connect()
        else:
            vc = message.guild.voice_client
        vc.play(discord.FFmpegPCMAudio(vl.hiin))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1.0
        while not vc.is_playing():
            await asyncio.sleep(1)

    #あう…
    if message.content in tc.auu:
        channel = client.get_channel(voice_ID)
        if message.guild.voice_client is None:
            vc = await channel.connect()
        else:
            vc = message.guild.voice_client
        vc.play(discord.FFmpegPCMAudio(vl.au))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 0.7
        while not vc.is_playing():
            await asyncio.sleep(1)

    #にへへ
    if message.content in tc.nihehe:
        channel = client.get_channel(voice_ID)
        if message.guild.voice_client is None:
            vc = await channel.connect()
        else:
            vc = message.guild.voice_client
        vc.play(discord.FFmpegPCMAudio(vl.nihehe))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1.0
        while not vc.is_playing():
            await asyncio.sleep(1)

    #がんばります！！
    if message.content in tc.ganbaru:
        channel = client.get_channel(voice_ID)
        if message.guild.voice_client is None:
            vc = await channel.connect()
        else:
            vc = message.guild.voice_client
        vc.play(discord.FFmpegPCMAudio(vl.ganbarimasu))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1.0
        while not vc.is_playing():
            await asyncio.sleep(1)

    #ばいばい
    if message.content in tc.bye:
        for voice_client in client.voice_clients:
            await voice_client.disconnect()

#甜花ちゃんをDiscordへお送りするよ
client.run(tenka_Token)
