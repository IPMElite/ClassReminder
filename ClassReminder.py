import discord
import datetime
from time import gmtime, strftime
from datetime import date
import time
import asyncio
import os
from discord.ext import tasks
from discord.utils import get

num = 60
token = os.environ.get('BOT_TOKEN')
bot = discord.Client()

@bot.event
@bot.event
#msg = "This is an automatic message per launch and will be deleted after a few seconds."
#async def on_ready():
#	try:
#		channel = bot.get_channel(discord.utils.get(guild.channels, name = "reminders")
#		await channel.send("This is an automatic message per launch and will be deleted after a few seconds.")
#	except:
#		print("Creating new channel")
		#server = ctx.message.server
		#await bot.create_channel(server, "reminder", type=discord.ChannelType.text)
#		channel = await guild.create_text_channel('reminders')
#		message = await channel.send("This is an automatic message per launch and will be deleted after a few seconds.")
#		await asyncio.sleep(5)
#		await bot.delete_message(message)
#		await asyncio.sleep(4)
async def on_ready():
	channel = bot.get_channel(767857071944892426)
	message = await channel.send("React to this message to subscribe to reminders")
	await bot.add_reaction(message, emoji='🔔')
async def on_reaction_add(reaction, user):
	ChID = '767857071944892426'
	if reaction.message.channel.id != ChID:
		return
	if reaction.emoji == "🔔":
		Subscribed = discord.utils.get(user.server.roles, name="Subscribed")
	await client.add_roles(user, Subscribed)
async def time_check():
	print("Running time check")
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
		# print(d)
		channel = bot.get_channel(767855423775572018)
		#channel = bot.get_channel(discord.utils.get(server.channels, name = "reminders"))
		if (d == "Mon" or d == "Tue" or d == "Wed" or d == "Thu" or d == "Fri") and (today != 2020-11-3 or today != 2020-11-26 or today != 2020-11-27 or today != 2020-12-17 or today != 2020-12-18 or today != 2020-12-21 or today != 2020-12-22 or today != 2020-12-23 or today != 2020-12-24):
			if d == "Wed" and current_time >= "07:53:30" and current_time <= "07:54:30":
				await channel.send( "FBLA is starting in a minute.")
			if current_time >= "08:33:30" and current_time <= "08:34:30":
				await channel.send("Period 1 is starting in a minute.")
			if current_time >= "09:29:30" and current_time <= "09:30:30":
				await channel.send("Period 2 is starting in a minute.")
			if current_time >= "10:20:30" and current_time <= "10:21:30":
				await channel.send("Period 3 is starting in a minute.")
			if current_time >= "11:13:30" and current_time <= "11:14:30":
				await channel.send("Period 4 is starting in a minute.")
			if current_time >= "12:05:30" and current_time <= "12:06:30":
				await channel.send("Period 5 is starting in a minute.")
			if current_time >= "12:57:30" and current_time <= "12:58:30":
				await channel.send("Period 6 is starting in a minute.")
			if current_time >= "13:49:30" and current_time <= "13:50:30":
				await channel.send("Period 7 is starting in a minute.")
			if current_time >= "14:41:30" and current_time <= "14:42:30":
				await channel.send("Period 8 is starting in a minute.")
			if d == "Mon" and current_time >= "15:43:30" and current_time <= "15:44:30":
				await channel.send("Computer Science Club in starting in a minute.")
			if d == "Mon" and current_time >= "16:45:00" and current_time <= "16:46:00":
				await channel.send("School is over.")
			if d == "Thu" and current_time >= "15:28:30" and current_time <= "15:29:30":
				await channel.send("History Bee/Bowl is starting in a minute.")
			if d == "Thu" and current_time > "16:30:00" and current_time < "16:40:00":
				await channel.send("School is over.")
			if (d == "Tue" or d == "Wed" or d == "Fri") and current_time >= "15:20:00" and current_time <= "15:21:00":
				await channel.send("School is over.")
			await asyncio.sleep(60)
		elif d == "Sat" or d == "Sun":
			print("Weekend")
			await asyncio.sleep(1800)
#async def on_reaction_add(reaction, user):
#	ChID = '767857071944892426'
#	if reaction.message.channel.id != ChID:
#		return
#	if reaction.emoji == ":hourglass:":
#		Subscribed = discord.utils.get(user.server.roles, name="Subscribed")
#	await client.add_roles(user, Subscribed)
#async def on_ready():
#	channel = bot.get_channel(767857071944892426)
#	role = discord.utils.get(
#	message = await channel.send("Please react to this message if you wish to subscribe to reminders for each period.")
bot.loop.create_task(time_check())
bot.run(token)
