import discord
import time

client = discord.Client(intents=discord.Intents.default())


def write_file(message):
    fh = open('commands.txt', 'w')
    fh.write("cmd="+message.content)
    fh.close()


def read_file():
    f = open('reply.txt', 'r')
    reply = f.read()
    f.close()
    return reply[3:]


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await member.channel.send(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):

    id = client.get_guild(781365287474954250)
    if message.content.find("-help") != -1 and message.content.find("-") == 0:
        await message.channel.send("here are the commands that you can use to command  the bot:"
                                   "\n-hello-------to tell hello to the bot\n-users------get number of users in the server"
                                   "\n-news------to get some local news updates\n-jokes------to get somethinng to make you laugh"
                                   "\n-rsearch---to search something on reddit"
                                   "\n-gsearch---get anything from google"
                                   "\n-stop-------to stop the brains of the bot")
    elif message.content.find("-hello") != -1 and message.content.find("-") == 0:
        write_file(message)
        await message.channel.send("hello from the bot")
    elif message.content == "-users" and message.content.find("-") == 0:
        write_file(message)
        await message.channel.send(f"""No of members {id.member_count}""")
    elif message.content.find("-news") != -1 and message.content.find("-") == 0:
        write_file(message)
        time.sleep(4)
        n = read_file()
        await message.channel.send(n)
    elif message.content.find("-jokes") != -1 and message.content.find("-") == 0:
        write_file(message)
        time.sleep(4)
        j = read_file()
        await message.channel.send(j)
    elif message.content.find("-rsearch") != -1 and message.content.find("-") == 0:
        write_file(message)
        time.sleep(4)
        r = read_file()
        await message.channel.send(r)
    elif message.content.find("-gsearch") != -1 and message.content.find("-") == 0:
        write_file(message)
        time.sleep(4)
        g = read_file()
        await message.channel.send(g)
    elif message.content.find("-stop") != -1 and message.content.find("-") == 0:
        write_file(message)
        time.sleep(2)
        await message.channel.send("aa bot stopped!")

client.run('key_goes_here')
