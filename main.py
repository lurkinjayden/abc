import os
import discord
import io
from PIL import Image
import random
from discord.ext import commands
import asyncio
import requests
import json
import re
from io import BytesIO
import instaloader
from pytube import YouTube
from moviepy.editor import *
import time
from datetime import datetime, timedelta


TOKEN = "MTIwMDExMDQ2MjQ4Mjc4MDE5MA.GyHJGb.C4zE_5qepi7VgBea4VeVOrQW1W7mW687ARoMDs"

one_victim = None
seven_victim = None
autoreply_victim = None
autoreply_user = None
autoreply_messages = []
include_base = True
stopreacting = False

bold = False

pack_victim = None
packs = []

stop = False

base_message = open('base.txt', 'r',).read()

with open('pack.txt', 'r', encoding='utf-8') as pack:
    reply_messages = pack.read().splitlines()

with open('reply.txt', 'r') as reply_file:
    reply = reply_file.read()

speed = 0.000000000000000000000000000000000000000000000000000101010011001010101001010101000110010010101001010101001101001010100101010010101000101010010101000
keep_going = True
client = commands.Bot(command_prefix= "///", self_bot=True)


async def send_messages(channel, messages):
    for msg in messages:
        await channel.send(msg)
        await asyncio.sleep(0.000001)

@client.event
async def on_ready():
    print(f"logged in as {client.user.name}")

@client.event
async def on_message(message):
    global stopreacting, one, seven, one_victim, seven_victim, autoreply_user, autoreply_victim, autoreply_messages, include_base, stop, pack_victim, packs, flood_message, stop_sending, bold
 
    if message.author == client.user and message.content.startswith('.stream'):
        stream_status = message.content[len('.stream'):].strip()
        await client.change_presence(activity=discord.Streaming(name=stream_status, url="https://twitch.tv/xxx"))

    if message.author == client.user:
        if not stopreacting:
            await message.add_reaction('☠️')
    if message.author == client.user and message.content == '0':
        await message.delete()
        stopreacting = not stopreacting


    if message.author == client.user and message.content == '88':
         await message.delete()
         sentences = ['UR NOT STEPPING TO ME LMFAO WDF',
            'COME DIE LMFAO',
            'NIGGA IS ASS AS FUCK',
            '☠️ 😭',
            'UR GONNA STAY THE FUCK DOWN',
            'UR FUCKING SHITTY',
            'DIE TO UR FUCKING LORD',
            '# LOLOL ',
            '# OUTLAST ME I WONT STOP ',
            '☠️ 😭',
            'NIGGA WHERE THE FUCK ARE U',
            '# NIGGA FUCKING DIED',
            '# UR SHIT LMAO IM CLOWNING U',
            'SLOW FUCK I WIN LMFAOOO',
            '# NIGGAS SLOW AS FUCK',
            'UR ASS',
            'SIT THE FUCK DOWN RЕTARD LMFAO',
            'UR A GAY FAGGОT LMAO',
            '# U SUCK NIGGA',
            'GO FASTER BITCH',
            'COME HERE',
            'UR A FUCK TOY',
            'U WONT DO SHIT',
            'STUPID FUCK',
            '# SLOW ASS NIGGA',
            '# UR A FUCKING LOSER',
            'STAY DOWN',
            'POOR ASS FUCK NIGGA',
            'U CANT OUTLAST ME',
            'I WIN U FUCKING RETARD LFMAO UR NOT DOING SHIT',
            '# U CANT FUCKING PRESSURE',
            'WHY THIS NIGGA SOME SHIT LMFAO',
        ]
         await send_messages(message.channel, sentences)


    if message.author == client.user and message.content == '87':
        await message.delete()
        sentences = ['IS IT A BIRD',
            'IS IT A PLANE',
            'NO',
            '# ITS JUST THIS WEAK ASS NIGGA',
            'LO',
            'L',
            'O',
            '# UR A FUCKING LOSER',
            'https://tenor.com/view/joker-why-so-serious-serious-gif-11972349',
            'WEAK',
            'ASS',
            'FUCK',
            'TOY',
            'LOLOL',
            '# UR FUCKING SLOW RЕTARD',
            '# U SUCK NIGGA',
            'GO FASTER BITCH',
            'COME HERE',
            'UR A FUCK TOY',
            'U WONT DO SHIT',
            '# SLOW ASS NIGGA',
            '# UR A FUCKING LOSER',
            'STAY DOWN',
            'POOR ASS FUCK NIGGA',
            'U CANT OUTLAST ME',
            '# U CANT FUCKING PRESSURE',
            'LOL',
            '# WEAK ASS FUCKING LOSER',
            'LO',
            'L',
            'O',
        ]
        await send_messages(message.channel, sentences)

    if message.author == client.user and message.content.startswith('ig'):
        username = message.content.split(' ')[1]
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        await message.channel.send(profile.profile_pic_url)

    if message.author == client.user and message.content.startswith('7'):
        user_id = None
        if message.mentions:
            await message.delete()
            user_id = message.mentions[0].id
        else:
            try:
                user_id = int(message.content.split(' ')[1])
            except ValueError:
                pass
        if user_id:
            seven_victim = user_id
            packs = []
            with open('7.txt', 'r', encoding='utf-8') as seven:
                for line in seven:
                    packs.append(line.strip())                 
            random.shuffle(packs)
            include_base = False
            stop_sending = False
            print(f"now hoeing {message.author.mention}")
            while not stop_sending:  # add while loop here
                for msg in packs:
                    if stop_sending:  # check stop_sending here
                        break
                    words = msg.split()
                    formatted_message = '\n'.join(words)
                    flood_message = f'<@{user_id}>\n{formatted_message}'
                    try:
                        await message.channel.send(flood_message)
                    except discord.errors.HTTPException as e:
                        if 'The write action you are performing' in str(e):
                            print('rate limited, sleeping for 10 seconds')
                            time.sleep(10)
                            continue
                    await asyncio.sleep(2)

    if message.author == client.user and message.content.startswith('5'):
        user_id = message.mentions[0].id if message.mentions else None
        if user_id:
                await message.delete()
                autoreply_user = user_id
                autoreply_messages = [f'{base_message} {msg.strip()}' for msg in message.content[2:].split(',')]
                include_base = True
                print(f"ar set for {message.author.mention}: {autoreply_messages}")

    if message.author == client.user and message.content.startswith('4'):
            user_id = message.mentions[0].id if message.mentions else None
            if user_id:
                await message.delete()
                autoreply_user = user_id
                autoreply_messages = [f'{msg.strip()}' for msg in message.content[2:].split(',')]
                include_base = False
                print(f"ar set for {message.author.mention}: {autoreply_messages}")

    if message.author == client.user and message.content.startswith('2'):
        user_id = message.mentions[0].id if message.mentions else None
        if user_id:
            await message.delete()
            pack_victim = user_id
            packs = []
            with open('pack.txt', 'r', encoding='utf-8') as pack:
                packs = [line.strip() for line in pack]
            include_base = False
            print(f"now hoeing {message.author.mention}")

    if message.author == client.user and message.content.startswith('1'):
        user_id = None
        if message.mentions:
            await message.delete()
            user_id = message.mentions[0].id
        else:
            try:
                user_id = int(message.content.split(' ')[1])
            except ValueError:
                pass
        if user_id:
            one_victim = user_id
            packs = []
            with open('1.txt', 'r', encoding='utf-8') as one:
                for line in one:
                    packs.append(line.strip())           
            random.shuffle(packs)
            include_base = False
            stop_sending = False
            print(f"now hoeing {message.author.mention}")
            number = 1
            while not stop_sending:
                for msg in packs:
                    if stop_sending:
                        break
                    flood_message = f'# <@{user_id}> {msg} {number}'
                    number += 1
                    try:
                        await message.channel.send(flood_message)
                    except discord.errors.HTTPException as e:
                        if 'The write action you are performing' in str(e):
                            print('rate limited, sleeping for 10 seconds')
                            time.sleep(10)
                            continue
                    await asyncio.sleep(2)

    elif message.author == client.user and message.content == 'quit':
            message = None
            one_victim = None
            seven_victim = None
            autoreply_victim = None
            autoreply_messages = []
            pack_victim = None
            flood_message = None
            packs = None
            stop_sending = True
            print(f"stopped hoeing")
 
    elif message.author.id == autoreply_user and autoreply_messages:
        for reply in autoreply_messages:
            await message.channel.send(reply)
    
    elif message.author.id == pack_victim and packs:
        pack = random.choice(packs)
        await message.reply(pack)

    if message.author == client.user and message.content == 'Halt!':
        await message.delete()
        stop = True
    if message.author == client.user and message.content.startswith('gc'):
        await message.delete()
        stop = False
        args = message.content.split()
        new_names = ' '.join(args[1:]).split(',')
        gcid = message.channel.id

        number = 0
        while not stop:
            gc = client.get_channel(gcid)
            if isinstance(gc, discord.GroupChannel):
                for new_name in new_names:
                    name = f"{new_name.strip()} {number}"
                    await gc.edit(name=name)
                    await asyncio.sleep(0.01)
                    number += 111


    if message.author == client.user and message.content.startswith('pfp'):
        content = message.content.split()
        if len(content) > 1:
            try:
                user_id = int(content[1])
                member = client.get_user(user_id)
            except ValueError:
                member = message.mentions[0] if message.mentions else message.author
        else:
            member = message.author
        await message.channel.send(member.avatar_url)

    if message.author == client.user and message.content.startswith('.t'):
        await message.delete()
        args = message.content.split()[1:]
        try:
            if len(args) > 0 and args[0].isdigit():
                channel_id = int(args[0])
                channel = client.get_channel(channel_id)
                if channel is None:
                    print(f"channel doesnt exist: {channel_id}")
                    return
                msg = ' '.join(args[1:])
            else:
                channel = message.channel
                msg = ' '.join(args)

            words = msg.split(' ')
            for word in words:
                await channel.send(word)
                await asyncio.sleep(0.001)
        except discord.Forbidden:
            await print("no perms")
        except Exception as e:
            await print(f"error: {str(e)}")

    if message.author == client.user:
        if bold and not message.content == '.bold':
            edited_message = "# " + message.content
            await message.edit(content=edited_message)
    if message.author == client.user and message.content == '.bold':
        await message.delete()
        bold = not bold

    if message.author == client.user and message.content.startswith('.download'):
        link = message.content.split(' ')[1]

        if "youtube.com" in link or "youtu.be" in link:
            yt = YouTube(link)
            video = yt.streams.first().download()
            audio = VideoFileClip(video).audio
            audio.write_audiofile('output.mp3', bitrate='320k')
            await message.channel.send(file=discord.File('output.mp3'))
            # os.remove('output.mp3')  # delete the file after sending it

        elif "soundcloud.com" in link or "on.soundcloud.com" or "m.soundcloud.com" in link:
            track = api.resolve(link) # type: ignore
            assert type(track) is track

            filename = f'{track.artist} - {track.title}.mp3'
            print(f"Filename: {filename}")  # Check the filename
            try:
                with open(filename, 'wb+') as file:
                    track.write_mp3_to(file)
            except IOError as e:
                await message.channel.send(f"file error: {str(e)}")
                return

            await message.channel.send(file=discord.File(filename))

            cover_art_url = track.artwork_url.replace('-large', '-t3000x3000')
            response = requests.get(cover_art_url)
            img = Image.open(io.BytesIO(response.content))

            cover_path = 'cover.png'
            img.save(cover_path)

            await message.channel.send(file=discord.File(cover_path))

            if os.path.exists(cover_path):
                os.remove(cover_path)
        elif "pinterest.com" in link:
            content = requests.get(link).text
            if "video-snippet" in content:
                match = re.findall(r'<script data-test-id=\"video-snippet\".+?</script>', content)
                j = json.loads(match[0].replace('<script data-test-id=\"video-snippet\" type=\"application/ld+json\">', "").replace("</script>", ""))
                media_link = j["contentUrl"]
            else:
                match = re.findall(r'<script data-test-id=\"leaf-snippet\".+?</script>', content)
                j = json.loads(match[0].replace('<script data-test-id=\"leaf-snippet\" type=\"application/ld+json\">', "").replace("</script>", ""))
                media_link = j["image"]
            response = requests.get(media_link)
            filename = 'pinterest_media.png' if not "video-snippet" in content else 'pinterest_media.mp4'
            with open(filename, 'wb') as file:
                file.write(response.content)
            await message.channel.send(file=discord.File(filename))
        else:
            await message.channel.send("wrong link")



    if message.author == client.user:
        if message.content == ',':
            async for msg in message.channel.history(limit=100):
                if msg.author == client.user and (message.created_at - msg.created_at).total_seconds() < 10:
                    await msg.delete()
                    await asyncio.sleep(0.000000000000001)
        else:
            await client.process_commands(message)

    if message.author == client.user:
        if message.content.startswith('.c'):
            content = message.content[2:].strip()
            if content.isdigit():
                num_messages_to_delete = int(content)
                async for msg in message.channel.history(limit=num_messages_to_delete):
                    if msg.author == client.user:
                     if not message.is_system():
                        await msg.delete()
                        await asyncio.sleep(0.000000000000001)
        else:
            await client.process_commands(message)

    if message.author == client.user and message.content == '.delroles':
        roles = message.guild.roles
        for role in roles:
            try:
                if role != message.guild.default_role:
                    await role.delete()
                    print(f"deleted role: {role.name}")
            except discord.Forbidden:
                print(f"couldnt delete role: {role.name}")
            except discord.HTTPException:
                print(f"couldnt delete role: {role.name}, it might have been deleted already.")
        time.sleep(5)

    if message.author == client.user and message.content == '.help':
        help_message = """
         # FUCK LYFESTYLE
        - `stream <text>`: sets a streaming status
        - `88`: autopressure
        - `87`: another autopressure
        - `7 @user`: flood autopressure
        - `5 @user <message>`: sets a flood autoreply with your message to the mentioned user
        - `4 @user <message>`: sets a regular autoreply (no flood).
        - `2 @user`: another autoreply
        - `1 @user`: slow autopressure: pings every 2 seconds or so
        - `quit`: turns off the autoreply
        - `gc <name>`: loops the gc name
        - `stop`: stops the gc changer
        - `.bold`: makes your messages bold (toggle)
        - `pfp @user`: grabs the pfp of a user.
        - `.ig <username>`: grabs a pfp from an instagram username
        - `.download <youtube or soundcloud link>`: converts a youtube or soundcloud link into an mp3; idk why i made this but its pretty useful
        - `.t <message>` : basically an autotyper idk why i made this but yeah
        - `,`: deletes your messages sent within 20 seconds, dont ask why i made this
        - `.c <number>`: deletes the number of messages (from yourself)
        - `.delroles`: deletes every role from a server (will most likely cause you to get fucked by bleed antinuke)
        """
        await message.channel.send(help_message)


client.run(TOKEN, bot=False)
