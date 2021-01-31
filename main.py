# Author: Pranav Raja
#imports
import math
import random
from datetime import date
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from newsapi import NewsApiClient
import requests
import json
from emoji import EMOJI_ALIAS_UNICODE as EMOJIS
import pandas as pd
import importlib

#variables
bot = commands.Bot(command_prefix='$')
newsapi = NewsApiClient(api_key='a73e70169fa449dba6e22aa3c5befd88')
pastdate = "2020-12-20"
todayDate = date.today()
FormatDate = todayDate.strftime("%Y-%m-%d")

#commands + log on
class BotCommands:
    @bot.command()
    async def eightball(ctx):
        eightballnumbers = ["You will be a millionare",
                            "You will become an ani", "You will be broke", "You will be a Utuber", "You will be my mom",
                            "You're a wizard HARRY", "You'll be dumber than a dummy",
                            "YOu wont get into MIT!!!!!!!!!!", "You will be in crippling depression forever",
                            "YOu will be a proffesional poker player", "You will have a wife",
                            "You will be the president", "You will breathe air",
                            "You will become healthy because of Mc.Donalds", "You will become a human",
                            "You will be salty sugar"]
        answerforeightball = random.choice(eightballnumbers)
        await ctx.send(answerforeightball)
        print('I found the command')

    @bot.command()
    async def whosalty(ctx):
        peoplewhosalty = ['Pranav', 'Ani', 'Aryan', 'Erik',
                          'Teja', 'Karthik', 'Viraat', 'Apache Pig', 'Maanas', 'Lucas', 'Patrick', 'Mr.Bean', 'Aliens',
                          'PhantomDragon', 'Importly', 'Boredalways', 'sugar', 'Ur Mom',
                          'Candy', 'Boredombot', 'rust', 'python', 'YEEEEEEEEEEEET', 'no u', 'ur dad', 'bullies',
                          'Tamil', 'INDIA', 'Me', 'Cake', 'Quadratic Formula', 'Fifeild', 'Rags', 'Viraat Skills',
                          'HomeworkBot cuz he doesn\'t procrastinate',
                          'Mr.krabs', 'Mrs.Couilibaly', 'Poptarts', 'Stephen Curry']
        person = random.choice(peoplewhosalty)
        if person == 'Me':
            await ctx.send("I am very salty")
        elif person == 'Aliens':
            await ctx.send(person + ' are very salty')
        elif person == 'Poptarts':
            await ctx.send(person + ' are very salty')
        elif person == 'bullies':
            await ctx.send(person + ' are very salty')
        else:
            await ctx.send(person + ' is very salty')

    @bot.command()
    async def salt(ctx):
        await ctx.send(
            'Salt is the rating of this server, less than 60 means that people are nice, if more than 60 server is too salty and I destroy the rating to give you guys a second chance')

    @bot.command()
    async def Hello(ctx):
        await ctx.send('Hello Mommy')

    @bot.command()
    async def anisalt(ctx):
        await ctx.send(
            'OVER 90000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

    @bot.command()
    async def test(ctx, arg):
        await ctx.send(arg)

    @bot.group()
    async def math(ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Please enter a command after $math, so far I have $isodd,')

    @math.command()
    async def isodd(ctx, arg):
        if not arg:
            await ctx.send('Please enter a number!')
        arg = int(arg)
        if arg % 2 == 0:
            await ctx.send(str(arg) + ' is even')
            arg = int(arg)
            await ctx.send(arg / 2)
        else:
            await ctx.send(str(arg) + ' is odd')

    @math.command()
    async def squart(ctx, arg):
        arg = float(arg)
        arg = arg ** 2
        arg = str(arg)
        if len(arg) > 2000:
            await ctx.send('I can square it but discord be dumb so sorry but can\'t ')
        else:
            await ctx.send(arg)

    @math.command()
    async def sqrt(ctx, arg):
        arg = float(arg)
        arg = math.sqrt(arg)
        await ctx.send(arg)

    @math.command()
    async def add(ctx, arg1, arg2):
        arg1 = float(arg1)
        arg2 = float(arg2)
        await ctx.send(arg1 + arg2)

    @math.command()
    async def min(ctx, arg1, arg2):
        arg1 = float(arg1)
        arg2 = float(arg2)
        await ctx.send(arg1 - arg2)

    @math.command()
    async def geometryfacts(ctx, arg1, *args):
        await ctx.send('{} : {} '.format(arg1, ' '.join(args)))

    @bot.group()
    async def geofacts(ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Please enter a command after $geofacts, refer to $help geofacts if needed')

    @geofacts.command()
    async def addfacts(ctx, args):
        test1, test2 = args.split(",")
        await ctx.send('Added Word - {} : Added Definition - {} '.format(test1, test2))
        geodiction = {}
        print("Test 1 ", test1)
        print("Test 2 ", test2)
        for i in [test1]:
            geodiction[i] = eval(test2)
            await ctx.send(geodiction)

    @math.command()
    async def div(ctx, arg1, arg2):
        arg1 = float(arg1)
        arg2 = float(arg2)
        if arg1 == 1 and arg2 == 0:
            await ctx.send('1 / 0 is undefined my guy')
        else:
            await ctx.send(arg1 / arg2)

    @math.command()
    async def multi(ctx, arg1, arg2):
        arg1 = float(arg1)
        arg2 = float(arg2)
        await ctx.send(arg1 * arg2)

    @bot.command()
    async def ping(ctx, arg):
        await ctx.send('@' + str(arg))
        await ctx.send('HAHA spam go brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')

    @math.command()
    async def helpme(ctx):
        await ctx.send('https://www.youtube.com/')
        await ctx.send('it solves all your problems')

    @math.command()
    async def multiple(ctx, arg1, arg2):
        arg1 = int(arg1)
        arg2 = int(arg2)
        arg3 = arg1 % arg2
        arg4 = arg1 / arg2
        if arg3 == 0:
            await ctx.send(str(arg2) + ' is a multiple of ' + str(arg1))
            await ctx.send(str(arg4))
        else:
            await ctx.send('not a multiple')

    @math.command()
    async def triples(ctx, arg1, arg2, arg3):
        arg1, arg2, arg3 = float(arg1), float(arg2), float(arg3)
        arg1squared, arg2squared, arg3squared = arg1 ** 2, arg2 ** 2, arg3 ** 2
        sumofsquaredargs = arg1squared + arg2squared
        if sumofsquaredargs == arg3squared:
            await ctx.send(str(sumofsquaredargs) + ' = ' + str(arg3squared))
            await ctx.send('yes its a triple that math looks correct')

        else:
            await ctx.send(str(sumofsquaredargs) + ' not = to ' + str(arg3squared))
            await ctx.send('math look bad')

    @math.command()
    async def helptriples(ctx, arg1, arg2, arg3):
        if arg1 == '?':
            arg2, arg3 = float(arg2), float(arg3)
            if arg2 < arg3:
                arg2s, arg3s = arg2 ** 2, arg3 ** 2
                arg2ss = arg3s - arg2s
                arg2sss = math.sqrt(arg2ss)
                await ctx.send(arg2sss)
            else:
                await ctx.send('your value is greater than the third value')

        elif arg2 == '?':
            arg1, arg3 = float(arg1), float(arg3)
            if arg1 < arg3:
                arg1s, arg3s = arg1 ** 2, arg3 ** 2
                arg1ss = arg3s - arg1s
                arg1sss = math.sqrt(arg1ss)
                await ctx.send(arg1sss)
            else:
                await ctx.send('your value is greater than the third value')

        elif arg3 == '?':
            arg1, arg2 = float(arg1), float(arg2)
            arg1, arg2 = arg1 ** 2, arg2 ** 2
            arg1plus2 = arg1 + arg2
            arg1plus2 = math.sqrt(arg1plus2)
            await ctx.send(arg1plus2)

        else:
            await ctx.send('do you have a ? and your first 2 numbers are less than the third?')

    @math.command()
    async def powerto(ctx, arg1, arg2):
        arg1, arg2 = int(arg1), int(arg2)
        if arg2 < 500:
            squared = arg1 ** arg2
            await ctx.send(squared)
        else:
            await ctx.send('BOY TO LONGGGGGGGGGGGGGGGG')

    @bot.command()
    async def LearnCoding(ctx):
        peoplewhoneedtolearn = ['Teja', 'Teja', 'Teja', 'Teja', 'Teja', 'Teja', 'Teja', 'Teja', 'Teja', 'Teja', 'Teja',
                                'Teja', 'Teja', 'Teja', 'Erik', 'Pranav', 'Viraat', 'Maanas', 'Ani']
        person = random.choice(peoplewhoneedtolearn)
        await ctx.send(person + ' learn coding now')

    @bot.command()
    async def news(ctx, *, args):
        pageIncrease = 1
        countchcker = 0
        top_headlines = newsapi.get_everything(q=args,
                                               # sources='bbc-news',
                                               from_param=pastdate,
                                               to=FormatDate,
                                               language='en',
                                               sort_by='relevancy',
                                               page=pageIncrease)
        z = 2
        if top_headlines['totalResults'] == '0':
            await ctx.send("No articles regarding the following topic")
        else:
            for i in top_headlines['articles'][0:5]:
                title = i['title']
                author = i['author']
                url = i['url']
                content = i['description']
                advertisement = ['feature', 'learn',
                                 '$', 'Feature', 'Learn', 'bundle']
                if any(word in title for word in advertisement) or any(word in content for word in advertisement):
                    pass
                else:
                    embedVar = discord.Embed(
                        title=title, description=content, color=discord.Color.dark_green())
                    embedVar.add_field(
                        name='Made by:', value=author, inline=False)
                    embedVar.add_field(name='URL:', value=url, inline=True)
                    await ctx.send(embed=embedVar)

    @bot.command()
    async def sc(ctx, *, args):
        args = args.lower()
        await bot.change_presence(activity=discord.Game(name=args))
        await ctx.send("Changed status too: {}".format(args.lower()))

    @bot.command()
    async def statuschange(ctx, *, args):
        args = args.lower()
        await bot.change_presence(activity=discord.Game(name=args))
        await ctx.send("Changed status too {}".format(args.lower()))

    @bot.command()
    async def searchfor(ctx, arg):
        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"

        querystring = {"q": arg, "pageNumber": "1",
                       "pageSize": "7", "autoCorrect": "true"}

        headers = {
            'x-rapidapi-key': "998a3437bdmshca45d523e5bd524p1ab9f7jsnc47fb6c3852f",
            'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        jsonLoads = json.loads(response.text)

        counter = 0
        for i in jsonLoads['value']:
            if counter == 7:
                await ctx.send(f"Search results: {jsonLoads['totalCount']}")
            title = i['title']
            description = i['body']
            url = i['url']
            author = i['provider']['name']
            embedSearchResults = discord.Embed(title=title, description=description,
                                               color=discord.Color.from_rgb(214, 171, 79))
            embedSearchResults.add_field(
                name='Author:', value=author, inline=False)
            embedSearchResults.add_field(name='URL:', value=url, inline=False)
            await ctx.send(embed=embedSearchResults)
            counter += 1

    class Links(dict):
        @bot.group()
        async def links(ctx):
            if ctx.invoked_subcommand is None:
                await ctx.send('Type a command after $links')

        @links.command()
        async def get(ctx, arg):
            siteDictionary = {
                'focus': 'https://fs.duvalschools.org/adfs/ls/?client-request-id=55ae1dd4-f220-49ca-c404-008000240084&RedirectToIdentityProvider=AD+AUTHORITY',
                'student software': 'https://dcps.duvalschools.org/Page/18553',
                'anime': 'https://vrv.co/', 'youtube': 'https://www.youtube.com/',
                'episode': 'https://www.youtube.com/watch?v=RzClCJFpSoM&t=13s', 'aryan': 'https://www.youtube.com/'}
            arg = arg.lower()
            if arg in siteDictionary:
                await ctx.send('<' + siteDictionary[arg] + '>')

        @links.command()
        async def add(ctx, arg1, arg2):
            arg1, arg2 = arg1.lower(), arg2.lower()




    @bot.command()
    async def add(ctx, arg1, arg2, arg3):
        List1 = [arg1, arg2, arg3]
        DataFrame = pd.DataFrame(data=List1, columns=["Hw Name", "Date", "Description"])

class events:
    @bot.event
    async def on_ready():
        print(f"{bot.user} is online")

    @bot.event
    async def on_message(message):
        if (message.author == bot.user):
            return
        else:
            messageContent = message.content.lower()
            emojipeople = {
                'aryan': "<:Hi:774326299862106133>",
                'teja': EMOJIS[':alien:'],
                'erik': "<:eik:774326564035756044>",
                'pranav': '<:randomkid:771409396512981002>',
                'maanas': '<:breathboy:803704140718276698>',
                'viraat': "<:saturnboy:803305564104425482>",
                'oviya': "<:Oviya:771439844269359174>",
                'ani': "<:depressedkid:788119418198556682>",
                'anirudh': "<:depressedkid:788119418198556682>",
                'vs': EMOJIS[':crossed_swords:'],
                'v.s': EMOJIS[':crossed_swords:']
                }
            for i in emojipeople:
                if i in messageContent.split():
                    await message.add_reaction(emojipeople[i])
            badwords = ['stupid', 'idiot', 'moron', 'retard', 'fifield', 'hate', 'k-drama', 'gifted', 'kumon', ]
            for i in badwords:
                if i in messageContent.split():
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} that is inappropriate, Word: {i.upper()} should not be used")



        await bot.process_commands(message)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            return
        raise error

bot.run('Nzc4Njc4NTU3NDc5MTQxMzg2.X7Ve6w.sdTsRyZYtgG74WmQtmjJrMThjw4')
