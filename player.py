import os
import discord
import requests
import asyncio
default_volume = 0.5

class Player :

    def __init__(self, client, member):
        # self.loop = loop
        self.client = client
        print(self.client.user.name+ " ::: "+ member.voice_channel.name)
        # self.voice_author = member.voice_channel
        self.voice_client = None
        connect_channel(member.voice_channel)
        print(self.client.is_voice_connected(member.server))
        print(self.voice_client)
        self.playlist = {}
        self.volume = default_volume


    async def connect_channel(voiceCh):
        self.voice_client = await self.client.join_voice_channel(voiceCh)

    def play(self,title,url):
        """ Play song """
        if len(playlist) == 0 :
            voice_client
        else :
            """Add To Queue"""
            playlist[title] = url
        playlist[i].start()

    async def pause(*args):
        #dekfeoijgeoigj
        print("mabite")

    def play_pause(command):
        #troreorkeok
        print("mabite")

    def run2(channel):
        #voice_client = await client.move_to(channel)
        play()
        while not playlist[i].is_done() :
            print("mabite")

    async def skip(*args):
        print("mabite")

    async def vol(*args):
        print("mabite")


    async def add(*args):
        print("add")

    def start2():
        print("start2")

    def stop2():
        print("stop2")

    def list2():
        print("list2")
