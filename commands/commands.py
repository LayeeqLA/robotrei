
from twitchbot import Command, DummyCommand, SubCommand, CustomCommand
from twitchbot import auto_register_mod
import json
import datetime
import re

import random
from urllib.request import urlopen, HTTPError
import json
import asyncio

""" todo list:
database stuff w the server
database points for goodbot/badbot
add fun apis
"""

# data = json.load(open('customcommands.json', 'r'))
# print(data)


# make sure to update both lists

@Command('vampire', aliases=['vamp'])
async def cmd_function(msg, *args):
    await msg.reply(f' ok so {msg.mention} u are {vampire_options(msg)}')

def vampire_options(msg):
    vampire = ['Jasper from Twilight who was a confederate soldier. but hot so yanno.. redeemable. very moody',
               'Rosalie from Twilight.. hottest bad bitch of em all. congrats',
               'lol Bella Swan. u dumbass. but like shes okay later',
               'Nosferatu... the only vampire i DONT want to sleep with',
               'Damon Salvatore and im in love with you. deeply... lets kiss? haha jk... unless?,,, ;)',
               'Stefan Salvatore, very cool.. can i pls have Damons number???',
               'Dracula.. classic. vampire daddy. nothing else to say. vanilla ice cream of vampires',
               'Eric Northman... is this true love?? sir pls bite me... i am yours',
               'Bill from true blood. not hot. no clue how sookie was into him, he srs looks dead. ugh. team Eric',
               'Pamela from true blood. banging latex lady. be my sugarmommy pls',
               'Tanya from Twilight, u fucking RAT... snitches get stitches... u deserved ur fate',
               'not even a vampire, u are a filthy werewolf. gross. moonboy.',
               'Godric from True Blood, you have seen it all, unmoved mover. peaceful being'
               ]
    return random.choice(vampire)

# vampire tagged
@Command('whichvampire', aliases=['wv'])
async def cmd_function(msg, *args):
    await msg.reply(f' ok so @{msg.mentions[0]} u are {vampire_options(msg)}')

def vampire_options(msg):
    vampire = ['Jasper from Twilight who was a confederate soldier. but hot so yanno.. redeemable. very moody',
               'Rosalie from Twilight.. hottest bad bitch of em all. congrats',
               'lol Bella Swan. u dumbass. but like shes okay later',
               'Nosferatu... the only vampire i DONT want to sleep with',
               'Damon Salvatore and im in love with you. deeply... lets kiss? haha jk... unless?,,, ;)',
               'Stefan Salvatore, very cool.. can i pls have Damons number???',
               'Dracula.. classic. vampire daddy. nothing else to say. vanilla ice cream of vampires',
               'Eric Northman... is this true love?? sir pls bite me... i am yours',
               'Bill from true blood. not hot. no clue how sookie was into him, he srs looks dead. ugh. team Eric',
               'Pamela from true blood. banging latex lady. be my sugarmommy pls',
               'Tanya from Twilight, u fucking RAT... snitches get stitches... u deserved ur fate',
               'not even a vampire, u are a filthy werewolf. gross. moonboy.',
               'Godric from True Blood, you have seen it all, unmoved mover. peaceful being'

               ]
    return random.choice(vampire)

# fortune
@Command('fortune')
async def cmd_function(msg, *args):
    await msg.reply(fortune_options(msg))

def fortune_options(msg):
    fortunes = ['Be on the alert to recognize your prime at whatever time of your life it may occur.',
                'Your road to glory will be rocky, but fulfilling.',
                'Courage is not simply one of the virtues, but the form of every virtue at the testing point.',
                'Patience is your ally at the moment. Don’t worry!',
                'Nothing is impossible to a willing heart.,'
                'Don’t worry about money. The best things in life are free.',
                'Don’t pursue happiness – create it.',
                'Courage is not the absence of fear; it is the conquest of it.',
                'Nothing is so much to be feared as fear.',
                'All things are difficult before they are easy.',
                'The real kindness comes from within you.',
                'A ship in harbor is safe, but that’s not why ships are built.',
                'You don’t need strength to let go of something. What you really need is understanding.',
                'If you want the rainbow, you have to tolerate the rain.',
                'Fear is interest paid on a debt you may not owe.',
                'The usefulness of a cup is in its emptiness.',
                'He who throws mud loses ground.']
    return random.choice(fortunes)

# change each stream
@Command('text', aliases=['reading'])
async def cmd_function(msg, *args):
    await msg.reply('today im just messing around w the bot and vibing')
# maybe remove i cant be bothered to change em manually
@Command('song', aliases=['music'])
async def cmd_function(msg, *args):
    await msg.reply('currently playing this: https://www.youtube.com/watch?v=PofuCgkPMqA')

@Command('today')
async def cmd_function(msg, *args):
    await msg.reply('today im just messing around w the bot and vibing')

# changing variable
@Command('bitcoin', aliases=['bit', 'b'])
async def cmd_function(msg, *args):
    btc_price_usd = json.loads(urlopen('https://api.bybit.com/v2/public/tickers?btcusd').read())['result'][0]['last_price']
   # btc_price_euro = json.loads(urlopen('https://api.bybit.com/v2/public/tickers?btcusd').read())['result'][0]['last_price']
    await msg.reply(f'the current price of bitcoin is: ${btc_price_usd}')
  #  await asyncio.sleep(5)
#    await msg.reply(f'while we are talking about bitcoin... u can donate in btc actually, 13AxggqBeq8ajcpCHbymfZRyyqUKzk39qi .. im sure a smart handsome bitcoin lover like u has some to spare... did i say u are very handsome {msg.mention}?? the most handsome... <3')

@Command('ethereum', aliases=['eth'])
async def cmd_function(msg, *args):
    eth_price_usd = json.loads(urlopen('https://api.bybit.com/v2/public/tickers?ethusd').read())['result'][1]['last_price']
    await msg.reply(f'the current price of ethereum is: ${eth_price_usd}')

# added weather stuff kelvins--> metric WEATHER, FUCKING TIMEZONES
@Command('weather', aliases=['cold'])
async def cmd_function(msg, *args):
    if not args:
        weather = json.loads(urlopen('https://api.openweathermap.org/data/2.5/weather?q=Prague&appid=cf90323172994c9ae286c8786ae08390&units=metric').read())
        temp = weather['main']['temp']
        description = weather['weather'][0]['description']
        feels_like = weather['main']['feels_like']
        dumb_units = round(((temp * 1.8) + 32),2)
        sunset_raw = weather['sys']['sunset']
        sunset = datetime.datetime.fromtimestamp(sunset_raw).strftime('%H:%M')
        sunrise_raw = weather['sys']['sunrise']
        sunrise = datetime.datetime.fromtimestamp(sunrise_raw).strftime('%H:%M')

        await msg.reply(f'for me (prague) the temperature is {temp} but it feels like {feels_like} degrees celsius or {dumb_units} in fahrenheit and it is {description}, sun will set at {sunset} but it will rise again at {sunrise}')
    else:

        display_name = ' '.join(args).title()
        cityname = '+'.join(args)
        if(''.join(args).isalpha()):
            request_url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=cf90323172994c9ae286c8786ae08390&units=metric'

            try:
                response = urlopen(request_url)
                data = json.loads(response.read())
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                feels_like = data['main']['feels_like']
                dumb_units = round(((temp * 1.8) + 32),2)
                timezone = data['timezone']
                #sunset
                sunset_raw = data['sys']['sunset']
                sunset_convert = sunset_raw + timezone
                sunset = datetime.datetime.fromtimestamp(sunset_convert).strftime('%H:%M')
                #sunrise
                sunrise_raw = data['sys']['sunrise']
                sunrise_convert = sunrise_raw + timezone
                sunrise = datetime.datetime.fromtimestamp(sunrise_convert).strftime('%H:%M')





                await msg.reply(f'The temperature in {display_name} is {temp} but it feels like {feels_like} celsius but its {dumb_units} in fahrenheit and it is {description}, sun will set at {sunset} but it will rise again at {sunrise} in local time')
            except HTTPError:
                await msg.reply(f'It seems you have not provided a useful city name')

# added weather stuff kelvins--> metric
#RAIN
# new api a54b1b5aeed2e1b8d98fea848734d56d for rain

@Command('rain')
async def cmd_function(msg, *args):
    if not args:
        rain = json.loads(urlopen('https://api.openweathermap.org/data/2.5/forecast?q=prague&appid=a54b1b5aeed2e1b8d98fea848734d56d&units=metric').read())
        current_humidity = rain['list'][0]['main']['humidity']
        tomorrow_humidity = rain['list'][6]['main']['humidity']

        await msg.reply(f'the humidity in Prague is {current_humidity}, but tomorrow noon it will be {tomorrow_humidity}')
    else:
        display_name = ' '.join(args).title()
        cityname = '+'.join(args)
        request_url = f'https://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid=a54b1b5aeed2e1b8d98fea848734d56d&units=metric'

        try:
            response = urlopen(request_url)
            data = json.loads(response.read())
            current_humidity = data['list'][0]['main']['humidity']
            tomorrow_humidity = data['list'][6]['main']['humidity']
            await msg.reply(f'The current humidity in {display_name} is {current_humidity}, but tomorrow noon it will be {tomorrow_humidity}')

        except HTTPError:
            await msg.reply(f'It seems you have not provided a useful city name')

# ONE call for prague - cannot do for other cities
#@Command('onecall')
async def cmd_function(msg, *args):

    onecall = json.loads(urlopen('https://api.openweathermap.org/data/2.5/onecall?lat=50.088039&lon=14.42076&exclude=minutely,hourly&appid=75717376a32a615f8801633ff195a5d5&units=metric').read())






@Command('joke')
async def cmd_function(msg, *args):
    joke = json.loads(urlopen('https://official-joke-api.appspot.com/random_joke').read())
    setup = joke['setup']
    punchline = joke['punchline']
    await msg.reply(setup)
    await asyncio.sleep(2)
    await msg.reply(punchline)


@Command('tea')
async def cmd_function(msg, *args):
    await msg.reply('vanilla rooibos tea!')

@Command('amazon', aliases=['bezos', 'jeff'])
async def cmd_function(msg, *args):
    await msg.reply('amazon is a terrible company')


@Command('elon', aliases=['musk', 'muskrat'])
async def cmd_function(msg, *args):
    await msg.reply('elon musk should be made into a leather couch and left by the trashcan')

@Command('theend')
async def cmd_function(msg, *args):
    await msg.reply('thank u all for watching!!! pls follow me!!! also come to my discord and see u tomorrow!!! <3 https://discord.com/invite/YuXqUR6')

@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply('weekdays: 9-ish till evening I study and have lectures, then python and/or eve online in the evenings till cca 10pm. weekends: surprise but basically a more chill study/python/eve time')

# links
@Command('github', aliases=['gb', 'git'])
async def cmd_function(msg, *args):
    await msg.reply('come bully me at https://github.com/lisareina/robotrei')

@Command('cleancode', aliases=['cc', 'cleancoderules', 'coderules'])
async def cmd_function(msg, *args):
    await msg.reply(' here are rules im gonna try and follow https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29')

@Command('invite')
async def cmd_function(msg, *args):
    await msg.reply('in game channel = LisaRei, ign = xymfa, and join w my link https://www.eveonline.com/signup?invc=046f680f-889d-4949-9a19-a383f98045e2 for one MILLION free skill points')

@Command('eve', aliases=['e', 'eveonline'])
async def cmd_function(msg, *args):
    await msg.reply('Eve Online is a space-based, persistent world massively multiplayer online role-playing game developed and published by CCP Games. Players of Eve Online can participate in a number of in-game professions and activities, including mining, piracy, manufacturing, trading, exploration, and combat.')

@Command('discord', aliases=['d'])
async def cmd_function(msg, *args):
    await msg.reply('come hang out on discord! https://discord.com/invite/YuXqUR6 or use !dw to whisper the link to urself')

@Command('twitter', aliases=['t', 'bird'])
async def cmd_function(msg, *args):
    await msg.reply('follow me on twitter https://twitter.com/lisareistudy')

@Command('instagram', aliases=['i', 'insta', 'ig'])
async def cmd_function(msg, *args):
    await msg.reply('my insta is: https://www.instagram.com/thelisarei/')

@Command('donate', aliases=['paypal', 'tip', 'money'])
async def cmd_function(msg, *args):
    await msg.reply('please sir may i have some money *shakes cup* https://streamlabs.com/lisarei/tip')

# basics

@Command('panic')
async def cmd_function(msg, *args):
    await msg.reply('AAAAAAAAAAAAAAAAAAAAAAA')

@Command('indent', aliases=['indentation'])
async def cmd_function(msg, *args):
    await msg.reply('pssst @lisarei doesnt know how to indent pass it on')

@Command('mom')
async def cmd_function(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply('sorry guys this is my mom calling so i have to pick up so ill mute myself. shouldnt take toooo long.')


@Command('bye')
async def cmd_function(msg, *args):
    await msg.reply(f'see u {msg.mention}, thnx for stopping by')

@Command('brb')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} will be back soon!!')

@Command('isk')
async def cmd_function(msg, *args):
    await msg.reply('send ISK to "xymfa" and i will not double it')


@Command('time', aliases=['timezone'])
async def cmd_function(msg, *args):
    await msg.reply(
            f'time is  a social construct but here u go, it is: {(datetime.datetime.now()).strftime("%H:%M, %A %d/%m")}... gmt+1 babyy')

# practical
@Command('sound', aliases=['loud', 'quiet'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lisarei something is wrong w the sound')

@Command('muted', aliases=['m', 'mic'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lisarei u are muted')

@Command('posture')
async def cmd_function(msg, *args):
    await msg.reply(f'u gotta use channel points to make me not sit like a pretzel... but just this once ill sit up straight anyway')

@Command('hydrate')
async def cmd_function(msg, *args):
    await msg.reply(f'u gotta use channel points to make me drinkkk... but just this once ill take a sip since its u {msg.mention}')

@Command('situpstraightsis')
async def cmd_function(msg, *args):
    allowed_users = {'i_thanvanth'}
    if msg.author in allowed_users:
        await msg.reply('T says sit up @lisarei')

@Command('lurk')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} is gonna be lurking <3')

@Command('hug')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u have been hugged @{msg.mentions[0]}')

@Command('thankyou', aliases=['thnx', 'ty'])
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'shoutout to @{msg.mentions[0]} thank u!!! <3 i love u')

@Command('streamershoutout', aliases=['streamer', 'ss'])
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'shoutout to @{msg.mentions[0]} who is also a streamer!! go follow them')

# about
@Command('age')
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a dog shed be dead... mid 20s')

@Command('height', aliases=['tall'])
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a tree shed be 6ft, but as a human shes 185cm or so')

@Command('where', aliases=['country','origin', 'from'])
async def cmd_function(msg, *args):
    await msg.reply('lisa is from the czech republic, its a small country next to germany')

@Command('python')
async def cmd_function(msg, *args):
    await msg.reply('i am using pycharm pro, have been learning since october 25th 2020, rn im working on this bot')

@Command('equipment', aliases=['specs'])
async def cmd_function(msg, *args):
    await msg.reply('macbook pro 2015, keyboard: filco minila air mx brown switches')

@Command('keyboard')
async def cmd_function(msg, *args):
    await msg.reply('keyboard: filco minila air mx brown switches')

@Command('languages')
async def cmd_function(msg, *args):
    await msg.reply('i speak czech, english, russian, spanish, and some french. also did 2 years of latin and a bit of trying to learn lojban and esperanto')

@Command('games', aliases=['game'])
async def cmd_function(msg, *args):
    await msg.reply('stardew valley, eve online and some minecraft... if u wanna play w me go to my discord')

@Command('stardew')
async def cmd_function(msg, *args):
    await msg.reply('Stardew Valley is an open-ended country-life RPG! Youve inherited your grandfathers old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life.')

@Command('degree', aliases=['uni','university'])
async def cmd_function(msg, *args):
    await msg.reply('im doing an MScEng in agricultural economics and international development')

# bot feedbackdatabase
@Command('goodbot', aliases=['goodrobot', 'good'])
async def cmd_function(msg, *args):
    await msg.reply(f'awww thank u {msg.mention} i am glad u like me')

@Command('badbot', aliases=['badrobot', 'bad'])
async def cmd_function(msg, *args):
    await msg.reply(f'wow..... {msg.mention} i have feelings too you know... u try being a bot.... its not so easy')
    # it would add a point or something????? into the database

@Command('bot')
async def cmd_function(msg, *args):
    await msg.reply('i am not a bot i am a robot.... use !robot pls. but fine fine... i am a twitchbot, made in python, to see my insides use !github')

@Command('sorry')
async def cmd_function(msg, *args):
    await msg.reply(f'hmmm i dont know if i forgive you... robots never forgive or forget')

@Command('die')
async def cmd_function(msg, *args):
    await msg.reply('oh wow... u big meanie.... speechlesssss')

@Command('daddy')
async def cmd_function(msg, *args):
    await msg.reply(f'my daddy is https://github.com/sharkbound/PythonTwitchBotFramework but who is your daddy??? {msg.mention}')

@Command('say')
async def cmd_say(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(' '.join(args))