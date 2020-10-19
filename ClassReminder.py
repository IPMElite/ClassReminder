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
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
#msg = "This is an automatic message per launch and will be deleted after a few seconds."
async def on_ready():
	try:
		await bot.send_message(discord.utils.get(server.channels, name = "reminders"), "This is an automatic message per launch and will be deleted after a few seconds.")
	except:
		print("Creating new channel")
		await bot.create_channel(server, "reminder", type discord.ChannelType.text)
		message = await bot.send_message(discord.utils.get(server.channels, name = "reminders"), "This is an automatic message per launch and will be deleted after a few seconds.")
		await asyncio.sleep(5)
		await bot.delete_message(message)
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
		#channel = bot.get_channel(764596098437349401)
		channel = bot.get_channel(discord.utils.get(server.channels, name = "reminders"))
		if (d == "Mon" or d == "Tue" or d == "Wed" or d == "Thu" or d == "Fri") and (today != 2020-11-3 or today != 2020-11-26 or today != 2020-11-27 or today != 2020-12-17 or today != 2020-12-18 or today != 2020-12-21 or today != 2020-12-22 or today != 2020-12-23 or today != 2020-12-24):
			if d == "Wed" and current_time >= "7:55:00" and current_time <= "8:20:00":
				await channel.send( "FBLA is starting in a minute.")
			if current_time >= "8:33:30" and current_time <= "8:34:30":
				await channel.send("Period 1 is starting is a minute.")
			if current_time >= "9:29:30" and current_time <= "9:30:30":
				await channel.send("Period 2 is starting is a minute.")
			if current_time >= "10:21:30" and current_time <= "10:21:30":
				await channel.send("Period 3 is starting is a minute.")
			if current_time >= "11:13:30" and current_time <= "11:14:30":
				await channel.send("Period 4 is starting is a minute.")
			if current_time >= "12:05:30" and current_time <= "12:06:30":
				await channel.send("Period 5 is starting is a minute.")
			if current_time >= "12:57:30" and current_time <= "12:58:30":
				await channel.send("Period 6 is starting is a minute.")
			if current_time >= "13:49:30" and current_time <= "13:50:30":
				await channel.send("Period 7 is starting is a minute.")
			if current_time >= "14:41:30" and current_time <= "14:42:30":
				await channel.send("Period 8 is starting is a minute.")
			if d == "Mon" and current_time >= "15:43:30" and current_time <= "15:44:30":
				await channel.send("Computer Science Club is starting in a minute.")
			if d == "Mon" and current_time >= "16:30:00" and current_time <= "16:31:00":
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

bot.loop.create_task(time_check())
bot.run(token)
