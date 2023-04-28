#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:08:17 2023

@author: ajas
"""

import discord, random, serial, time
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import datetime


# client = commands.Bot(command_prefix="$")
intents = discord.Intents.all()

client = commands.Bot(command_prefix="$", intents=intents)

ledstate = False
#serport = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1)
serport = serial.Serial("/dev/tty.usbserial-140", baudrate=9600, timeout=0.5)

##utc = datetime.timezone.utc
##time = datetime.time(hour=2, minute=55, tzinfo=utc)

@client.event
async def on_ready():
    print("Bot Prepared!")

##@tasks.loop(seconds=5.0)
##async def myLoop(ctx):
##    print("Task Time")
##    serport.write(b's')
##    await ctx.send("Scheduled Time")

##class Pump:
##    @tasks.loop(time=time)
##    async def myLoop(ctx):
##        print("Task Time")
##        await ctx.send("Scheduled Time")

#@client.command()
# async def toggle(ctx):
#     global ledstate
#     ledstate = not ledstate
#     if ledstate:
#         serport.write(b'o')
#         await ctx.send("Turned led Off")
#     else:
#         serport.write(b'f')
#         await ctx.send("Turned led On")
# @client.command()
# async def on(ctx):
#         serport.write(b'f')
#         await ctx.send("Turned led On")
# @client.command()
# async def off(ctx):
#         serport.write(b'o')
#         await ctx.send("Turned led off")

    
@client.command()
async def feedfish(ctx):
    serport.write(b's')
    await ctx.send("Feeding the Fish")


# Run client ------------------------------------------------------------------- #
client.run("MTA5NjIzODQxNDAwMjY2MzQ1Ng.Gamsq1.xXp7diWdrWwButIHxPF5O9V1Plx-1vFqeGir_k")
