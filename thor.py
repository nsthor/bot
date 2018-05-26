""" Musical Bot : Thor

Discord Bot release by IT from Stud-IO
"""
__author__ = 'ANTOINE Alecsandre\nDABE Christophe\nGUILLAUME Audren'
__copyright__ = 'All rights reserved, Stud-IO 2018'
__version__ = 'Alpha_0.0.1'

# Discord
import discord
import youtube_dl

# Web
from bs4 import BeautifulSoup
import requests
from urllib import parse, request

# System
import logging
import asyncio
import os, time, random, json
import subprocess

# Custom classes
# from player import * as Player
from roles import get_role_number, get_help_message




# Init discord client
client = discord.Client()
client.login(255423383783604227)

# Client launched
@client.event
async def on_ready():
    """
        Lancement du bot
    """
    print('\nLogged in as')
    print(' '+client.user.name)
    print(' '+client.user.id)




# Retrieve author's role
# Possible roles are defined in roles.py file
def get_member_roles(author):
    roles = []
    for r in author.roles:
        n = r.name
        roles.append(get_role_number(n))
    roles.sort()
    return roles[0]



async def help_message(rank, author):
    print(get_help_message(rank))
    private_msg = await client.start_private_message(author)
    await client.send_message(private_msg, get_help_message(rank))



# Command receiving
# Here are treated the differents commands sent by users
if __name__ == '__main__':

    print("Im the one who knocks ... ")

    # Main Discord Function
    # Wait Message
    # Do Something
    @client.event
    async def on_message(message):
        author = message.author
        rank = get_member_roles(author)

        # Defined function for on message events
        if message.content.startswith('!help'):
            await help_message(rank, author)

        if message.content.startswith('!join'):
            print("Not implemented yet")

        if message.content.startswith('!player'):
            print("Not implemented yet")

        #
        # if message.content.startswith('!link'):
        #     await yt_link(message)
        #
        # if message.content.startswith('!name'):
        #     await yt_name(message)
        #
        # if message.content.startswith('!run'):
        #     player = Player(client, author)
        #     #player.run2(author.voice_channel)
        #
        # if message.content.startswith('!play'):
        #     player.start2()
        #
        # if message.content.startswith('!pause'):
        #     player.pause2()
        #
        # if message.content.startswith('!skip'):
        #     player.skip2()
        #
        # if message.content.startswith('!stop'):
        #     player.stop2()
        #
        # if message.content.startswith('!vote'):
        #     player.vote2()



    client.run('MjU1NDIzMzgzNzgzNjA0MjI3.Cydbfw.ZHrhxbHrldZhSQr1QJKYNh1tUE8')
pass
