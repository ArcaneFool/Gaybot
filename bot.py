import discord
import random
import asyncio
from discord.ext.commands import Bot
botprefix = ('<','£' , '=' , '"')
TOKEN="NDIwODgyNDc2NzQ4MjQyOTQ0.DZFyFw.81RzMdHOt3XBCLLa5MLZ1n2WTV0"
client = Bot(command_prefix=botprefix)

@client.command(name='8ball',
                pass_context=True
                )
async def ball(context , inp , inp2 = "" , inp3=""):
    if inp == "are" and inp2 == "you" and inp3 == "gay":
        await client.say("NO U" + " , "  + context.message.author.mention)
    else: 
        possible_responses=["FUCK YH" , "ARE YOU GAY" , "YOUR MUM GAY" , "NO RETARD" , "NO KYS" , "OFC FUCKTARD" , "NO YOU" , "IL TOUCHA YOUR SPAGHET" , "ASK YOUR DICKHOLE"]
        await client.say(random.choice(possible_responses) + " , " + context.message.author.mention)
async def ping():
    await client.say(ping_pong)
@client.command(pass_context=True,
                aliases=["purge" , "Purge" , "Prune"] 
                )
async def prune(context,number):
    number=int(number)
    if context.message.author.server_permissions.administrator==True:
        msg=[]
        async for x in client.logs_from(context.message.channel, limit = number):
            msg.append(x)
        await client.delete_messages(msg)
    else:
        await client.say("FUCK OUTTA HERE YOU AIN'T NO MODERATOR" + " , " + context.message.author.mention)
    
@client.command()
async def doc():
    await client.say("STFU DOC")

@client.command()
async def mem():
    await client.say(client.get_all_members())
                     
@client.command()
async def oof():
    await client.say("OOF")

@client.command(pass_context=True)
async def ping(context):
    result=[" is a korean boy loving ass" , " is a lolifurry" , " likes boy semen" , " likes dem wrickled tits" , " likes his brothers rod" , " IS A DOUCHEBAGGETE" ," im jealous of everyone who HASN'T MET YOU" , " IS A DOGGYKNOBBER" , " licks his mothers minge"]
    mentions=["<@265851383692001280>", "<@277129203592331264>","<@241305141624438784>", "<@280443982864056320>","<@149452733215277056>" , "<@174244883970654208>","<@133028189243965440>"]
    await client.say(random.choice(mentions) + random.choice(result))

@client.command(pass_context=True)
async def invite(context):
   await client.say("INVITE MY GAY ASS WITH THIS URL" + " " + "https://discordapp.com/oauth2/authorize?client_id=420882476748242944&scope=bot&permissions=939979967" + " , " + context.message.author.mention)
@client.command(pass_context=True)
async def ban(context, member):
    await client.say(member)
    if context.message.author.server_premissions.administarator==True:
        await client.ban(memeber)
        await client.say(member + " has been banned")

@client.event
async def on_member_join(member):
    await client.send_message("<285441500169502741>" , member.mention + " HAS JOINED THIS CRAP HOLD")
@client.event
async def on_ready():
    print('Logged in as')   
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='WITH YOUR MUM'))


client.run(TOKEN)


