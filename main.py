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


@client.event
async def on_ready():
    print("Bot Prepared!")
    
@client.command()
async def feedfish(ctx):
    serport.write(b's')
    await ctx.send("Feeding the Fish")


# Run client ------------------------------------------------------------------- #
client.run("MTA5NjIzODQxNDAwMjY2MzQ1Ng.Gamsq1.xXp7diWdrWwButIHxPF5O9V1Plx-1vFqeGir_k")
