import discord
import datetime
from time import gmtime, strftime
from datetime import date
import time
import asyncio
import os
from discord.ext import tasks
from discord.utils import get
from discord.ext import commands

token = os.environ.get('BOT_TOKEN')
bot = discord.Client()
@bot.event
@bot.event
async def on_ready():
	for guild in bot.guilds:
		print("deploy message")
		channel_id = discord.utils.get(guild.channels, name="reminders")
		channel = bot.get_channel(channel_id.id)
		await channel.send("This is an automatic message and will be deleted after a few seconds.")
	await asyncio.sleep(5)
	for guild in bot.guilds:
		print("delete message")
		channel_id = discord.utils.get(guild.channels, name="reminders")
		channel = bot.get_channel(channel_id.id)
		async for msg in channel.history(limit = 50):
			await msg.delete()
async def time_check():
	await bot.wait_until_ready()
	print("Bot ready")
	print(bot.is_closed)
	while not bot.is_closed():
		print("Inside loop")
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		print(current_time)
		today = date.today()
		print(today)
		d = today.strftime("%a")
		role = get(guild.roles, name='Subscribed')
		channel_id = discord.utils.get(guild.channels, name="reminders")
		channel = bot.get_channel(channel_id.id)
		if (d == "Mon" or d == "Tue" or d == "Wed" or d == "Thu" or d == "Fri") and (today != 2020-11-3 or today != 2020-11-26 or today != 2020-11-27 or today != 2020-12-17 or today != 2020-12-18 or today != 2020-12-21 or today != 2020-12-22 or today != 2020-12-23 or today != 2020-12-24):
			if d == "Wed" and current_time >= "07:53:30" and current_time <= "07:54:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("FBLA is starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if current_time >= "08:33:30" and current_time <= "08:34:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Period 1 is starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)					
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
							await msg.delete()
			if current_time >= "09:29:30" and current_time <= "09:30:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Period 2 is starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if current_time >= "10:21:30" and current_time <= "10:22:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Period 3 is starting in a minute. ")
					await channel.send(role.mention)
					await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if current_time >= "11:13:30" and current_time <= "11:14:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Period 4 is starting in a minute. ")
					await channel.send(role.mention)
					await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if current_time >= "12:05:30" and current_time <= "12:06:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Period 5 is starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if current_time >= "12:57:30" and current_time <= "12:58:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Period 6 is starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if current_time >= "13:49:30" and current_time <= "13:50:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Period 7 is starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if current_time >= "14:41:30" and current_time <= "14:42:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Period 8 is starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if d == "Mon" and current_time >= "15:43:30" and current_time <= "15:44:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("Computer Science Club in starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if d == "Mon" and current_time >= "17:00:00" and current_time <= "17:01:00":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("School is over.")
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if d == "Thu" and current_time >= "15:28:30" and current_time <= "15:29:30":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("History Bee/Bowl is starting in a minute. ")
					await channel.send(role.mention)
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if d == "Thu" and current_time > "16:30:00" and current_time < "16:31:00":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("School is over.")
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			if (d == "Tue" or d == "Wed" or d == "Fri") and current_time >= "15:20:00" and current_time <= "15:21:00":
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					await channel.send("School is over.")
				await asyncio.sleep(600)
				for guild in bot.guilds:
					channel_id = discord.utils.get(guild.channels, name="reminders")
					channel = bot.get_channel(channel_id.id)
					async for msg in channel.history(limit = 50):
						await msg.delete()
			await asyncio.sleep(60)
		
		elif d == "Sat" or d == "Sun":
			print("Weekend")
			await asyncio.sleep(1800)
		
		elif (today == 2020-11-3 or today == 2020-11-26 or today == 2020-11-27 or today == 2020-12-17 or today == 2020-12-189 or today == 2020-12-21 or today == 2020-12-22 or today == 2020-12-23 or today == 2020-12-24):
			for guild in bot.guilds:
				channel_id = discord.utils.get(guild.channels, name="reminders")
				channel = bot.get_channel(channel_id.id)
				await channel.send("Today is off.")
				await channel.send(role.mention)
			await asyncio.sleep(60000)
			for guild in bot.guilds:
				channel_id = discord.utils.get(guild.channels, name="reminders")
				channel = bot.get_channel(channel_id.id)
				async for msg in channel.history(limit = 50):
					await msg.delete()
bot.loop.create_task(time_check())

bot.run(token)
