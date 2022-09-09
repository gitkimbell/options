import re
import time
import random
import nextcord
import pandas as pd
from tda import auth
from gtts import gTTS
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from nextcord.utils import get, find
from datetime import timedelta, date, datetime


##########################################
##-TDAmeritrade API to get Options data-##
##########################################
token_path = 'token'
api_key = 'IBMQEU1SRYKCVLBSPKSFQ27PZRGPPGWI@AMER.OAUTHAP'
redirect_uri = 'https://localhost'
try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver

    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)

CALLS = c.Options.ContractType.CALL
PUTS = c.Options.ContractType.PUT
SAK = c.Options.StrikeRange.STRIKES_ABOVE_MARKET
SBK = c.Options.StrikeRange.STRIKES_BELOW_MARKET

##########################
##-Dates for Expiration-##
##########################
start = date.today()
expiry = start + timedelta(days=8)
expiry2 = start + timedelta(days=2)

#########
##-QQQ-##
#########
cQQQ = c.get_option_chain(symbol='QQQ', contract_type=CALLS, strike_count=5, strike_range=SAK)#, to_date=expiry)
cQQQd = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[0]][0]['description']
cQQQd2 = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[1]][0]['description']
cQQQd3 = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[2]][0]['description']
cQQQd4 = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[3]][0]['description']
cQQQd5 = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[4]][0]['description']
cQQQl = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[0]][0]['mark']
cQQQl2 = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[1]][0]['mark']
cQQQl3 = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[2]][0]['mark']
cQQQl4 = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[3]][0]['mark']
cQQQl5 = cQQQ.json()['callExpDateMap'][list(cQQQ.json()['callExpDateMap'].keys())[0]][
    list(cQQQ.json()['callExpDateMap'][
             list(cQQQ.json()['callExpDateMap'].keys())[0]].keys())[4]][0]['mark']

pQQQ = c.get_option_chain(symbol='QQQ', contract_type=PUTS, strike_count=8, strike_range=SAK)#, to_date=expiry)
pQQQd = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[4]][0]['description']
pQQQd2 = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[3]][0]['description']
pQQQd3 = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[2]][0]['description']
pQQQd4 = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[1]][0]['description']
pQQQd5 = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[0]][0]['description']
pQQQl = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[4]][0]['mark']
pQQQl2 = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[3]][0]['mark']
pQQQl3 = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[2]][0]['mark']
pQQQl4 = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[1]][0]['mark']
pQQQl5 = pQQQ.json()['putExpDateMap'][list(pQQQ.json()['putExpDateMap'].keys())[0]][
    list(pQQQ.json()['putExpDateMap'][
             list(pQQQ.json()['putExpDateMap'].keys())[0]].keys())[0]][0]['mark']

#########
##-SPY-##
#########
cSPY = c.get_option_chain(symbol='SPY', contract_type=CALLS, strike_count=5, strike_range=SAK)#, to_date=expiry2)
cSPY_dict = []
o = c.get_option_chain('SPY')
query = o.json()
for contr_type in ['callExpDateMap']:
    contract = dict(query)[contr_type]
    expirations = contract.keys()
    for expiry in list(expirations):
        strikes = contract[expiry].keys()
        for st in list(strikes):
            entry = contract[expiry][st][0]
            cSPY_dict.append(entry)
df_cSPY = pd.DataFrame(cSPY_dict)
new_df = df_cSPY[(df_cSPY['daysToExpiration']<2) & (df_cSPY['inTheMoney']==False)] #& (df_pSPY['strikePrice']>390)]
SPY_calls = new_df.loc[:, ['description', 'last']]
SPY_calls_d = new_df.loc[:, ['description']]
SPY_calls_l = new_df.loc[:, ['last']]

cSPYd = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[0]][0]['description']
cSPYd2 = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[1]][0]['description']
cSPYd3 = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[2]][0]['description']
cSPYd4 = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[3]][0]['description']
cSPYd5 = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[4]][0]['description']
cSPYl = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[0]][0]['mark']
cSPYl2 = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[1]][0]['mark']
cSPYl3 = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[2]][0]['mark']
cSPYl4 = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[3]][0]['mark']
cSPYl5 = cSPY.json()['callExpDateMap'][list(cSPY.json()['callExpDateMap'].keys())[0]][
    list(cSPY.json()['callExpDateMap'][
             list(cSPY.json()['callExpDateMap'].keys())[0]].keys())[4]][0]['mark']

pSPY = c.get_option_chain(symbol='SPY', contract_type=PUTS, strike_count=8, strike_range=SAK)#, to_date=expiry2)
pSPYd = pSPY.json()['putExpDateMap'][list(pSPY.json()['putExpDateMap'].keys())[0]][
    list(pSPY.json()['putExpDateMap'][
             list(pSPY.json()['putExpDateMap'].keys())[0]].keys())[4]][0]['description']
pSPYl = pSPY.json()['putExpDateMap'][list(pSPY.json()['putExpDateMap'].keys())[0]][
    list(pSPY.json()['putExpDateMap'][
             list(pSPY.json()['putExpDateMap'].keys())[0]].keys())[4]][0]['mark']

pSPY_dict = []
o = c.get_option_chain('SPY')
query = o.json()
for contr_type in ['putExpDateMap']:
    contract = dict(query)[contr_type]
    expirations = contract.keys()
    for expiry in list(expirations):
        strikes = contract[expiry].keys()
        for st in list(strikes):
            entry = contract[expiry][st][0]
            pSPY_dict.append(entry)
df_pSPY = pd.DataFrame(pSPY_dict)
new_df = df_pSPY[(df_pSPY['daysToExpiration']<2) & (df_pSPY['inTheMoney']==False)] #& (df_pSPY['strikePrice']>390)]
SPY_puts = new_df.loc[:, ['description', 'last']]
SPY_puts_d = new_df.loc[:, ['description']]
SPY_puts_l = new_df.loc[:, ['last']]

##########
##-AAPL-##
##########
cAAPL = c.get_option_chain(symbol='AAPL', contract_type=CALLS, strike_count=5, strike_range=SAK)#, to_date=expiry)
cAAPLd = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[0]][0]['description']
cAAPLd2 = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[1]][0]['description']
cAAPLd3 = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[2]][0]['description']
cAAPLd4 = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[3]][0]['description']
cAAPLd5 = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[4]][0]['description']
cAAPLl = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[0]][0]['mark']
cAAPLl2 = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[1]][0]['mark']
cAAPLl3 = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[2]][0]['mark']
cAAPLl4 = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[3]][0]['mark']
cAAPLl5 = cAAPL.json()['callExpDateMap'][list(cAAPL.json()['callExpDateMap'].keys())[0]][
    list(cAAPL.json()['callExpDateMap'][
             list(cAAPL.json()['callExpDateMap'].keys())[0]].keys())[4]][0]['mark']

pAAPL = c.get_option_chain(symbol='AAPL', contract_type=PUTS, strike_count=8, strike_range=SAK)#, to_date=expiry)
pAAPLd = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[4]][0]['description']
pAAPLd2 = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[3]][0]['description']
pAAPLd3 = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[2]][0]['description']
pAAPLd4 = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[1]][0]['description']
pAAPLd5 = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[0]][0]['description']
pAAPLl = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[4]][0]['mark']
pAAPLl2 = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[3]][0]['mark']
pAAPLl3 = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[2]][0]['mark']
pAAPLl4 = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[1]][0]['mark']
pAAPLl5 = pAAPL.json()['putExpDateMap'][list(pAAPL.json()['putExpDateMap'].keys())[0]][
    list(pAAPL.json()['putExpDateMap'][
             list(pAAPL.json()['putExpDateMap'].keys())[0]].keys())[0]][0]['mark']


#######################
##-Cortana Bot Token-##
#######################
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='*', intents=intents)
my_secret = '************'

###################
##-Login message-##
###################
@bot.event
async def on_ready():
    voice_channel = bot.get_channel(1000184715149574144)
    backend_channel = bot.get_channel(1002364629135134721)
    print('{0.user}'.format(bot) + ' has logged in')
    await voice_channel.connect()
    await backend_channel.send('$Connected')


#####################
###-Reaction Roles-##
#####################
@bot.command(name='react')
async def react(ctx): #Fix MSFT
    react_message = await ctx.send(
        '**⭐ This is a reaction subscription for signals ⭐**'+'\n'+'\n'
        +'*-React according to the corresponding tickers to receive notifications*'+'\n'
        +'*-React again to remove the corresponding notifications*'+'\n'+'\n'
        +'<:QQQ:1005539784632049765>  QQQ      '+'<:SPY:1003421843887231046>  SPY         '
        +'<:AAPL:1003421828569641021>  AAPL        '+'<:AMZN:1003421830591287356>  AMZN      '+'\n'+'\n'
        +'<:AMD:1003421829634998333>  AMD      '+'<:COIN:1003421831757303888>  COIN      '
        +'<:DKNG:1003421833804132484>  DKNG      '+'<:GOOG:1003421835251155035>  GOOG    '+'\n'+'\n'
        +'<:META:1003421836178096158>  META    '+'<:NFLX:1003421837088264222>  NFLX      '
        +'<:NVDA:1003421838237499483>  NVDA       '+'<:PTON:1003421839126708264>  PTON     '+'\n'+'\n'
        +'<:PYPL:1003421840083005502>  PYPL      '+'<:SHOP:1003421841077051402>  SHOP     '
        +'<:SNAP:1003421841722966068>  SNAP         '+'<:SNOW:1003421843077730314>  SNOW    '+'\n'+'\n'
        +'                       <:SQ:1003421844717703278>  SQ          '
        +'<:TSLA:1003421845543981157>  TSLA'+'\n'+'\n'
        +'   ----------------------------------------------------------')

    await react_message.add_reaction(emoji='<:QQQ:1005539784632049765>') #QQQ
    await react_message.add_reaction(emoji='<:SPY:1003421843887231046>') #SPY
    await react_message.add_reaction(emoji='<:AAPL:1003421828569641021>') #AAPL


@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    msg_id = 1005559699007090698
    guild = find(lambda g: g.id == payload.guild_id, bot.guilds)

# QQQ
    if payload.emoji.id == 1005539784632049765 and message_id == msg_id:
        role = get(guild.roles, name='QQQ')
        if role is not None:
            member = find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
# SPY
    if payload.emoji.id == 1003421843887231046 and message_id == msg_id:
        role = get(guild.roles, name='SPY')
        if role is not None:
            member = find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
# AAPL
    if payload.emoji.id == 1003421828569641021 and message_id == msg_id:
        role = get(guild.roles, name='AAPL')
        if role is not None:
            member = find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)



@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    msg_id = 1005559699007090698
    guild = find(lambda g: g.id == payload.guild_id, bot.guilds)

# QQQ
    if payload.emoji.id == 1005539784632049765 and message_id == msg_id:
        role = get(guild.roles, name='QQQ')
        if role is not None:
            member = nextcord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
# SPY
    if payload.emoji.id == 1003421843887231046 and message_id == msg_id:
        role = get(guild.roles, name='SPY')
        if role is not None:
            member = nextcord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
# AAPL
    if payload.emoji.id == 1003421828569641021 and message_id == msg_id:
        role = get(guild.roles, name='AAPL')
        if role is not None:
            member = find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)


###################
##-c0ncept plays-##
###################
@bot.event
async def on_raw_reaction_add(payload):
    plays = bot.get_channel(1005893581166358558)
    guild = bot.get_guild(payload.guild_id)
    channel = guild.get_thread(payload.channel_id)

    if payload.emoji.id == 1005895849580171315 and payload.member.name == 'c0ncept':
        try:
            msg = await channel.fetch_message(payload.message_id)
            await plays.send(msg.embeds[0].description)
        except:
            pass


##############
##-Triggers-##
##############
@bot.event
async def on_message(msg):
    await bot.process_commands(msg)

    voice = msg.guild.voice_client
    rdm = random.randint(1, 6)

    voice_channel = bot.get_channel(1000184715149574144)
    backend_channel = bot.get_channel(1002364629135134721)
    signal_channel = bot.get_channel(1000520762194669669)

    thread_qqq = bot.get_channel(1005911468472008805)
    thread_spy = bot.get_channel(1003471559035457646)
    thread_aapl = bot.get_channel(1003471637896777769)

    role_qqq = get(msg.guild.roles, name='QQQ')
    role_spy = get(msg.guild.roles, name='SPY')
    role_aapl = get(msg.guild.roles, name='AAPL')


##################################
##-Bot Join/Leave Voice Channel-##
##################################
    if msg.content.startswith('$Connected'):
        output = gTTS(text='Cortana is online. Alerts activated', lang='en', tld='com.au', slow=False)
        output.save("alive.mp3")
        voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("alive.mp3")))
        # print(SPY_puts.tail(10))


    if msg.content.startswith('$join'):
        in_channel = msg.author.voice
        if not in_channel:
            await msg.channel.send('You need to be in a Voice Channel')
        else:
            try:
                if not voice is None:
                    output = gTTS(text='Alerts Already Activated', lang='en', tld='com.au', slow=False)
                    output.save("active.mp3")
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("active.mp3")))
                if voice is None:
                    voice_channel2 = msg.author.voice.channel
                    vc = await voice_channel2.connect()
                    time.sleep(1)
                    output = gTTS(text='Alerts activated', lang='en', tld='com.au', slow=False)
                    output.save("join.mp3")
                    vc.play(FFmpegPCMAudio("join.mp3"))
            except:
                await backend_channel.send('an error occurred...')

    if msg.content.startswith('$leave'):
        try:
            output = gTTS(text='Signing off', lang='en', tld='com.au', slow=False)
            output.save("leave.mp3")
            voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("leave.mp3")))
            time.sleep(2)
            await msg.guild.voice_client.disconnect()
        except:
            await msg.channel.send('Cortana' + " isn't" + ' in a Voice Channel')

##########
##-QQQ-##
##########
    if msg.content.startswith('-QQQ('):
        embed = nextcord.Embed(title='Gathering data for QQQ Puts...adding to QQQ Thread', colour=0x206694)
        embed2 = nextcord.Embed(title='Put Contracts: ',
                                description=
                                '-' + pQQQd + ' @ $' + str(round(pQQQl * 100)) + '\n' +
                                '-' + pQQQd2 + ' @ $' + str(round(pQQQl2 * 100)) + '\n' +
                                '-' + pQQQd3 + ' @ $' + str(round(pQQQl3 * 100)) + '\n' +
                                '-' + pQQQd4 + ' @ $' + str(round(pQQQl4 * 100)) + '\n' +
                                '-' + pQQQd5 + ' @ $' + str(round(pQQQl5 * 100)) + '\n' +
                                f"{role_qqq.mention}",
                                colour=0x206694)
        try:
            await signal_channel.send(embed=embed)
            await thread_qqq.send(embed=embed2)
            if voice is None:
                await voice_channel.connect()
                output = gTTS(text='QQQ Puts', lang='en', tld='com.au', slow=False)
                output.save("QQQp.mp3")
                msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQp.mp3")))
            else:
                output = gTTS(text='QQQ Puts', lang='en', tld='com.au', slow=False)
                output.save("QQQp.mp3")
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQp.mp3")))
        except:
            try:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQp.mp3")))
            except:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQp.mp3")))
    if msg.content.startswith('+QQQ('):
        embed = nextcord.Embed(title='Gathering data for QQQ Calls...adding to QQQ Thread', colour=0x206694)
        embed2 = nextcord.Embed(title='Call Contracts: ',
                                description=
                                '+' + cQQQd + ' @ $' + str(round(cQQQl * 100)) + '\n' +
                                '+' + cQQQd2 + ' @ $' + str(round(cQQQl2 * 100)) + '\n' +
                                '+' + cQQQd3 + ' @ $' + str(round(cQQQl3 * 100)) + '\n' +
                                '+' + cQQQd4 + ' @ $' + str(round(cQQQl4 * 100)) + '\n' +
                                '+' + cQQQd5 + ' @ $' + str(round(cQQQl5 * 100)) + '\n' +
                                f"{role_qqq.mention}",
                                colour=0x206694)
        try:
            await signal_channel.send(embed=embed)
            await thread_qqq.send(embed=embed2)
            if voice is None:
                await voice_channel.connect()
                output = gTTS(text='QQQ Calls', lang='en', tld='com.au', slow=False)
                output.save("QQQc.mp3")
                msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQc.mp3")))
            else:
                output = gTTS(text='QQQ Calls', lang='en', tld='com.au', slow=False)
                output.save("QQQc.mp3")
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQc.mp3")))
        except:
            try:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQc.mp3")))
            except:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQc.mp3")))

#########
##-SPY-##
#########
    if msg.content.startswith('-SPY('):
        embed = nextcord.Embed(title='Gathering data for SPY Puts...adding to SPY Thread', colour=0x206694)
        embed2 = nextcord.Embed(title='Put Contracts: ',
                                description=str(SPY_puts.tail(10)),
                                colour=0x206694)
        try:
            await signal_channel.send(embed=embed)
            await thread_spy.send(embed=embed2)
            if voice is None:
                await voice_channel.connect()
                output = gTTS(text='SPY Puts', lang='en', tld='com.au', slow=False)
                output.save("SPYp.mp3")
                msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPYp.mp3")))
            else:
                output = gTTS(text='SPY Puts', lang='en', tld='com.au', slow=False)
                output.save("SPYp.mp3")
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPYp.mp3")))
        except:
            try:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPYp.mp3")))
            except:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPYp.mp3")))
    if msg.content.startswith('+SPY('):
        embed = nextcord.Embed(title='Gathering data for SPY Calls...adding to SPY Thread', colour=0x206694)
        embed2 = nextcord.Embed(title='Call Contracts: ',
                                description=str(SPY_calls.head(10)),
                                  # '+'+cSPYd + ' @ $' + str(round(cSPYl * 100))+'\n'+
                                  # '+'+cSPYd2 + ' @ $' + str(round(cSPYl2 * 100))+'\n'+
                                  # '+'+cSPYd3 + ' @ $' + str(round(cSPYl3 * 100))+'\n'+
                                  # '+'+cSPYd4 + ' @ $' + str(round(cSPYl4 * 100))+'\n'+
                                  # '+'+cSPYd5 + ' @ $' + str(round(cSPYl5 * 100))+'\n'+
                                  # f"{role_spy.mention}",
                                colour=0x206694)
        try:
            await signal_channel.send(embed=embed)
            await thread_spy.send(embed=embed2)
            # print(new_df.loc[:, ['description', 'last']])
            if voice is None:
                await voice_channel.connect()
                output = gTTS(text='SPY Calls', lang='en', tld='com.au', slow=False)
                output.save("SPYc.mp3")
                msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPYc.mp3")))
            else:
                output = gTTS(text='SPY Calls', lang='en', tld='com.au', slow=False)
                output.save("SPYc.mp3")
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPYc.mp3")))
                # cSPYd0 = cSPYd + ' @ $' + str(round(cSPYl * 100))
                # find = re.findall('\d+', str(cSPYd0))
                # print(find[3]) #- prints the contract cost

        except:
            try:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPYc.mp3")))
            except:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPYc.mp3")))

##########
##-AAPL-##
##########
    if msg.content.startswith('-AAPL('):
        embed = nextcord.Embed(title='Gathering data for AAPL Puts...adding to AAPL Thread', colour=0x206694)
        embed2 = nextcord.Embed(title='Put Contracts: ',
                                description=
                                '-' + pAAPLd + ' @ $' + str(round(pAAPLl * 100)) + '\n' +
                                '-' + pAAPLd2 + ' @ $' + str(round(pAAPLl2 * 100)) + '\n' +
                                '-' + pAAPLd3 + ' @ $' + str(round(pAAPLl3 * 100)) + '\n' +
                                '-' + pAAPLd4 + ' @ $' + str(round(pAAPLl4 * 100)) + '\n' +
                                '-' + pAAPLd5 + ' @ $' + str(round(pAAPLl5 * 100)) + '\n' +
                                f"{role_aapl.mention}",
                                colour=0x206694)
        try:
            await signal_channel.send(embed=embed)
            await thread_aapl.send(embed=embed2)
            if voice is None:
                await voice_channel.connect()
                output = gTTS(text='Apple Puts', lang='en', tld='com.au', slow=False)
                output.save("AAPLp.mp3")
                msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPLp.mp3")))
            else:
                output = gTTS(text='Apple Puts', lang='en', tld='com.au', slow=False)
                output.save("AAPLp.mp3")
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPLp.mp3")))
        except:
            try:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPLp.mp3")))
            except:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPLp.mp3")))
    if msg.content.startswith('+AAPL('):
        embed = nextcord.Embed(title='Gathering data for AAPL Calls...adding to AAPL Thread', colour=0x206694)
        embed2 = nextcord.Embed(title='Call Contracts: ',
                                description=
                                '+' + cAAPLd + ' @ $' + str(round(cAAPLl * 100)) + '\n' +
                                '+' + cAAPLd2 + ' @ $' + str(round(cAAPLl2 * 100)) + '\n' +
                                '+' + cAAPLd3 + ' @ $' + str(round(cAAPLl3 * 100)) + '\n' +
                                '+' + cAAPLd4 + ' @ $' + str(round(cAAPLl4 * 100)) + '\n' +
                                '+' + cAAPLd5 + ' @ $' + str(round(cAAPLl5 * 100)) + '\n' +
                                f"{role_aapl.mention}",
                                colour=0x206694)
        try:
            await signal_channel.send(embed=embed)
            await thread_aapl.send(embed=embed2)
            if voice is None:
                await voice_channel.connect()
                output = gTTS(text='Apple Calls', lang='en', tld='com.au', slow=False)
                output.save("AAPLc.mp3")
                msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPLc.mp3")))
            else:
                output = gTTS(text='Apple Calls', lang='en', tld='com.au', slow=False)
                output.save("AAPLc.mp3")
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPLc.mp3")))
        except:
            try:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPLc.mp3")))
            except:
                time.sleep(rdm)
                voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPLc.mp3")))


#################
##-Exit Signals-##
#################
    ##-QQQ-##
    if msg.content.startswith('QQQ Exit'):
        ctx = await thread_qqq.fetch_message(thread_qqq.last_message_id)
        QQQ_exit = ctx.embeds[0].description
        find = re.findall('\d+', str(QQQ_exit))
        if ctx.embeds[0].title == 'Put Contracts:':
            embedp = nextcord.Embed(title='Exit Signal',
                                   description='Then:$' + str(find[3]) + ' ->  Now:$' + str(round(pQQQl * 100)) + '\n' +
                                               'Then:$' + str(find[7]) + ' ->  Now:$' + str(round(pQQQl2 * 100)) + '\n' +
                                               'Then:$' + str(find[11]) + ' ->  Now:$' + str(round(pQQQl3 * 100)) + '\n' +
                                               'Then:$' + str(find[15]) + ' ->  Now:$' + str(round(pQQQl4 * 100)) + '\n' +
                                               'Then:$' + str(find[19]) + ' ->  Now:$' + str(round(pQQQl5 * 100)),
                                   colour=0x9b59b6)
            await thread_qqq.send(embed=embedp)
            try:
                if voice is None:
                    await voice_channel.connect()
                    output = gTTS(text='QQQ Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("QQQ exit.mp3")
                    msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQ exit.mp3")))
                else:
                    output = gTTS(text='QQQ Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("QQQ exit.mp3")
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQ exit.mp3")))
            except:
                try:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQ exit.mp3")))
                except:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQ exit.mp3")))
        elif ctx.embeds[0].title == 'Call Contracts:':
            embedc = nextcord.Embed(title='Exit Signal',
                                   description='Then:$' + str(find[3]) + ' ->  Now:$' + str(round(cQQQl * 100)) + '\n' +
                                               'Then:$' + str(find[7]) + ' ->  Now:$' + str(round(cQQQl2 * 100)) + '\n' +
                                               'Then:$' + str(find[11]) + ' ->  Now:$' + str(round(cQQQl3 * 100)) + '\n' +
                                               'Then:$' + str(find[15]) + ' ->  Now:$' + str(round(cQQQl4 * 100)) + '\n' +
                                               'Then:$' + str(find[19]) + ' ->  Now:$' + str(round(cQQQl5 * 100)),
                                   colour=0x9b59b6)
            await thread_qqq.send(embed=embedc)
            try:
                if voice is None:
                    await voice_channel.connect()
                    output = gTTS(text='QQQ, Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("QQQ exit.mp3")
                    msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQ exit.mp3")))
                else:
                    output = gTTS(text='QQQ, Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("QQQ exit.mp3")
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQ exit.mp3")))
            except:
                try:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQ exit.mp3")))
                except:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("QQQ exit.mp3")))
        else:
            await msg.delete()

    ##-SPY-##
    if msg.content.startswith('SPY Exit'):
        ctx = await thread_spy.fetch_message(thread_spy.last_message_id)
        SPY_exit = ctx.embeds[0].description
        find = re.findall('\d+', str(SPY_exit))
        if ctx.embeds[0].title == 'Put Contracts:':
            embedp = nextcord.Embed(title='Exit Signal',
                                   description='Then:$' + str(find[3]) + ' ->  Now:$' + str(round(pSPYl * 100)),
                                   colour=0x9b59b6)
            await thread_spy.send(embed=embedp)
            try:
                if voice is None:
                    await voice_channel.connect()
                    output = gTTS(text='SPY, Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("SPY exit.mp3")
                    msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPY exit.mp3")))
                else:
                    output = gTTS(text='SPY, Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("SPY exit.mp3")
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPY exit.mp3")))
            except:
                try:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPY exit.mp3")))
                except:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPY exit.mp3")))
        elif ctx.embeds[0].title == 'Call Contracts:':
            embedc = nextcord.Embed(title='Exit Signal',
                                   description='Then:$' + str(find[3]) + ' ->  Now:$' + str(round(cSPYl * 100)) + '\n' +
                                               'Then:$' + str(find[7]) + ' ->  Now:$' + str(round(cSPYl2 * 100)) + '\n' +
                                               'Then:$' + str(find[11]) + ' ->  Now:$' + str(round(cSPYl3 * 100)) + '\n' +
                                               'Then:$' + str(find[15]) + ' ->  Now:$' + str(round(cSPYl4 * 100)) + '\n' +
                                               'Then:$' + str(find[19]) + ' ->  Now:$' + str(round(cSPYl5 * 100)),
                                   colour=0x9b59b6)
            await thread_spy.send(embed=embedc)
            try:
                if voice is None:
                    await voice_channel.connect()
                    output = gTTS(text='SPY Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("SPY exit.mp3")
                    msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPY exit.mp3")))
                else:
                    output = gTTS(text='SPY Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("SPY exit.mp3")
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPY exit.mp3")))
            except:
                try:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPY exit.mp3")))
                except:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("SPY exit.mp3")))
        else:
            await msg.delete()

    ##-AAPL-##
    if msg.content.startswith('AAPL Exit'):
        ctx = await thread_aapl.fetch_message(thread_aapl.last_message_id)
        AAPL_exit = ctx.embeds[0].description
        find = re.findall('\d+', str(AAPL_exit))
        if ctx.embeds[0].title == 'Put Contracts:':
            embedp = nextcord.Embed(title='Exit Signal',
                                   description='Then:$' + str(find[3]) + ' ->  Now:$' + str(round(pAAPLl * 100)) + '\n' +
                                               'Then:$' + str(find[7]) + ' ->  Now:$' + str(round(pAAPLl2 * 100)) + '\n' +
                                               'Then:$' + str(find[11]) + ' ->  Now:$' + str(round(pAAPLl3 * 100)) + '\n' +
                                               'Then:$' + str(find[15]) + ' ->  Now:$' + str(round(pAAPLl4 * 100)) + '\n' +
                                               'Then:$' + str(find[19]) + ' ->  Now:$' + str(round(pAAPLl5 * 100)),
                                   colour=0x9b59b6)
            await thread_aapl.send(embed=embedp)
            try:
                if voice is None:
                    await voice_channel.connect()
                    output = gTTS(text='Apple Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("AAPL exit.mp3")
                    msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPL exit.mp3")))
                else:
                    output = gTTS(text='Apple Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("AAPL exit.mp3")
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPL exit.mp3")))
            except:
                try:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPL exit.mp3")))
                except:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPL exit.mp3")))
        elif ctx.embeds[0].title == 'Call Contracts:':
            embedc = nextcord.Embed(title='Exit Signal',
                                   description='Then:$' + str(find[3]) + ' ->  Now:$' + str(round(cAAPLl * 100)) + '\n' +
                                               'Then:$' + str(find[7]) + ' ->  Now:$' + str(round(cAAPLl2 * 100)) + '\n' +
                                               'Then:$' + str(find[11]) + ' ->  Now:$' + str(round(cAAPLl3 * 100)) + '\n' +
                                               'Then:$' + str(find[15]) + ' ->  Now:$' + str(round(cAAPLl4 * 100)) + '\n' +
                                               'Then:$' + str(find[19]) + ' ->  Now:$' + str(round(cAAPLl5 * 100)),
                                   colour=0x9b59b6)
            await thread_aapl.send(embed=embedc)
            try:
                if voice is None:
                    await voice_channel.connect()
                    output = gTTS(text='Apple Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("AAPL exit.mp3")
                    msg.guild.voice_client.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPL exit.mp3")))
                else:
                    output = gTTS(text='Apple Exit Signal', lang='en', tld='com.au', slow=False)
                    output.save("AAPL exit.mp3")
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPL exit.mp3")))
            except:
                try:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPL exit.mp3")))
                except:
                    time.sleep(rdm)
                    voice.play(nextcord.PCMVolumeTransformer(FFmpegPCMAudio("AAPL exit.mp3")))
        else:
            await msg.delete()


#########
##-Run-##
##########
bot.run(my_secret)
